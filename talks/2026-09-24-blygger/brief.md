# Talk Brief — Blygger at the Protocol Symposium 2026

Operator inputs. Not published — this file is the input, not part of the deck. The
deck itself is one file, `talk.md`; edit that for content.

Structure dictated by Venkat, session 21 (2026-09-16). Drafted by Opus 5 from existing
collateral: `blygger-spec/docs/protocol-v0.2.md`, the locked decisions in
`blygger-spec/CLAUDE.md`, `docs/notes/tn-1-versioning-and-pins.md`, `docs/roadmap.md`,
and the two live nodes.

**Round 2 — session 24 (2026-09-22), currency pass.** The deck was drafted at session
21, when v0.3 was still "next". Since then Phase A shipped and went live on both nodes
(2026-09-20), the public responses list landed, and `forked_from` landed today — so the
single biggest claim in the deck had gone stale in the author's favour. What changed:

- **Two new slides, 08 and 09** ("Quoting across origins", "A list, never a count"),
  after transclusion and before TK. Both carry new screenshots of the *live* stub stack
  between the two nodes, taken 2026-09-22, holding to the every-example-is-real rule.
- **Slide 20 (roadmap) rewritten.** v0.3 moved from "next" to shipped, and the ordering
  — implementation first, normative document after — is now stated as the method
  (decision #21) rather than left as a status line.
- **Slide 23 (if you build):** test count ~420 → ~500; added that the wire is at 0.3
  while the published document is 0.2, with the reason, because a protocol audience
  will notice the gap and the honest answer is better than being caught by it.
- **Slide 24 (resources):** added blygger.com, and deleted the line saying blygger.com
  was not yet built — it shipped at session 21, in the same session this brief was
  written.
- **Content-guide pass, same session.** `talk-kit/sync.py --check` reports the theme in
  sync, so the visual style was already applied; what had never been applied were the
  *content* limits in `talk-kit/theme/talk-content-guide.md`. Measured with
  `reference/check-deck.js` at 1536×864: **nothing was clipping**, but six slides missed
  the design targets, two of them because of this session's own additions. Fixed:
  - **18 "The wire, for protocol people"** — 12 lines, the worst in the deck, six bullets
    that all wrapped. Now six one-line bullets; the dropped detail ("ground truth, full
    archive", "suspected history rewrite") moved to the cues, where it was always going
    to be spoken anyway.
  - **08 and 09** — 5 bullets each over a screenshot. The guide gives a diagram slide 4
    free lines before the image starts shrinking, and asks for 3–4 bullets. Both now 4.
  - **03 "Two kinds of time"** — 9 lines from *two* bullets, i.e. two paragraphs with
    dots on them. Same content as short bullets plus one sub-bullet each; the prose
    definitions moved to the cues. Venkat's opening content, so the substance and the
    title are unchanged.
  - **20 (roadmap)** and **23 (if you build)** — 9 lines each, both inflated earlier in
    this same session. Back to 5 lines.
  - **17** — the only two-line title in the deck (53 chars), which costs two bullet lines
    of budget. Now "Nothing is deleted. Pins are forever." at 37.
  After: **all 24 slides within target, no clipping, no two-line titles.** Slide 01 (9
  lines) is the densest and is deliberate — it is Venkat's opening and the brief already
  calls it "a dense opening list rather than a slow build".
- **Fork lineage on slide 17** (added after an audit found it missing — the two new
  slides were written before `forked_from` was built the same day, and nothing went
  back for it). It belongs on the pins slide rather than a new one: that slide already
  says a pin is "an irrevocable promise to host one exact version, forever" and never
  said what the promise is *for*. Forking is the answer — only a pinned version is
  guaranteed to still be there, so it is the only thing anyone can safely descend from.
  One bullet, six now on that slide, still inside target. **The cue tells the speaker
  not to offer a demo:** this landed the same week and is not on the live nodes, so it
  is the one claim in the deck with no live artifact behind it. **Deployed to both
  nodes the same evening**, so the cue now says the opposite: the mechanism is live and
  can be shown from the studio, but nothing has been forked in public yet, so there is
  no finished example on a page. Publishing one is Venkat's call — it is content on his
  own blyg, not a deploy.
- **Every screenshot re-shot or re-cropped** (Venkat: the screenshot slides were
  hard to read). The old captures were full-page shots at 100% zoom with the content
  column occupying about a third of the frame, so the thing each slide pointed at —
  the version line, the provenance caption, the citation's fine print — rendered
  around 10px at 1080p, against the guide's 24px floor. Re-captured live at 1.35–1.6×
  browser zoom in an 860px window and cropped to the artifact, which is roughly a 3×
  gain in apparent size. `images/` is now all PNG; the old JPEGs are gone.
  - **Slide 13 changed shape, not just size.** It was a three-pane capture of the whole
    editor, and the brief already admitted nobody could read it. The argument is one
    visual fact — *these blocks are blue here and not blue there* — so it is now the
    preview pane alone, croppable to a landscape strip that the stage sizes on width.
    The source pane's content is already covered as code on slide 10, in type the room
    can read. Bullets and cues rewritten to match; a portrait first attempt was
    rejected after measuring, because a tall image is height-constrained and starved
    at four bullets exactly as the guide warns.
- **The venkateshrao screenshots were stale, not just small.** That node's theme is now
  dark; the session-21 captures are light. Both nodes are now shot as they actually
  render, which means slides 06/07 are dark and 08/09/11 are light. That is a real
  difference between two people's sites, so slide 08 gets a cue that says so —
  themes are the author's, and the protocol's only claim about them is the CSS
  contract. If the mixed palette reads as an accident from the room, the fix is to
  set both nodes to the same theme and re-shoot, not to fake one.
- **Slide 11 was factually wrong and is fixed.** It said "One of these I wrote. One a
  model wrote." The live item document says two generated scopes, both paragraphs
  carrying `blyg-tk-gen`, `claude-opus-5` — the only thing Venkat wrote is the one-line
  heading. This is a page the audience can inspect in three seconds, which is the exact
  failure the every-example-is-real rule exists to prevent. The question is now "**How
  much of this did a model write?**", the answer moved onto slide 12's cues, and the
  slide got stronger: the room will assume the long confident paragraph is human.
- **One cue direction fixed:** the no-counts point is now *planted* on slide 09 and
  *collected* on slide 16 ("You don't get a username"), not described as a callback on
  the earlier slide — it comes first now, so it sets the beat up rather than paying
  one off.

## Event

- **Conference:** Protocol Symposium 2026
- **Slot:** Thursday 2026-09-24, 23:00 UTC (4:00 PM PDT) — confirmed by Venkat 2026-09-16
- **Duration:** still unstated. **24 slides** as of round 2; at a brisk improvised
  pace that is roughly 22 minutes, and the deck cuts cleanly at four places if the
  slot is shorter — the technical pair (18–19), the participation split (21–23
  collapsing to one), slide 05, and now slide 09 ("A list, never a count"), which is
  the cheapest cut of the four because slide 08 stands alone and slide 16 makes the
  no-counts argument anyway. **Cut slide 09 before slide 08:** the cross-origin
  mechanism is the v0.3 headline and the rest of the deck now refers to it.
- **Delivery:** assumed Zoom screen share, slides advanced manually, no audio track
- **Speaker:** Venkatesh Rao

The date is the directory name and therefore the URL, so it is now fixed:
`/talks/2026-09-24-blygger/`. There are deliberately no word budgets or spoken-time
estimates — the talk is improvised to the slides, so both would measure the wrong thing.

## Audience

Mixed, and the structure assumes it. The middle of the deck (slides 12–15) is written
for publisher/author types with no protocol background — no jargon, motivation first.
Slides 16–17 are the opposite: written for protocol engineers, jargon deliberately
unhedged ("eventual consistency", "AP under partition", "enshrined"). The UX section
(06–11) should work for both, because it is screenshots and one worked example.

## Structure (Venkat's, verbatim in shape)

1. **Slides 01–05 — Venkat's opening, supplied 2026-09-16 and wired in.** What Blygger
   is; the etymology (blyg/Blogger/Yggdrasil); then three slides building the
   synchronic/diachronic argument — defining both terms with examples, naming why one
   medium struggles to do both (clumsy threads, editable-tweet provenance, unread
   changelogs), and closing on books as the one working solution and its cost (very,
   very slow; editions years apart).
2. **Slides 06–11 — UX.** The TK mechanism, transclusion and generative expansion with
   real examples, screenshots of the public and composition UI.
3. **Slides 12–15 — how the protocol works, ELI5**, motivation-first: RSS
   compatibility, no author namespaces in the protocol, withdraw-and-pin. Explicable to
   a normal publisher/author.
4. **Slides 16–17 — technical.** Protocol-engineer jargon is fine here.
5. **Slide 18 — roadmap.**
6. **Slides 19–21 — how authors, publishers, and developers can participate.**
7. **Slide 22 — resources.**

## Content decisions made while drafting

- **Every example is real and live**, not invented. The transclusion example is
  `venkateshrao.com/blyg/t/1vgtgz0g…`; the TK example is
  `blyg.protocol-institute.org/t/5zq1kdfptt…`, whose two generated scopes cite two real
  source fragments. Screenshots are of those exact pages. A protocol audience checks.
- **Slides 09–10 are built around the fact that you cannot tell.** The published TK page
  does not visually mark generated prose (decision #25), so slide 09 shows the page and
  asks the room, and slide 10 answers. Split across two deliberately: a slide that
  answers its own question while asking it is not asking it, because the room reads the
  bullets faster than the speaker can set the beat up.
- **The opening's temporality argument is called back twice**, so it does not sit inert:
  slide 06 names the version line as a diachronic surface inside a synchronic feed, and
  slide 15 names a pin as the book's edition at conversation speed.
- **Slide 14 (no usernames) is the ELI5 section's load-bearing one.** It is the decision
  most likely to be argued with by this audience and the one with the most worked-out
  record behind it (decision #11).
- **The roadmap slide (18) states the pre-1.0 no-promises stance** (decision #21) rather than
  burying it. Inviting participation without it would be a misrepresentation.

## Open / needs Venkat

- **Event date, slot length, and whether Q&A is separate** — see above.
- **Slide 13's screenshot is deliberately unreadable at presentation size.** It is a
  wide two-pane capture in a short slot, so the room sees the *shape* — source left,
  preview right, generated blocks tinted blue — and not the text. The cues say so. If
  the detail turns out to matter, the fix is a second slide cropped to one pane, not a
  bigger version of this one.
- **Slide 08's screenshot is the same case** (round 2). Its fine print — the citation's
  item id, version and retrieval date — will not read from the room, and does not need
  to: what the room reads is the three-layer shape (citation block, their quoted
  paragraph inside it, my text below). The cues now say so explicitly rather than
  leaving the speaker to discover it at the lectern.
- **Whether this belongs on blygger.org at all.** Session 20 settled the site's genres
  as normative text + technical notes; a talk is a third. Built under `/talks/` on the
  assumption that Venkat asking for it settles it, but it is one directory to delete.
- **Slide 07's example is still scratch content.** The only *local* transclusion
  published on either node is `venkateshrao.com/blyg/t/1vgtgz0g…`, whose prose is
  "The famous blyg" / "This is NOT the most famous blyg ever" / "Heading test" /
  "Quick brown fox". Round 2 cropped to the first quoted block, which hides most of it
  and shows the mechanism cleanly — but the two visible lines are still obviously a
  test fixture, in a deck whose stated rule is that every example is real. Every other
  thread on that node has `transclusions: []`. Ten minutes of authoring would fix it;
  it is content on the live blyg, so it is Venkat's call, same as the fork example.
- **Round 2: is 24 slides too many for an unstated slot?** The cut order above is a
  recommendation, not a decision. If the slot turns out to be 15 minutes the deck needs
  a real edit rather than four cuts, and the section to compress is the opening (05) plus
  the participation split.
