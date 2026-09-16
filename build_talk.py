#!/usr/bin/env python3
"""
build_talk.py — render talks/<slug>/{slides.yaml,track.md} into dist/talks/<slug>/.

Ported from humboldt-site/build.py::_build_talk (Protocol Institute's Humboldt
project, same symposium), minus the audio machinery: no per-slide narration audio,
no timing.json, no elapsed/progress transport, no cache-busting content hashes.

What that removal changes structurally: in humboldt's version the entire player is
gated on audio existing, because without a clip there is nothing to drive slide
advance. Here the deck is driven by the operator, so the stage is *always* built and
only the transport controls are conditional — which means the gate had to be
inverted rather than deleted.

Two source files per talk:

    talks/<slug>/slides.yaml   what is PROJECTED — meta + per-slide bullets
    talks/<slug>/track.md      what is SAID — "## NN — Title" sections

and optionally talks/<slug>/images/, copied alongside. brief.md is operator input
and is deliberately not published.

Install once:
    /opt/homebrew/bin/python3 -m pip install pyyaml --break-system-packages
"""

import html
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml not installed.\nRun: /opt/homebrew/bin/python3 -m pip install pyyaml --break-system-packages")

ROOT = Path(__file__).parent
TALKS = ROOT / "talks"

_TRACK_SECTION_RE = re.compile(r"^## (\d{2}) — (.*)$", re.M)


def _attr(s: str) -> str:
    """Collapse whitespace and escape for an HTML attribute. YAML block scalars keep
    their newlines, which are legal in an attribute but make the source unreadable and
    break naive alt-text extraction."""
    return html.escape(" ".join(str(s or "").split()), quote=True)


