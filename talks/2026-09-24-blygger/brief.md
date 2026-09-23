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
- **Slide 11's screenshot is deliberately unreadable at presentation size.** It is a
  wide two-pane capture in a short slot, so the room sees the *shape* — source left,
  preview right, generated blocks tinted blue — and not the text. The cues say so. If
  the detail turns out to matter, the fix is a second slide cropped to one pane, not a
  bigger version of this one.
- **Whether this belongs on blygger.org at all.** Session 20 settled the site's genres
  as normative text + technical notes; a talk is a third. Built under `/talks/` on the
  assumption that Venkat asking for it settles it, but it is one directory to delete.
- **Round 2: is 24 slides too many for an unstated slot?** The cut order above is a
  recommendation, not a decision. If the slot turns out to be 15 minutes the deck needs
  a real edit rather than four cuts, and the section to compress is the opening (05) plus
  the participation split.
