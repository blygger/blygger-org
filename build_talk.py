#!/usr/bin/env python3
"""
build_talk.py — render talks/<slug>/talk.md into dist/talks/<slug>/.

Ported from humboldt-site/build.py::_build_talk (Protocol Institute's Humboldt
project, same symposium), minus the audio machinery: no per-slide narration audio,
no timing.json, no elapsed/progress transport, no cache-busting content hashes.

What that removal changes structurally: in humboldt's version the entire player is
gated on audio existing, because without a clip there is nothing to drive slide
advance. Here the deck is driven by the operator, so the stage is *always* built and
only the transport controls are conditional — which means the gate had to be
inverted rather than deleted.

**One source file per talk**, so content can be iterated without touching structure:

    talks/<slug>/talk.md     YAML frontmatter + the whole deck
    talks/<slug>/images/     copied alongside
    talks/<slug>/brief.md    operator input, deliberately NOT published

This replaced a slides.yaml/track.md pair. Splitting "what is projected" from "what
is said" across two files meant every edit to a slide touched two places and kept
them in sync by hand — which is exactly how a renumber once produced two slides
sharing an id. Here a slide is one contiguous block of markdown.

Format inside talk.md:

    # Heading        starts a SECTION (applies to the slides that follow)
    ## Heading       starts a SLIDE
    ![alt](path)     the slide's image — ordinary markdown, alt text included
    - a list         what is PROJECTED; nest with two spaces for sub-bullets
    **Cues**         speaker prompts, rendered below the fold, never projected
    **Notes**        "why this slide exists", collapsed on the page

Slides are numbered by position, so inserting or reordering renumbers the rest and
there are no ids to keep in sync. Bullets are rendered through the markdown pipeline
rather than escaped as plain strings, which is what buys sub-bullets and inline
`code`/**emphasis** on the stage.

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
# The presentation theme is a plain CSS file, not a string in this module, because
# it is SHARED across the symposium decks (artisanal-bots, blygger-org, humboldt)
# and a stylesheet is the artifact all three can hold identically. It is read here
# and inlined into the page: no extra request, so fullscreen never waits on the
# network, and the built index.html stays a single self-contained file.
THEME = ROOT / "talk-theme.css"

_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
_IMAGE_RE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)\)\s*$", re.M)
# A block label on its own line: **Cues** / **Notes**. Case-insensitive so the file
# stays forgiving to edit by hand.
_LABEL_RE = re.compile(r"^\*\*(Cues|Notes)\*\*\s*$", re.M | re.I)


def _attr(s: str) -> str:
    """Collapse whitespace and escape for an HTML attribute — alt text taken from a
    markdown image may wrap across lines in the source."""
    return html.escape(" ".join(str(s or "").split()), quote=True)


_LIST_ITEM_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<marker>[-*+]|\d+[.)])\s")


def normalize_list_indent(md: str) -> str:
    """Re-indent nested list items to 4 spaces per level.

    Python-Markdown (with sane_lists, which build.py enables) only recognises a
    nested list at 4-space indentation. Nobody hand-writing a slide types four
    spaces — two is the natural thing, and two silently produced a flat list with
    no error anywhere. Rather than make the source file awkward, map whatever
    indent steps the author actually used onto levels and re-emit at 4 per level,
    so 2-, 3- and 4-space nesting all work.
    """
    widths = sorted({len(m.group("indent").expandtabs(4))
                     for m in (_LIST_ITEM_RE.match(l) for l in md.splitlines()) if m})
    if len(widths) < 2:
        return md
    level = {w: i for i, w in enumerate(widths)}

    out, cur = [], 0
    for line in md.splitlines():
        m = _LIST_ITEM_RE.match(line)
        if m:
            cur = level[len(m.group("indent").expandtabs(4))]
            out.append(" " * (cur * 4) + line.strip())
        elif line.strip():
            # A continuation line belongs to the item above it.
            out.append(" " * (cur * 4 + 2) + line.strip() if cur else line)
        else:
            out.append(line)
    return "\n".join(out)


def parse_talk(path: Path) -> tuple[dict, list[dict]]:
    """Parse talk.md into (meta, slides). Each slide is a dict with title, section,
    image, image_alt, and the raw markdown for projected / cues / notes."""
    text = path.read_text("utf-8")

    m = _FRONTMATTER_RE.match(text)
    if not m:
        sys.exit(f"{path}: missing YAML frontmatter (--- ... --- at the top of the file)")
    meta = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]

    # Strip HTML comments before splitting: the format documentation lives in one at
    # the top of the file and contains literal "## Heading" examples.
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)

    slides: list[dict] = []
    section = ""
    # Split on headings, keeping the level and the text.
    parts = re.split(r"^(#{1,2}) +(.+?)\s*$", body, flags=re.M)
    # parts[0] is any preamble; then repeating (hashes, title, content).
    for i in range(1, len(parts), 3):
        level, title, content = parts[i], parts[i + 1], parts[i + 2]
        if level == "#":
            section = title
            continue

        img_m = _IMAGE_RE.search(content)
        image = image_alt = None
        if img_m:
            image, image_alt = img_m.group("src"), img_m.group("alt")
            content = content[:img_m.start()] + content[img_m.end():]

        blocks = {"projected": "", "cues": "", "notes": ""}
        label_ms = list(_LABEL_RE.finditer(content))
        blocks["projected"] = content[:label_ms[0].start()] if label_ms else content
        for j, lm in enumerate(label_ms):
            end = label_ms[j + 1].start() if j + 1 < len(label_ms) else len(content)
            blocks[lm.group(1).lower()] = content[lm.end():end]

        slides.append({
            "title": title,
            "section": section,
            "image": image,
            "image_alt": image_alt,
            **{k: v.strip() for k, v in blocks.items()},
        })

    if not slides:
        sys.exit(f"{path}: no slides found (a slide is a '## Heading')")
    return meta, slides


def build_talk(talk_dir: Path, dist: Path, template: str, md_render) -> str | None:
    """Build one talk. Returns its output path relative to dist, or None if skipped.

    `md_render` is build.py's markdown renderer, passed in rather than imported so
    this module stays independent of build.py's module-level state.
    """
    talk_path = talk_dir / "talk.md"
    if not talk_path.exists():
        print(f"  talk {talk_dir.name} -> skipped (no talk.md)")
        return None

    meta, slides = parse_talk(talk_path)

    title = meta.get("title", "Talk")
    event = meta.get("event", "")
    speaker = meta.get("speaker", "")
    date_s = str(meta.get("date", ""))
    try:
        # Weekday included: a conference runs several days and "Thursday" is how
        # anyone actually holds which slot this is.
        date_h = datetime.strptime(date_s, "%Y-%m-%d").strftime("%A, %-d %B %Y")
    except ValueError:
        date_h = date_s
    if meta.get("time"):
        date_h = f"{date_h} &middot; {html.escape(str(meta['time']))}"

    # ── TOC + per-slide sections ──
    toc_rows, sections, deck = [], [], []
    missing_images: list[str] = []

    for n, s in enumerate(slides, start=1):
        sid = f"{n:02d}"
        s_title = s["title"]
        section = s["section"]
        # A slide with nothing to project has not been written yet. Derived rather
        # than declared, so the flag cannot go stale against the content.
        is_stub = not s["projected"].strip()

        img = s["image"]
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

        # Bullets go through markdown, which is what buys sub-bullets and inline
        # code/emphasis on the stage. The source is the author's own file, trusted
        # here the same way content/*.md already is.
        bullets_html = md_render(normalize_list_indent(s["projected"])) if s["projected"] else ""
        visual = ""
        if img:
            visual = (f'<div class="slide-image"><img src="{html.escape(img)}" '
                      f'alt="{_attr(s["image_alt"])}" loading="lazy"></div>')

        if is_stub:
            cues_html = ('<p class="stub-note"><em>Placeholder — nothing to project '
                         'on this slide yet.</em></p>')
        elif s["cues"]:
            cues_html = md_render(normalize_list_indent(s["cues"]))
        else:
            cues_html = "<p><em>No cues yet.</em></p>"

        note_html = ""
        if s["notes"]:
            note_html = (
                '        <details class="slide-note">\n'
                "          <summary>Why this slide exists</summary>\n"
                f"          {md_render(s['notes'])}\n"
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
        {bullets_html}
      </div>
      <div class="slide-cues">
        <span class="cues-label">Cues</span>
{cues_html}
      </div>
{note_html}    </section>""")

        deck.append({
            "id": sid,
            "title": s_title,
            "section": section,
            "bulletsHtml": bullets_html,
            "image": img,
            "imageAlt": " ".join(str(s["image_alt"] or "").split()),
            "stub": is_stub,
        })

    n_stub = sum(1 for d in deck if d["stub"])

    # ── the cover slide ──
    # Generated from frontmatter rather than authored, for two reasons. It is the
    # same three facts on every deck (title, speaker, event), so hand-writing it in
    # each talk.md would be three chances to let it drift from the page header that
    # states the same thing; and it makes the cover free for any talk that adopts
    # this pipeline, which is the point of sharing the theme at all.
    #
    # It is slide **00**, so it does not renumber the deck: slides stay 01..NN and
    # every #slide-NN permalink already published still lands where it did. It is
    # player-only — there is no transcript section for it, because the page header
    # immediately above the player already says all three things in running text,
    # and a cues block under a cover would have nothing to hold.
    try:
        cover_date = datetime.strptime(date_s, "%Y-%m-%d").strftime("%-d %B %Y")
    except ValueError:
        cover_date = date_s
    cover_html = f"""\
        <div class="stage-cover" id="stage-cover" hidden>
          <p class="cover-event">{html.escape(event)}</p>
          <h2 class="cover-title">{html.escape(title)}</h2>
          <hr class="cover-rule">
          <p class="cover-speaker">{html.escape(speaker)}</p>
          <p class="cover-meta">{html.escape(cover_date)}</p>
        </div>"""
    deck.insert(0, {
        "id": "00", "title": title, "section": "", "bulletsHtml": "",
        "image": None, "imageAlt": "", "stub": False, "cover": True,
    })

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
      <p class="talk-tagline">{html.escape(event)} &nbsp;&middot;&nbsp; {date_h}
         &nbsp;&middot;&nbsp; {html.escape(speaker)}</p>
    </div>

    <div class="talk-player" id="talk-player">
      <div class="stage" id="stage">
{cover_html}
        <div class="stage-inner">
          <div class="stage-meta">
            <span id="stage-num">Slide 01</span>
            <span id="stage-section"></span>
          </div>
          <h2 id="stage-title"></h2>
          <div id="stage-visual" class="stage-visual" hidden></div>
          <div id="stage-bullets"></div>
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

  var inner = document.querySelector('.stage-inner');
  var cover = document.getElementById('stage-cover');

  function render() {
    var d = DECK[i];
    // The cover is a different composition, not a slide with empty fields, so it
    // swaps the whole stage body rather than blanking the title and bullets.
    if (cover) {
      cover.hidden = !d.cover;
      inner.hidden = !!d.cover;
    }
    if (d.cover) {
      stage.classList.remove('stage-stub');
      pos.textContent = String(i + 1);
      fill.style.width = ((i + 1) / DECK.length * 100) + '%';
      return;
    }
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
    // Rendered markdown, built and escaped at build time — which is what lets a
    // slide carry sub-bullets and inline code, neither of which survives a
    // textContent-per-bullet loop.
    document.getElementById('stage-bullets').innerHTML = d.bulletsHtml || '';
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
        .replace("{{DESCRIPTION}}", _attr(f"{title}. {event}, {date_s}. Slides and speaker cues."))
        .replace("{{PROMPT}}", f"{html.escape(event)} &middot; {date_h}")
        .replace("{{RAIL_LABEL}}", "Slides")
        .replace("{{RAIL_ITEMS}}", "\n".join(
            f'      <li><a href="#slide-{d["id"]}">{html.escape(d["title"])}</a></li>'
            for d in deck if not d.get("cover")))
        .replace("{{CONTENT}}", body)
    )
    page = page.replace("</body>", f"<style>{_talk_css()}</style>\n<script>{js}</script>\n</body>")

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


def _talk_css() -> str:
    """The shared presentation theme, read at build time.

    Deliberately not cached in a module global: a build is a one-shot process, and
    reading it per build means editing talk-theme.css and re-running is enough —
    no stale copy survives in an interactive session.
    """
    if not THEME.exists():
        sys.exit(f"missing {THEME.name} — the shared presentation theme, which "
                 "lives beside this file. Copy it from whichever sibling talk "
                 "project has it (artisanal-bots, blygger-org); they are identical.")
    return THEME.read_text("utf-8")
