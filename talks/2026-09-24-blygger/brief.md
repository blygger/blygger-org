# Talk Brief — Blygger at the Protocol Symposium 2026

Operator inputs. Feeds `slides.yaml` and `track.md`. Not published — this file is the
input, not part of the deck.

Structure dictated by Venkat, session 21 (2026-09-16). Drafted by Opus 5 from existing
collateral: `blygger-spec/docs/protocol-v0.2.md`, the 25 locked decisions in
`blygger-spec/CLAUDE.md`, `docs/notes/tn-1-versioning-and-pins.md`, `docs/roadmap.md`,
and the two live nodes.

## Event — TO CONFIRM

- **Conference:** Protocol Symposium 2026 (assumed — same event as the Humboldt talk)
- **Date:** 2026-09-24 **(placeholder — the slug and `meta.date` both need the real slot)**
- **Duration:** assumed ~20 min + Q&A **(placeholder — drives the word budgets)**
- **Delivery:** assumed Zoom screen share, slides advanced manually, no audio track
- **Speaker:** Venkatesh Rao

Everything above marked placeholder is guessed. Correcting the date means renaming the
directory (the slug is the URL) and editing `meta.date`; correcting the duration means
re-cutting word budgets, which is why the per-slide budgets are visible on the page.

## Audience

Mixed, and the structure assumes it. The middle of the deck (slides 10–13) is written
for publisher/author types with no protocol background — no jargon, motivation first.
Slides 14–15 are the opposite: written for protocol engineers, jargon deliberately
unhedged ("eventual consistency", "AP under partition", "enshrined"). The UX section
(05–09) should work for both, because it is screenshots and one worked example.

## Structure (Venkat's, verbatim in shape)

1. **Slides 01–04 — placeholders, Venkat's content.** Where the idea came from, the
   etymology of the name, shortcomings in existing media it addresses, how it tackles
   constructing an AI-native medium. Four slides of room, as asked.
2. **Slides 05–09 — UX.** The TK mechanism, transclusion and generative expansion with
   real examples, screenshots of the public and composition UI.
3. **Slides 10–13 — how the protocol works, ELI5**, motivation-first: RSS
   compatibility, no author namespaces in the protocol, withdraw-and-pin. Explicable to
   a normal publisher/author.
4. **Slides 14–15 — technical.** Protocol-engineer jargon is fine here.
5. **Slide 16 — roadmap.**
6. **Slides 17–19 — how authors, publishers, and developers can participate.**
7. **Slide 20 — resources.**

## Content decisions made while drafting

- **Every example is real and live**, not invented. The transclusion example is
  `venkateshrao.com/blyg/t/1vgtgz0g…`; the TK example is
  `blyg.protocol-institute.org/t/5zq1kdfptt…`, whose two generated scopes cite two real
  source fragments. Screenshots are of those exact pages. A protocol audience checks.
- **Slide 08 is built around the fact that you cannot tell.** The published TK page does
  not visually mark generated prose (decision #25), so the slide shows the page, asks
  the room which paragraph was generated, and then shows the JSON. This is the strongest
  single demonstration of the disclosure stance and it costs one slide.
- **Slide 12 (no usernames) is the ELI5 section's load-bearing one.** It is the decision
  most likely to be argued with by this audience and the one with the most worked-out
  record behind it (decision #11).
- **The roadmap slide states the pre-1.0 no-promises stance** (decision #21) rather than
  burying it. Inviting participation without it would be a misrepresentation.

## Open / needs Venkat

- **Slides 01–04**: all four are stubs with a one-line prompt and an empty `bullets`
  list. `track.md` carries a `[PLACEHOLDER]` marker each.
- **Slide 09 needs a composition-UI screenshot.** The studio is behind a login and the
  agent cannot enter a password, so `images/studio-composer.png` is missing and the
  slide currently renders without an image. Grab one of the fragment or thread editor
  with a TK scope open and drop it in at that filename.
- **Event date, slot length, and whether Q&A is separate** — see above.
- **Whether this belongs on blygger.org at all.** Session 20 settled the site's genres
  as normative text + technical notes; a talk is a third. Built under `/talks/` on the
  assumption that Venkat asking for it settles it, but it is one directory to delete.
