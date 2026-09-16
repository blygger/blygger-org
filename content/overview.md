# Blygger

**An AI-native, decentralized medium for writing in public — built on files you
own and a feed anyone can read.**

Social media had one argument about feeds: chronological vs. algorithmic —
two ways of sequencing items that are already finished. Blygger is built on a
different fault line, the one that actually matters for publishing:
**absolute feeds vs. differential feeds.** An absolute feed announces
finished items — it rewards posting something once and moving on, and makes
editing it later look like backpedaling. A differential feed — a
changelog — announces *changes* to items that stay alive after they
publish, which rewards working a hard idea in public instead of declaring it
and walking away. That distinction, not feed ordering, is the design problem
Blygger exists to solve.

The name is a small bet on that idea. **Blyg** is Swedish for *shy* — the
reticence that keeps people from publishing before a thought is finished,
which a changelog-native feed is built to dissolve. **Ygg** nods to
Yggdrasil, the cosmic tree of Norse myth: roots and branches that are never
finished, only ever still growing.

Changelog-driven publishing has never really worked, and the reason is
mundane: nobody wants to read a diff. Git's log gets away with this because
nobody reads it for pleasure — the code is the deliverable, the log is for
tooling. Prose doesn't have that luxury; a changelog that's just a wall of
diffs is where readers stop. Blygger's bet is that AI can close that gap. It
presumes, though it does not require, an AI in the authoring loop whose job
is to take the accumulating versions of a piece and roll them up into
something a reader actually wants to read — not a diff, a digest.

Blygger is a protocol, not a platform. A **blyg** is a directory of plain
files — mounted anywhere on your own domain, conventionally `/blyg/` —
holding your writing, its edit history, and an RSS feed. Anything that can
serve files can host one. Anything that can read RSS can follow one. There is
no company in the middle, no account to create, and no timeline you don't
control.

The design is a deliberate mashup of four ancestors: **blogs** (your domain,
your archive), **Twitter** (short atomic posts), **wikis** (transclusion —
composing big texts out of small ones), and **git** (versions, changelogs, and
an edit culture borrowed from how software treats code).

## Two kinds of writing

- **Fragments** — short, atomic pieces. A thought, a claim, a paragraph.
- **Threads** — long-form pieces *composed out of fragments* by transclusion:
  write `![[fragment-id]]` on its own line and the fragment's content is baked
  into the thread at publish time, with a provenance record of exactly which
  version was included.

Your feed is the changelog: it announces new items *and* new versions of old
ones, newest activity first. Editing in public is a first-class act, not a
guilty correction.

## Publishing the way GitHub treats code

The precedent Blygger leans on is not social media — it's how programmers
publish software:

| GitHub | Blygger |
|---|---|
| Commits and history | Versions and changelogs |
| Tags / commit hashes | **Pins** — irrevocable, citable frozen versions |
| Forking a repo at a commit | Forking an item from a pinned version |
| Vendoring a dependency | Transclusion — a snapshot, with provenance |
| Watching (quiet, private) | Subscribing (client-local, invisible) |
| No comment box on the code | **No replies. Ever.** |

That last row is the point. Blygger is **a network of soapboxes, not a
conversation medium**. There is no reply primitive in the protocol and there
never will be. The only way to respond to someone is to *publish*: quote their
fragment into a thread of your own, with your editorial framing around it (we
call this **stubbing**), or fork a pinned version and take it somewhere new.
Responding costs the same thing publishing costs — putting your name on a
thing you made. Conversation is what other media are for; blygger posts
cross-post anywhere.

## Mutable by default, immutable by choice

Two deliberate inversions of the usual defaults:

- **Your history is yours.** Readers see the latest version of each item plus a
  changelog — dates and edit notes, not diffs. Old content stays private unless
  you decide otherwise.
- **A pin is a promise.** Pinning a version says: *this exact text stays
  fetchable at this URL forever* — surviving all later edits, even withdrawal.
  Pins are what make citation safe in a medium where everything else can move.

And one honest rule about leaving: there is no delete for published work, only
**withdrawal** — a permanent, reversible endcap that tells conforming readers
to drop the item. The protocol doesn't pretend the internet forgets; it just
makes your intent machine-readable, and keeps your promises (pins) even when
you change your mind about everything else.

## AI-native, AI-free wire

Blygger assumes writers work with AI — and keeps AI entirely out of the
protocol. The flagship mechanism is **TK-transclusion**: wrap transcluded
fragments in a `[TK]…[/TK]` scope and your own model, with your own key,
generates the connective text that contextualizes them — at authoring time, in
your private studio, under your editing hand. What gets published is ordinary
markdown and HTML plus provenance. Readers need no models, no keys, and can't
even tell from the wire which parts you typed.

The same boundary holds for identity: the protocol authenticates exactly one
thing — the domain publishing the feed. Bylines are assertions a publication
makes, like a masthead, not accounts in a system. **DNS is the namespace.**

## Finding each other

No follower counts, no follow requests, no social graph in the protocol.
Discovery is deliberately old-school, with two optional surfaces:

- **Blogrolls** — publish a curated list of the blygs you read; the network is
  crawlable from blogroll to blogroll and from quotation back to source.
- **Mentions** — when someone stubs your work, their client can notify yours
  (using the standard Webmention mechanism), and the claim is verifiable: the
  published files either quote you or they don't. Spam dies at the door.

Following someone is just subscribing to their feed — private, unilateral,
invisible, exactly like RSS. What's public is what you *made*: your writing,
your reading list, and the visible trail of who quoted whom.

## Getting started

**[Build a blyg](/start/)** — three ways in: publish a feed you already have,
host the reference client on Cloudflare, or build your own client from the spec.
A directory of existing blygs lives at [blygger.com](https://blygger.com).

## A talk about all this

**[Blygger: an AI-native medium made of static files](/talks/2026-09-24-blygger/)**
— Protocol Symposium 2026, Thursday 24 September, 23:00 UTC. The slides, plus the
speaker's cues, published before delivery.

## Status

The protocol and its reference implementation (a small Cloudflare Worker; the
published output is pure static files) are in active development, and two live
nodes have been running and subscribed to each other since August 2026:
[venkateshrao.com/blyg/](https://venkateshrao.com/blyg/) and
[blyg.protocol-institute.org](https://blyg.protocol-institute.org). *(This domain
is the protocol's namespace and documentation host — it does not run a blyg.)*

Version 0.1 — fragments, threads, transclusion, pins, withdrawal, the whole
publish side — shipped first. **Version 0.2 is the current document**: it adds the
subscribe side (resolution, importers, blogrolls, curated lists) and the wire
members for instructed generation. Next is 0.3 — threads across clients, and
Webmention for discovery.

**No version before 1.0 will be declared stable, including the wire format.**
Building the reference client is how the protocol gets tested, so the spec changes
when building finds something. Read and implement freely; don't build on it
expecting promises yet.

- **Spec:** [blygger.org/spec/0.2/](/spec/0.2/) *(draft — the living document)*
- **Technical notes:** [blygger.org/notes/](/notes/)
- **Source:** [github.com/blygger](https://github.com/blygger)
- **License:** MIT (code), CC-BY-4.0 (docs)
