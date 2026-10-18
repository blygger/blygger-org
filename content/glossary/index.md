# Glossary

The terms used across Blygger's spec, its tools and the people writing with
them. Section numbers (§) point into the [living specification]({{SPEC_LINK}}),
which is the authority wherever this page and the spec differ. Terms marked
*client* belong to particular clients, mostly the reference client
[Blygger Studio](https://github.com/blygger/blygger-studio), and are not part
of the protocol. Terms marked *community* are in common use but defined
nowhere normative.

## Places and files

**Blyg**
: A directory of static files on a publisher's own domain holding versioned
  items, a manifest, an archive index and an RSS feed. Anything that can serve
  files can serve one; anything that can read RSS can follow one. Swedish for
  *shy*, and nearly a homophone of *blog*.

**Origin**
: A blyg's base URL, such as `https://example.com/blyg/`. The unit of
  identity, trust and subscription: the only thing the protocol authenticates
  is the publisher at its origin. A blyg may mount at a domain root, under any
  path or on a subdomain (§2, §4).

**Mount**
: Where a blyg sits on its domain. Conventionally `/blyg/`, never required.

**Manifest**
: `blyg.json`, the file that says a URL is a blyg: its title, protocol
  version, client, and where its other files are (§6.1). From 0.4 it may name
  non-default paths through **surface templates**, so software that cannot
  serve fixed `.json` paths, such as WordPress, can still publish.

**Archive index**
: `items/index.json`, the list of every item the blyg has published with its
  latest version. The source of truth a reader reconciles against (§6.2).

**Item document**
: `items/{id}.json`, one item's latest content and metadata: its kind,
  version, changelog, references, and both `content_md` and a self-contained
  `content_html` (§5).

**Feed**
: `feed.xml`, a valid RSS 2.0 feed of publish events, newest first. It
  announces new items *and* new versions of old ones, so the feed is the
  changelog (§7).

**State plane / notification plane**
: The two halves of the wire. Item documents and the archive index are the
  **state plane**: complete and authoritative. The feed is the
  **notification plane**: a lossy, windowed signal that something changed.
  Readers rebuild state from the first and only take hints from the second
  (§1, §13).

**Page**
: An item's human-readable permalink, named by the item document itself
  (§5.8). Also, more broadly, the published side of the studio/page split.

**Studio / page split**
: The protocol governs only the published artifact, the *page*. How a
  publisher writes, edits, imports or generates content, the *studio*, is out
  of scope, and so is how any tool writes into a blyg (§1).

## Items and versions

**Item**
: The unit of publication: a permanent 26-character id plus a version
  history. Its kind is `fragment`, `thread` or `withdrawn` (§5).

**Fragment**
: A short item, about the size of a microblog post: a thought, a claim, a
  paragraph.

**Thread**
: A long item that can be composed of other items by transclusion (§10).

**Version**
: One published state of an item, numbered from 1. Every publish is the next
  number; drafts are invisible. The number is deliberately bare, with no
  semantic versioning or edition markers (§5.2).

**Rollup**
: How versions are presented: readers get the latest version's content plus
  a changelog of dates and notes, never diffs. Older content stays private
  unless pinned (§5.2).

**Changelog note**
: The optional description of a version's change. It describes; it never
  reproduces text that isn't public (§5.2).

**Pin**
: An irrevocable promise to serve one exact version forever at
  `items/{id}/v{n}.json`, surviving later edits and even withdrawal. The
  protocol's only marker of "this version matters", and what makes citation
  safe in a medium where everything else can change (§8).

**Withdrawal**
: The only way out for a published item: a final version with no content
  that tells conforming readers to drop their copies. There is no delete. A
  withdrawal can itself be reversed by publishing again, and pins outlive it
  (§9).

**Watermark**
: The highest version a reader has seen for an item it imported. It only
  rises; a lower version showing up is surfaced as a suspected history
  rewrite, never silently applied (§13.3).

## Quoting, linking and responding

**Transclusion**
: Quoting by reference. The line `![[id]]` in a thread bakes a snapshot of
  that item's content into the thread at publish time, with a record of
  exactly which version from which origin. Later edits to the source never
  rewrite the quote. Ted Nelson's word (§10).

**Partial transclusion**
: A transclusion followed directly by a blockquote: only that passage is
  baked, after a check that it really is in the source (§10.1–§10.2).

**Plain link**
: `[[id]]` anywhere in text: an ordinary link to an item's page. Unlike
  every other citation it notifies nobody, deliberately (§10.1).

**Label**
: Optional text after the id, `[[id | text]]` or `![[id | text]]`. On a link
  it is the link text; on a transclusion it is a note for the author.
  Resolution ignores it. New in 0.4 (§10.1).

**Reference**
: The citation shape `{ origin, id, version }`, naming one published version
  of one item at one origin. Used for transclusions, stubs, lineage and
  generation sources (§5.9).

**Stub**
: A thread that declares itself a response to exactly one target, through
  `stub_of`: another blyg's item or any URL. The medium's way to reply, since
  there is no reply primitive (§10.6).

**Fork / lineage**
: An item that began as a copy of a pinned version of another item says so
  with `forked_from`. Lineage is fixed when the fork is made and survives
  withdrawal (§5.6).

**Mention**
: A Webmention: a ping from one page to another saying "this cites you". A
  **verified mention** is one whose source item document structurally names
  the target, which the receiver checks by fetching it. Quotes, stubs, forks
  and generation sources send them; plain links do not (§15).

## Generation

**Generation provenance**
: The `generated` array on an item: which spans of a version a model wrote,
  and, from 0.4, from which **sources**. It is the publisher's own
  disclosure, unverified, and the only trace generation leaves on the wire.
  The instruction never travels (§5.7).

**Source**
: An item a generator was given to work from. From 0.4 it is disclosed as a
  reference and notifies its origin like a quote does, so paraphrase by model
  is never a silent way to use someone's words (§5.7, §15).

**TK scope** *(client)*
: In Blygger Studio and some other clients, `[TK]an instruction[/TK]` marks a
  gap for a model to fill at authoring time, inside the editor. After the
  copy-desk mark for "to come". What publishes is the output plus provenance.

**`impyrt`** *(client)*
: Blygger Studio's way to mark text written by a model somewhere else, so it
  publishes disclosed as generated: `[TK]impyrt=the pasted text[/TK]`.

## Reading and discovery

**Resolution**
: The procedure that turns any URL a reader is given into a subscription: a
  blyg origin, or a plain feed (§12).

**Subscription**
: A reader's private relationship to one blyg or feed. Invisible to the
  publisher: there is no follow object and no follower list (§12.2).

**Blogroll**
: An optional published OPML list of the subscriptions a publisher chooses
  to show. The outbound, curated half of the public graph; verified mentions
  are the inbound half (§11).

**L0 wrapper**
: How a reader treats a plain RSS feed: as summary items with links. Any RSS
  feed can be followed from a blyg (§13.6).

**Hopper** *(client)*
: A Blygger Studio collection: items from your own blyg and your
  subscriptions gathered by hand, private or published as a page.

**Pace-layered order** *(client)*
: Blygger Studio's optional home-page order, the "diachronic view": items sink
  as new ones arrive, and pins and pinned quotes slow the sinking. Computed
  from public data only, so any client can reproduce it.

## Conformance and process

**Conformance levels**
: L0 is any plain RSS feed; L1 is a single blyg with versions, pins,
  withdrawal and same-origin threads; L2 adds everything across origins:
  transclusion, stubs, lineage, mentions, generation sources, surface
  templates; L3 is reserved for encrypted content. Levels are strict
  supersets, and readers ignore what they don't understand (§3).

**Generator**
: The manifest key naming the client that published a blyg, such as
  `blygger-studio/0.46.3`. Because the manifest is public, every client
  announces itself, and the [ecosystem index](/ecosystem/) is built from a
  census of these strings (§3.2).

**Living document**
: The highest-numbered spec version, where revisions land. Lower versions are
  frozen as *superseded* and stay citable, with dated snapshots. No version
  before 1.0 is declared stable.

**Technical note**
: A non-normative document about practice the spec deliberately leaves out,
  such as identity or a write surface. At [blygger.org/notes/](/notes/).

**RFC**
: A proposed convention published on the official blyg,
  [blyg.blygger.org](https://blyg.blygger.org/), with a comment period, before
  any client adopts it.

**Reference client**
: [Blygger Studio](https://github.com/blygger/blygger-studio), the MIT-licensed
  client on Cloudflare Workers that the spec is tested against. One client
  among many, not the definition of the protocol.

## Community

**Thicket** *(community)*
: The network of blygs, and of the quotes, pins, forks and mentions between
  them. Formerly the *blygosphere*; from Aneesh Sathe. See [The
  Thicket](/thicket/).

**Blygger**
: The protocol and the project. A *blygger* is someone who writes in a blyg;
  *to blyg* is to publish in one.

**Bespoke build** *(community)*
: A blyg published by its owner's own generator, written from the spec for
  one site, often with an AI assistant. Listed as a category on the
  [ecosystem index](/ecosystem/).