def read_track(path: Path) -> dict[str, str]:
    """Parse track.md into {slide_id: narration}."""
    text = path.read_text("utf-8")
    out: dict[str, str] = {}
    matches = list(_TRACK_SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[m.group(1)] = text[m.end():end].strip()
    return out


def build_talk(talk_dir: Path, dist: Path, template: str, md_render) -> str | None:
    """Build one talk. Returns its output path relative to dist, or None if skipped.

    `md_render` is build.py's markdown renderer, passed in rather than imported so
    this module stays independent of build.py's module-level state.
    """
    slides_path, track_path = talk_dir / "slides.yaml", talk_dir / "track.md"
    if not (slides_path.exists() and track_path.exists()):
        print(f"  talk {talk_dir.name} -> skipped (no slides.yaml/track.md)")
        return None

    spec = yaml.safe_load(slides_path.read_text("utf-8"))
    meta = spec.get("meta", {})
    slides = spec.get("slides", [])
    track = read_track(track_path)

    title = meta.get("title", "Talk")
    event = meta.get("event", "")
    speaker = meta.get("speaker", "")
    date_s = meta.get("date", "")
    try:
        date_h = datetime.strptime(date_s, "%Y-%m-%d").strftime("%-d %B %Y")
    except ValueError:
        date_h = date_s

    # Structural checks before anything renders. Both of these have already gone
    # wrong once: a hand renumber left two slides sharing an id, which produced two
    # #slide-10 anchors and a deck that silently skipped a position, and the build
    # said nothing. Cheap to check, invisible when it breaks.
    ids = [str(x.get("id", "")).zfill(2) for x in slides]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        sys.exit(f"{talk_dir.name}/slides.yaml: duplicate slide ids {dupes}")
    orphans = sorted(set(track) - set(ids))
    if orphans:
        sys.exit(f"{talk_dir.name}/track.md: cue sections with no slide: {orphans}")

    # ── TOC + per-slide sections ──
    toc_rows, sections, deck = [], [], []
    missing_images: list[str] = []

    for s in slides:
        sid = str(s.get("id", "")).zfill(2)
        s_title = s.get("title", "")
        section = s.get("section") or ""
        is_stub = bool(s.get("placeholder"))
        narration = track.get(sid, "").strip()

        img = s.get("image")
        if img and not (talk_dir / img).exists():
            missing_images.append(f"{sid}: {img}")
            img = None

        stub_tag = '<span class="stub-tag">to write</span>' if is_stub else ""
        toc_rows.append(
            f'      <tr><td class="toc-num"><a href="#slide-{sid}">{sid}</a></td>'
            f'<td><a href="#slide-{sid}">{html.escape(s_title)}</a></td>'
            f'<td class="toc-section">{html.escape(section)}</td>'
            f'<td class="toc-stub">{stub_tag}</td></tr>'
        )

        bullets = "".join(f"<li>{html.escape(str(b))}</li>" for b in s.get("bullets") or [])
        visual = ""
        if img:
            visual = (f'<div class="slide-image"><img src="{html.escape(img)}" '
                      f'alt="{_attr(s.get("image_alt"))}" loading="lazy"></div>')

        if is_stub:
            narr_html = ('<p class="stub-note"><em>Placeholder — cues to be written '
                         'by the speaker.</em></p>')
        elif narration:
            narr_html = md_render(narration)
        else:
            narr_html = "<p><em>No cues yet.</em></p>"

        note = (s.get("notes") or "").strip()
        note_html = ""
        if note:
            note_html = (
                '        <details class="slide-note">\n'
                "          <summary>Why this slide exists</summary>\n"
                f"          {md_render(note)}\n"
                "        </details>\n"
            )

        sections.append(f"""\
    <section class="talk-slide{' is-stub' if is_stub else ''}" id="slide-{sid}">
      <div class="slide-head">
        <span class="slide-num">Slide {sid}</span>
        <span class="slide-section">{html.escape(section)}</span>
        <a href="#slide-{sid}" class="slide-permalink" title="Permalink to slide {sid}">&sect;</a>
      </div>
      <h2>{html.escape(s_title)}</h2>
      <div class="slide-projected">
        <span class="projected-label">On screen</span>
        {visual}
        <ul>{bullets}</ul>
      </div>
      <div class="slide-cues">
        <span class="cues-label">Cues</span>
{narr_html}
      </div>
{note_html}    </section>""")

        deck.append({
            "id": sid,
            "title": s_title,
            "section": section,
            "bullets": [str(b) for b in (s.get("bullets") or [])],
            "image": img,
            "imageAlt": " ".join(str(s.get("image_alt") or "").split()),
            "stub": is_stub,
        })

    n_stub = sum(1 for d in deck if d["stub"])

    banner = ""
    if meta.get("review_round"):
        opened = meta.get("review_opened", "")
        banner = f"""\
    <div class="talk-review">
      <p><strong>Draft — review round {meta['review_round']}</strong>{f", opened {opened}" if opened else ""}.
         This is the deck for a talk not yet given, published before delivery.
         The boxed bullets are what the room sees; the cues below them are the
         speaker's own prompts, not a script &mdash; the talk is improvised to the slides.</p>
      <p>Every slide has a <a href="#slide-01">&sect; permalink</a>{f" &mdash; {n_stub} slides are still placeholders." if n_stub else "."}</p>
    </div>"""

    body = f"""\
    <div class="talk-header">
      <h1>{html.escape(title)}</h1>
      <p class="talk-tagline">{html.escape(event)} &nbsp;&middot;&nbsp; {html.escape(date_h)}
         &nbsp;&middot;&nbsp; {html.escape(speaker)}</p>
    </div>

    <div class="talk-player" id="talk-player">
      <div class="stage" id="stage">
        <div class="stage-inner">
          <div class="stage-meta">
            <span id="stage-num">Slide 01</span>
            <span id="stage-section"></span>
          </div>
          <h2 id="stage-title"></h2>
          <div id="stage-visual" class="stage-visual" hidden></div>
          <ul id="stage-bullets"></ul>
        </div>
      </div>
      <div class="player-bar">
        <button id="prev" class="pbtn" aria-label="Previous slide">&#9664;</button>
        <button id="next" class="pbtn" aria-label="Next slide">&#9654;</button>
        <span class="ptime"><span id="pos">1</span> / {len(deck)}</span>
        <div class="pprogress"><div class="pprogress-fill" id="pfill"></div></div>
        <button id="fs" class="pbtn" aria-label="Full screen">&#9974; Full screen</button>
      </div>
      <p class="player-hint">Arrow keys step. Full screen to present.</p>
    </div>
{banner}
    <div class="talk-meta">
      <span><strong>{len(slides)}</strong> slides</span>
      <span><strong>{len(set(d["section"] for d in deck if d["section"]))}</strong> sections</span>
      {f'<span><strong>{n_stub}</strong> to write</span>' if n_stub else ""}
      {f'<span>Target <strong>{html.escape(str(meta.get("slot_display")))}</strong></span>' if meta.get("slot_display") else ""}
    </div>

    <table class="talk-toc">
      <tbody>
{chr(10).join(toc_rows)}
      </tbody>
    </table>

{chr(10).join(sections)}"""

    js = "var DECK = " + json.dumps(deck) + ";\n" + r"""
(function () {
  var i = 0;
  var stage = document.getElementById('stage');
  var pos = document.getElementById('pos');
  var fill = document.getElementById('pfill');

  function render() {
    var d = DECK[i];
    document.getElementById('stage-num').textContent = 'Slide ' + d.id;
    document.getElementById('stage-section').textContent = d.section || '';
    document.getElementById('stage-title').textContent = d.title;
    var vis = document.getElementById('stage-visual');
    if (d.image) {
      var img = document.createElement('img');
      img.src = d.image;
      img.alt = d.imageAlt || '';
      vis.innerHTML = '';
      vis.appendChild(img);
      vis.hidden = false;
    } else {
      vis.innerHTML = '';
      vis.hidden = true;
    }
    var ul = document.getElementById('stage-bullets');
    ul.innerHTML = '';
    d.bullets.forEach(function (b) {
      var li = document.createElement('li');
      li.textContent = b;
      ul.appendChild(li);
    });
    stage.classList.toggle('stage-stub', !!d.stub);
    pos.textContent = String(i + 1);
    fill.style.width = ((i + 1) / DECK.length * 100) + '%';
  }

  function go(n) {
    i = Math.max(0, Math.min(DECK.length - 1, n));
    render();
    if (location.hash !== '#slide-' + DECK[i].id) {
      history.replaceState(null, '', '#slide-' + DECK[i].id);
    }
  }

  document.getElementById('next').addEventListener('click', function () { go(i + 1); });
  document.getElementById('prev').addEventListener('click', function () { go(i - 1); });
  document.getElementById('fs').addEventListener('click', function () {
    if (document.fullscreenElement) { document.exitFullscreen(); }
    else if (stage.requestFullscreen) { stage.requestFullscreen(); }
  });

  // Arrows step the deck, but never while the reader is in a form field or has
  // followed a transcript link and is reading below the fold.
  document.addEventListener('keydown', function (e) {
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.metaKey || e.ctrlKey) return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); go(i + 1); }
    if (e.key === 'ArrowLeft'  || e.key === 'PageUp')   { e.preventDefault(); go(i - 1); }
  });

  // Deep link: /talks/<slug>/#slide-07 opens the deck on that slide.
  var m = /^#slide-(\d{2})$/.exec(location.hash || '');
  if (m) {
    var n = DECK.findIndex(function (d) { return d.id === m[1]; });
    if (n >= 0) i = n;
  }
  render();
})();
"""

    page = (
        template
        .replace("{{TITLE}}", html.escape(f"{title} — blygger"))
        .replace("{{DESCRIPTION}}", _attr(f"{title}. {event}, {date_h}. Slides and full narration."))
        .replace("{{PROMPT}}", f"{html.escape(event)} &middot; {html.escape(date_h)}")
        .replace("{{RAIL_LABEL}}", "Slides")
        .replace("{{RAIL_ITEMS}}", "\n".join(
            f'      <li><a href="#slide-{d["id"]}">{html.escape(d["title"])}</a></li>' for d in deck))
        .replace("{{CONTENT}}", body)
    )
    page = page.replace("</body>", f"<style>{TALK_CSS}</style>\n<script>{js}</script>\n</body>")

    out = dist / "talks" / talk_dir.name / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, "utf-8")

    img_dir = talk_dir / "images"
    n_img = 0
    if img_dir.is_dir():
        dest = out.parent / "images"
        dest.mkdir(exist_ok=True)
        for f in sorted(img_dir.iterdir()):
            if f.is_file() and not f.name.startswith("."):
                shutil.copy2(f, dest / f.name)
                n_img += 1

    rel = out.relative_to(dist)
    print(f"  talks/{talk_dir.name}  ->  {rel}  ({len(slides)} slides, {n_img} images)")
    if missing_images:
        # Not fatal: a deck under construction should still build. But silence here
        # would mean a slide quietly loses its screenshot between now and the talk.
        for miss in missing_images:
            print(f"    ! missing image, slide {miss}")
    if n_stub:
        print(f"    ! {n_stub} placeholder slides still to write")
    return str(rel)


