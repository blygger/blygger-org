# Cues — Blygger at the Protocol Symposium 2026

Speaker cues, not a script. Venkat speaks to the slides and improvises; these are
prompts, the things worth not forgetting, and the few phrasings that are load-bearing
enough to be worth having on hand.

Sections are `## NN — Title` and must match the slide ids in `slides.yaml`.

Slides 01–04 are Venkat's own and are stubbed.

## 01 — Where this came from

[PLACEHOLDER — Venkat]

## 02 — Why "blygger"

[PLACEHOLDER — Venkat]

## 03 — What existing media get wrong

[PLACEHOLDER — Venkat]

## 04 — The AI-native problem

[PLACEHOLDER — Venkat]

## 05 — A blyg is fragments and threads

- Live page, mine, right now.
- Two units, not one: **fragment** = a note; **thread** = fragments composed.
- Most media give you one unit and you pretend everything is that shape.
- Point at the version line: *v3 · pinned v1, v3*. Every item wears its revision
  history in public. Needs no explanation — it's on the page.

## 06 — Transclusion: quote by reference

- The blue-ruled block is not copy-paste. I wrote `![[id]]` on its own line.
- **Snapshotted at publish.** Reader gets the bytes I saw. Editing the source later
  never rewrites this quote.
- Embeds break or drift. This can't do either.
- Caption carries provenance: which item, which version.
- If there's a line worth landing: quoting is the load-bearing act in written culture
  and most media made it worse.

## 07 — [TK]: leave an instruction in the draft

- TK = copy-desk mark, "to come". A century old. Text known to be missing.
- Form 1: instruction not yet run. Form 2: same scope after running — instruction and
  output both still in the draft, side by side.
- **The subtle bit, say it slowly:** inside a TK scope, `![[id]]` means *source*, not
  quote. Same syntax, two meanings, decided by whether it's inside a scope.
- Generation is always deliberate and reviewed. Publishing never generates. Publishing
  with an unresolved scope is an error.

## 08 — Which paragraph was generated?

- Real published page from the other node. Two paragraphs. One mine, one a model's.
- **Ask the room. Let it sit.** Take a guess or two. Do not answer on this slide.

## 09 — You can't tell. That is deliberate.

- Answer: you can't tell. Nothing on the page marks it.
- Show what the page *does* carry: `generated[{sources, model, at}]` in the JSON;
  `blyg-tk-gen` class in the HTML, visible in view-source in three seconds.
- Disclosure is total. It just isn't decorative.
- **Why no tint:** provenance is self-asserted, nothing verifies it, a colour would
  start meaning "verified". A badge that looks authoritative and isn't is worse than
  no badge.
- Second reason if there's room: I read it and kept it. At that point it's mine.

## 10 — Writing it

- That's what a reader gets; this is what I get.
- Point isn't the interface — it's the **split**. Private studio, public page. The
  protocol governs only the page.
- Everything on this screen is my client's choice and no part of the standard.
- So a completely different client isn't non-compliant, it's just a different studio.

## 11 — It's just files

- A blyg is a directory. Manifest, feed, one JSON per item, a page per item. That's it.
- No database in the protocol. Mine uses one because it's a live authoring tool.
- Copy the directory to any static host; every reader still works.
- Mounts anywhere — root, subdirectory, subdomain. Protocol never assumes.
- Don't ask them to take it on faith: we export the whole blyg to flat files and diff
  against what the live server serves.

## 12 — It's still RSS

- Valid RSS. Not RSS-like.
- Existing readers work today. A reader that's never heard of blygger loses nothing.
- Works the other direction too: a blyg can subscribe to any RSS/Atom feed, no
  cooperation needed.
- Anecdote if useful: subscribed mine to Simon Willison; he publishes Atom, which is
  how Atom support got written.
- **Frame for publishers:** you're already half in. You can be read. What upgrading
  buys is being *quotable*.

## 13 — You don't get a username

- No accounts, no handles, no `@you@server`. No namespace to be in.
- Your domain is your name. DNS already exists and already works.
- **The argument:** every namespace is a registry, every registry has an owner, and the
  owner is the thing we were trying not to have.
- Author names are decoration — optional, per-item, protocol promises nothing.
- Only the origin is authenticated.
- Follow it through: no follower lists, no counts, no follow requests. Subscribing is
  client-local and invisible. There is no number to go up.
