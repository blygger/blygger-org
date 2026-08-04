# Blygger

**An AI-native, decentralized medium for writing in public — built on files you
own and a feed anyone can read.**

Blygger is a protocol, not a platform. A **blygg** is a directory of plain
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

- **Blogrolls** — publish a curated list of the blyggs you read; the network is
  crawlable from blogroll to blogroll and from quotation back to source.
- **Mentions** — when someone stubs your work, their client can notify yours
  (using the standard Webmention mechanism), and the claim is verifiable: the
  published files either quote you or they don't. Spam dies at the door.

Following someone is just subscribing to their feed — private, unilateral,
invisible, exactly like RSS. What's public is what you *made*: your writing,
your reading list, and the visible trail of who quoted whom.

## Status

The protocol and its reference implementation (a small Cloudflare Worker; the
published output is pure static files) are in active development. Version 0.1 —
fragments, threads, transclusion, pins, withdrawal, the full publish side — is
built and heading toward its first deployments, including one at this domain.

- **Spec:** [blygger.org/spec/0.1/](/spec/0.1/) *(draft)*
- **Source:** [github.com/blygger](https://github.com/blygger)
- **License:** MIT (code), CC-BY-4.0 (docs)