def build_talks(dist: Path, template: str, md_render) -> list[str]:
    """Build every talk under talks/. Returns output paths."""
    if not TALKS.is_dir():
        return []
    built = []
    for d in sorted(TALKS.iterdir()):
        if d.is_dir() and not d.name.startswith("."):
            r = build_talk(d, dist, template, md_render)
            if r:
                built.append(r)
    return built


TALK_CSS = """
.talk-header { margin-bottom: 1.6rem; }
.talk-header h1 { margin-bottom: 0.3rem; }
.talk-tagline { color: #6b6b66; font-size: 0.95rem; margin: 0; }

/* The deck breaks out of the prose column: a 16:9 stage inside a reading measure
   is a postage stamp, and this page's primary job is the deck. */
.talk-player { margin: 0 0 2.2rem; width: min(100%, 60rem); }
@media (min-width: 1200px) { .talk-player { width: 52rem; } }
/* The stage is a fixed 16:9 box and its contents must fit inside it, which rules
   out letting anything size itself from its own content. It is therefore a flex
   column: meta and title take what they need, bullets take what they need, and the
   image gets whatever is left over and no more.

   The `min-height: 0` is load-bearing. A flex item's default `min-height: auto`
   refuses to shrink below its content, so an image slide would push the bullets out
   of the bottom of the stage. (A percentage `max-height` does not work here either:
   the parent has no definite height, so it resolves to `none` — which is exactly the
   bug this replaced, where a tall screenshot pushed the title off the top.) */
/* The stage is a SIZE CONTAINER and everything inside it is sized in cqh — 1% of
   the stage's own height. That is what makes the composition resolution-independent:
   the embedded 16:9 preview and the fullscreen presentation are the same slide at
   two scales, rather than two layouts that each need tuning.

   Sizing in rem/vw instead is what produced the bug this replaced — the embedded
   stage is only ~350px tall inside a 64rem column, so absolute type left a 2-pixel
   screenshot on one slide and pushed two bullets off the bottom of another, while
   the same CSS looked fine fullscreen. Anything added here should be in cqh too. */
.stage { background: #1d2024; border-radius: 5px; aspect-ratio: 16 / 9;
  display: flex; align-items: stretch; overflow: hidden;
  container-type: size; }
.stage-inner { padding: 5cqh 5cqh 4cqh; width: 100%;
  display: flex; flex-direction: column; min-height: 0; }
.stage-meta { display: flex; gap: 1.6cqh; align-items: baseline; font-size: 2.6cqh;
  letter-spacing: 0.1em; text-transform: uppercase; color: #7f8790;
  margin-bottom: 2cqh; flex: 0 0 auto; }
#stage-title { font-size: 7.2cqh; color: #fafaf7;
  margin: 0 0 3cqh; line-height: 1.18; flex: 0 0 auto; }
/* Bullets are the slide's content and the image is support, so the bullets take
   their natural height and the image gets the remainder. The reverse ordering
   silently truncated four bullets to one, which is the worse failure: a squeezed
   screenshot is visibly squeezed, whereas a clipped list looks like a short list.
   If the image ends up tiny, the slide has too many bullets — say so by showing it. */
#stage-bullets { margin: 0; padding-left: 3.5cqh; flex: 0 0 auto; }
#stage-bullets li { color: #d8dade; max-width: none; margin-bottom: 1.6cqh;
  font-size: 4.1cqh; line-height: 1.35; }
#stage-bullets li::marker { color: #6f7780; }
/* Takes the leftover room, never more; the image scales to fit what it is given. */
.stage-visual { flex: 1 1 auto; min-height: 0; display: flex;
  align-items: center; justify-content: center; margin: 0 0 2.5cqh; }
/* `display: flex` above is a class rule and outranks the UA's [hidden] { display:
   none }, so without this an image-less slide still reserved the flex space and the
   bullets sat pinned to the bottom of the stage with a hole above them. */
.stage-visual[hidden] { display: none !important; }
.stage-visual img { max-width: 100%; max-height: 100%; width: auto; height: auto;
  object-fit: contain; border-radius: 3px; border: 1px solid #333a42; }
/* A placeholder slide should be unmistakable from the back of a room. */
.stage.stage-stub { background: #2a2118; outline: 2px dashed #6b5a3e; outline-offset: -8px; }

.player-bar { display: flex; align-items: center; gap: 0.6rem; margin-top: 0.85rem;
  flex-wrap: wrap; }
.pbtn { font-family: inherit; font-size: 0.82rem; color: #3a3a36; background: #f0f0ec;
  border: 1px solid #e0e0da; border-radius: 3px; padding: 0.42rem 0.7rem;
  cursor: pointer; line-height: 1; }
.pbtn:hover { background: #f6ebe4; color: #d95a1f; border-color: #e8cdb9; }
.ptime { font-size: 0.78rem; color: #888; font-variant-numeric: tabular-nums;
  white-space: nowrap; }
.pprogress { flex: 1 1 6rem; height: 3px; background: #e8e8e4; border-radius: 2px;
  overflow: hidden; min-width: 4rem; }
.pprogress-fill { height: 100%; width: 0; background: #d95a1f; transition: width 0.2s linear; }
.player-hint { font-size: 0.76rem; color: #9a9a94; margin: 0.5rem 0 0; }

/* Fullscreen only changes the container's size; cqh carries the rest. */
.stage:fullscreen { border-radius: 0; aspect-ratio: auto; height: 100%; }

.talk-review { background: #fbf4ef; border-left: 3px solid #d95a1f; padding: 1rem 1.3rem;
  margin-bottom: 1.8rem; border-radius: 0 3px 3px 0; }
.talk-review p { font-size: 0.92rem; margin-bottom: 0.6rem; }
.talk-review p:last-child { margin-bottom: 0; }

.talk-meta { display: flex; flex-wrap: wrap; gap: 1.6rem; font-size: 0.85rem; color: #666;
  padding-bottom: 1.1rem; border-bottom: 1px solid #e8e8e4; margin-bottom: 1.4rem; }
.talk-meta strong { font-weight: 600; color: #1a1a1a; }

.talk-toc { font-size: 0.88rem; margin-bottom: 3rem; width: 100%; border-collapse: collapse; }
.talk-toc td { padding: 0.3rem 0.75rem 0.3rem 0; border-bottom: 1px solid #f0f0ec; }
.talk-toc .toc-num { width: 2.5rem; color: #999; font-variant-numeric: tabular-nums; }
.talk-toc .toc-num a { color: #999; }
.talk-toc .toc-section { width: 11rem; color: #9a9a94; font-size: 0.8rem; }
.talk-toc .toc-stub { width: 5rem; text-align: right; }

.stub-tag { font-size: 0.7rem; letter-spacing: 0.04em; text-transform: uppercase;
  color: #8a6a2b; background: #faf2e4; padding: 0.1rem 0.4rem; border-radius: 2px; }

.talk-slide { margin-bottom: 3.2rem; scroll-margin-top: 2rem; }
.talk-slide h2 { margin-top: 0.35rem; margin-bottom: 1rem; }
.slide-head { display: flex; align-items: baseline; gap: 0.75rem; font-size: 0.75rem;
  letter-spacing: 0.05em; text-transform: uppercase; color: #999; }
.slide-num { font-weight: 600; }
.slide-section { color: #b5b5ae; }
.slide-words { margin-left: auto; text-transform: none; letter-spacing: 0;
  font-variant-numeric: tabular-nums; }
.slide-words.over { color: #a4552f; }
.slide-permalink { color: #ccc; text-decoration: none; }
.slide-permalink:hover { color: #d95a1f; }

.slide-projected { background: #1d2024; border-radius: 4px; padding: 1.1rem 1.4rem 1.2rem;
  margin-bottom: 1.3rem; }
.projected-label { display: block; font-size: 0.68rem; letter-spacing: 0.1em;
  text-transform: uppercase; color: #7f8790; margin-bottom: 0.6rem; }
.slide-projected ul { margin: 0; padding-left: 1.1rem; }
.slide-projected ul:empty { display: none; }
.slide-projected li { color: #e8e8e4; font-size: 0.95rem; line-height: 1.5;
  margin-bottom: 0.35rem; max-width: none; }
.slide-projected li::marker { color: #6f7780; }
.slide-image { margin: 0 0 0.8rem; text-align: center; }
.slide-image img { max-width: 100%; height: auto; border-radius: 4px;
  border: 1px solid #333a42; }

.talk-slide.is-stub .slide-projected { background: #2a2118; }
.stub-note { color: #8a6a2b; }

.slide-cues { border-left: 2px solid #ece7e2; padding-left: 1rem; }
.cues-label { display: block; font-size: 0.68rem; letter-spacing: 0.1em;
  text-transform: uppercase; color: #b5b5ae; margin-bottom: 0.5rem; }
.slide-cues ul { margin: 0; padding-left: 1.1rem; }
.slide-cues li { font-size: 0.95rem; line-height: 1.6; margin-bottom: 0.35rem; }
.slide-cues p { font-size: 0.95rem; line-height: 1.6; }
.slide-note { margin-top: 1rem; font-size: 0.86rem; }
.slide-note summary { cursor: pointer; color: #888; font-size: 0.75rem;
  letter-spacing: 0.05em; text-transform: uppercase; }
.slide-note summary:hover { color: #d95a1f; }
.slide-note p { margin-top: 0.6rem; color: #555; padding-left: 0.9rem;
  border-left: 2px solid #e8e8e4; }

@media (max-width: 640px) {
  .talk-meta { gap: 1rem; }
  .slide-head { flex-wrap: wrap; gap: 0.5rem; }
  .slide-words { margin-left: 0; }
  .talk-toc .toc-section { display: none; }
}
"""