- Expect pushback here. This is the slide they'll argue with.

## 14 — Nothing is deleted. Some things are promised forever.

- No hard delete. Only exit is **withdraw** — permanent visible endcap, URL answers
  forever, says "withdrawn".
- **Pin** = irrevocable promise to host exact bytes at an exact URL, forever.
- Pins survive withdrawal. That's the point. Withdraw the piece, the cited version
  still resolves.
- Unpinned versions are served by no route in any representation. Otherwise withdrawal
  would be theatre.
- **The line:** an edition bump is cheap talk; a pin is a costly signal. So the
  machine-readable "this matters" is the expensive one, not the free one.

## 15 — The wire, for protocol people

- Gear change — jargon is fine here.
- Two planes. `items/{id}.json` = state, ground truth, full archive. `feed.xml` =
  notification, lossy, just a signal. Nothing important lives only in the feed.
- AP under partition, no pretending otherwise. Convergence poll-driven and eventual:
  ~25 min measured, ~45 worst case. No cross-origin consistency guarantee, ever.
- **The inversion worth explaining:** reconciliation surface is the archive index, not
  the feed. So a dropped entry / clock skew / malformed feed degrades to a slower sync,
  not data loss — which is what lets the notification plane be as lossy as RSS is.
- Watermarks never silently regress: a lower version is surfaced as suspected history
  rewrite, not applied. Loud, not prevented.
- IDs stable random 128-bit, never content-addressed — identity must survive editing.
- L0–L3 strict supersets; unknown constructs ignored, not rejected.

## 16 — What is deliberately not enshrined

- Four decisions, months apart, same ending each time.
- AI — generation is studio-side; wire gets output + provenance.
- Identity — opaque, client-asserted, never addressable.
- Editorial convenience — no reply primitive, ever. Transclusion is the primitive.
  Speech about someone else's work should cost an editorial act.
- Significance markup — no semver, no edition field. Pins carry the weight.
- I didn't notice the pattern until the fourth one.
- **Principle:** anything the protocol can't verify, it declines to represent — because
  a field that looks authoritative and isn't corrupts the fields that are.

## 17 — Where it is, where it's going

- Shipped: publish, subscribe, blogrolls, curated lists, instructed generation.
- Running: two live nodes actually subscribed to each other over the real internet,
  plus one legacy-RSS leg.
- Next, v0.3: threads across clients; Webmention for discovery — reused not invented,
  with structural verification (receiver checks the source actually names the target).
- Then: filter plugins, staleness over the transclusion DAG, local RAG, 1.0 freeze.
- **Say this plainly before asking for involvement:** nothing is stable, and no
  pre-1.0 version will be, including the wire. Building the client is how the protocol
  gets tested; twice last month that changed the spec.

## 18 — If you write

- Be straight: nothing to install yet. Self-host template is 1.0 RC work.
- Useful now: read the two live blygs (real writing, not fixtures) and tell me where
  the fragment/thread split feels wrong.
- **The one question I want answered by someone who isn't me:** does writing with TK
  change *what* you write, or only how fast? Very different findings.

## 19 — If you publish

- You already have the hard part: a domain nobody can take away.
- You're already readable — your feed works from inside this medium, no action needed.
- Mounts anywhere, so adopting it isn't rebuilding a site that works.
- **The ask is the opposite of adoption:** if you'd never run this, tell me why in
  detail. Worth more than another install right now.

## 20 — If you build

- Spec at blygger.org/spec/0.2/ — standalone and complete, no deltas to chase.
- Reference client: MIT, Cloudflare Workers, ~420 tests. Documented CSS contract.
- **The ask, and the last thing they hear:** one implementation isn't a protocol, it's
  a program with a spec next to it. My 1.0 gate is a *second* implementation on a
  different substrate — local-first, folder on a laptop, deploying to a dumb static
  host.
- Undesigned. Unstarted. Highest-leverage thing in the room.

## 21 — Resources

- All on screen, and this deck is a web page — links are there afterwards.
- Two live blygs; spec, notes, namespace on blygger.org; code on GitHub (MIT / CC-BY).
- blygger.com: domain exists, nothing else yet — say so rather than omitting it.
- Thanks.
