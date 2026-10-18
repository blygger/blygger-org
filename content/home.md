# Blygger

<!-- SCAFFOLD (session 49, 2026-10-17). The tabbed front page that will replace
overview.md. Built only with `build.py --new-home`; a plain build and deploy.sh
still publish overview.md. Every section below is a placeholder: the italic
line says what it is for. Copy is written after the raw-materials review
(drafts/front-page/raw-materials.md) settles a rhetorical strategy.
Link every use of "thicket" to /thicket/. -->

*Placeholder lede, one or two sentences, read by both audiences before the
tabs: what Blygger is, in a line.*

<div class="tabset" markdown="1">

<section class="tab-panel" data-tab="publishers" data-label="For Publishers" markdown="1">

## What a blyg is

*Placeholder. For people who write online and might set up a site with an
existing tool but won't customise much. Plain-language picture of a blyg and
of the [thicket](/thicket/) it joins.*

## Where this comes from

*Placeholder. Blygger in the history of online media: homepages, blogs and
RSS, the platform era, and what was lost and kept along the way.*

## What's different here

*Placeholder. What writing in a blyg is like, in the words of people doing it:
small pieces with addresses, quoting by reference, editing in public, no
replies, AI with disclosure.*

## Start a blyg

*Placeholder. The easiest routes in, from the [ecosystem](/ecosystem/) and
[Build a blyg](/start/), with no code assumed. Then [blygger.com](https://blygger.com)
to find blygs to read.*

</section>

<section class="tab-panel" data-tab="developers" data-label="For Developers" markdown="1">

Blygger is a protocol for public writing built on static files and RSS. This is
a compact technical introduction: the core idea, the design principles behind
it, what the spec deliberately leaves to clients, and where to start building.
Terms in bold are defined in the [glossary](/glossary/).

## Versions and chronology together

Media keep time in two ways. Some are about the present moment, like a social
feed, where everything is now and nothing is revised. Others are about change,
like a git log or a book's editions, where the record of the changing is the
point. Blygger tries to do both in one medium.

A **blyg** is a directory of files at an **origin**, a base URL on the
publisher's own domain such as `https://example.com/blyg/`. It publishes
**items**: short **fragments** and long **threads**, each with a permanent
26-character id and a numbered **version** history. Publishing an edit makes
the next version. The **item document** (`items/{id}.json`) carries the latest
content and a changelog of dates and notes, never diffs, so the history is
visible without the old text being public.

The feed is where the two kinds of time meet. `feed.xml` announces publish
events, newest first: new items *and* new versions of old ones. A follower sees
a live stream; the same stream is each item's changelog. The version counter is
deliberately bare. Significance is expressed by a **pin** instead: an
irrevocable promise to serve one exact version forever at
`items/{id}/v{n}.json`. A pin is what makes it safe to cite something that can
still change, the way a book's edition can be cited while the author keeps
writing.

## Quoting by reference

A thread quotes another item with a line of its own, `![[id]]`. At publish
time the publisher bakes a snapshot of the source into the thread's HTML and
records a **reference**, `{ origin, id, version }`, naming exactly what it
quoted. This is **transclusion**, Ted Nelson's word for it. The source can be
a fragment or a thread, the publisher's own or from any blyg it reads, quoted
whole or as a **partial transclusion** of one passage. The quote is always the
publisher's local snapshot, never a live fetch, so a later edit or
**withdrawal** of the source never rewrites it.

Responding works the same way, because there is no reply primitive. A **stub**
is a thread that declares itself a response to exactly one target with
`stub_of`. A **fork** starts from a pinned version of someone else's item and
records its lineage with `forked_from`. Quotes, stubs, forks and generation
sources each send a **mention**, a Webmention that the receiver verifies by
fetching the sender's item document and checking that it really names the
target. A plain inline link, `[[id]]` (with an optional **label**, `[[id |
text]]`, from 0.4), is the one citation that notifies nobody. The network of
blygs connected this way is the [thicket](/thicket/).

## Generation, inline and disclosed

Blygger assumes writers work with models and keeps models out of the wire.
Generation happens in the client, at authoring time: in the reference client a
`[TK]an instruction[/TK]` scope marks a gap for the publisher's own model to
fill, and other clients do it their own way. What publishes is ordinary text
plus **generation provenance**: a `generated` array in the item document
saying which spans a model wrote, and a `blyg-tk-gen` class on those spans in
the HTML. The instruction never travels. From 0.4, an item a generator drew on
is disclosed as a **source** and notifies its origin, so a model's paraphrase
is never a silent way to use someone's words.

Disclosure is the publisher's own claim, unverified, like a byline. Readers
need no models and no keys. A blyg written or run entirely by an agent is a
blyg like any other; the protocol neither can nor tries to tell.

## Design principles

**A static file contract.** The protocol governs only the published files. A
blyg can be served from any static host, exported as plain files, and mounted
at a domain root, a path or a subdomain. Item documents and the archive index
(`items/index.json`) are the state of record; the feed is only a signal that
something changed. Readers reconcile against the index, so a missed or
malformed feed entry costs a slower sync, never lost data.

**RSS as the floor.** Every blyg feed is a valid RSS 2.0 feed whose entries
carry self-contained HTML, so any feed reader sees a sensible microblog and a
reader that knows nothing of Blygger loses nothing. Going the other way, any
plain RSS feed can be followed from a blyg as summary items.

**Backward compatibility by design.** Conformance levels are strict supersets:
**L0** is any RSS feed, **L1** a single blyg with versions, pins, withdrawal
and its own threads, **L2** everything across origins. Readers ignore
constructs they don't understand instead of rejecting the document, which lets
levels and versions advance without breaking anyone: a valid 0.3 document is a
valid 0.4 document unchanged. Nothing is promised before 1.0, but a breaking
change bumps the version and is recorded.

**Existing standards for the network.** Notification is
[Webmention](https://www.w3.org/TR/webmention/), a W3C recommendation, with one
addition: a mention counts only if the source's published files structurally
name the target. It is optional at every level, and a static-only blyg simply
advertises no endpoint. Subscriptions are private and unilateral, as in RSS.
The only public graph is what publishers choose to show: a **blogroll** in
OPML going out, and verified mentions coming in.

**DNS is the namespace.** The one authenticated party is the publisher at its
origin. There are no accounts and no central registry.

**Refusals, on purpose.** Anything the protocol can't verify, it declines to
represent. There will be no reply primitive, follower graph, addressable
author, metrics of any kind, title field or version-significance markup. The
spec lists them in §16.8, and the [technical notes](/notes/) give the
reasons.

## What the spec leaves open

The spec draws a line between the published files and everything a client
does with them, and keeps a long list of decisions on the client's side of it.

**Presentation.** How items, threads, quotes, stubs and forks look is up to
the client. The spec fixes the routes and the promises (a pinned version stays
fetchable), not the page. Ordering a reader's merged feed is the reader's own
policy, since remote timestamps are self-asserted. The few presentation rules
that do exist protect disclosure: three CSS classes are baked into published
HTML, for whole quotes, partial quotes and generated spans, and a theme may
style them freely but may not make them invisible or rewrite them (the [CSS
contract](https://github.com/blygger/blygger-spec/blob/main/docs/css-contract.md)).
Themes, home-page orders, static front pages and reading views are all client
territory.

**Identity.** Beyond the origin, the protocol says nothing about who anyone
is. The optional per-item `author` field is an opaque, unverified assertion,
like a masthead: a feed has one publisher but may have many authors. How to
show that a person is who they say has been left to practice, not protocol:
the current recommendation is that a person is a URL they control, proven by a
reciprocal `rel="me"` link or a signature over an item's content hash. That
practice belongs in non-normative technical notes and RFCs, so it can evolve
without a protocol version: a note on groups is published, and one on
identity is next on the roadmap.

**How to write into a blyg.** There is no normative write API, at this version
or any foreseen one. Clients publish however they like; the reference client
happens to offer a REST API, OAuth-style tokens and an MCP server, which other
tools and agents use.

**Which models, if any.** The spec defines how generated text is disclosed,
not whether, how or with what it is generated.

**Discovery and ranking.** The protocol supplies blogrolls and verified
mentions and nothing global. Directories, search and explorers are services
built on top: [blygger.com](https://blygger.com) is one.

## Resources and good practice

- **The [specification]({{SPEC_LINK}}).** Implement the living document, the
  highest-numbered version. Pin a dated snapshot when you need the text to
  hold still, and say which one you built against. Don't build from plan
  documents or from a client's source: when the reference client and the spec
  disagree, the client has a bug. [Build a blyg](/start/#which-text-to-build-against)
  says more.
- **The [glossary](/glossary/)** and the [technical notes](/notes/), which
  record why things were decided, including the designs that were rejected.
- **[Blygger Studio](https://github.com/blygger/blygger-studio)**, the
  MIT-licensed reference client on Cloudflare Workers, with its test suite, a
  documented API and SDK, and an extension mechanism. One client among many.
- **A conformance toolkit**, in review as
  [blygger-spec#11](https://github.com/blygger/blygger-spec/pull/11), so that
  "conformant" means something anyone can check.
- **The official blyg, [blyg.blygger.org](https://blyg.blygger.org/)**, which
  carries release notes and RFCs. Proposed conventions are published there
  with a comment period before any client adopts them; comment by stubbing.
- **Issues and proposals** go to the repository they concern, under
  [github.com/blygger](https://github.com/blygger); the issue templates say
  which.

A few habits that have saved implementers trouble:

- Name your client in the manifest's `generator` key, and point
  `generator_url` at its source if it has one. The ecosystem census reads
  them.
- Don't ship a default title shared by every installation; derive it from the
  deployment's own host ([why](/start/#advisory-do-not-ship-a-generic-default-title)).
- Ignore what you don't understand, and carry `content_html` verbatim when you
  store or re-emit someone else's item.
- Send a mention for every remote reference you publish; if you receive
  mentions, verify them structurally and rate-limit the endpoint, since it is
  the one place a stranger can make your server fetch a URL.
- Poll politely, and let the archive index heal what the feed misses.

## Where to start

The [ecosystem index](/ecosystem/) lists every known client, integration,
authoring tool and bespoke build, with the live blygs each one serves: read a
few before writing your own, and add yours when it publishes. The
[roadmap](/roadmap/) is the one list of what is being worked on across the
spec, the reference client, blygger.org and blygger.com, with an issue behind
each row to pick up or argue with. And [blygger.com](https://blygger.com) lists
the blygs in the thicket, which is where to test against real feeds.

</section>

</div>
