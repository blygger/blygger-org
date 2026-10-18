# Blygger

**Blygger is a decentralized social publishing and conversation protocol that
cleanly synthesizes key features of blogs, microblogs, wikis and graph-like
notebooks, in an AI-native, agent-friendly way.** Its core organizing principle
is to braid two kinds of time together seamlessly: chronological feed time and
version-history time (synchronic and diachronic).

Blygger is designed to be highly backward compatible with existing protocols
like RSS and [Webmention](https://www.w3.org/TR/webmention/), and supports many
familiar patterns of use while also enabling radical new ones. Your writing
lives on your own domain, readable by traditional RSS feed readers, but with
clients designed for Blygger, much richer interactions and conversations become
possible. The sites that write this way are called **blygs**, and the broader
web of quotes and replies that emerges among them makes up what was first
called the blygosphere, and is now called the [thicket](/thicket/). There is a
growing [ecosystem](/ecosystem/) of clients and tools, and a growing number of
[active blygs](https://blygger.com). Read either the
[publishers](#publishers) or [developers](#developers) introduction below to
get started.

<div class="tabset" markdown="1">

<section class="tab-panel" data-tab="publishers" data-label="For Publishers" markdown="1">

## What people make with a blyg

A **blyg** is a website, or a corner of one, where every post keeps its
history. You can edit in public, freeze any version for good, and quote other
people's posts in a way that stays accurate however they change later.

*Blyg* is Swedish for *shy*, and one vowel from *blog*. *Blygger* tips its hat
to Blogger, one of the first blogging tools, and its *ygg* nods to Yggdrasil,
the Norse world tree, never finished, always still growing. Writing on a blyg
is *blygging*, and someone who does it is a *blygger*.

The format turns out to suit more kinds of writing than a blog does:

- **A plain blog.** You post, you move on, and you rarely go back. Nothing about
  Blygger gets in the way: anyone with a feed reader can follow it.
- **A book written in the open.** Chapters and sections are posts of their own,
  revised as you go, and the book is a long post that quotes them in order. Each
  time you finish a draft you freeze it as an edition, and readers can cite
  edition two while you work on three.
- **A constitution, a policy or a contract.** Text that changes rarely, where
  every version that ever took effect is frozen and stays readable at its own
  address, so nobody can argue about what it said.
- **A shopping list or a packing list** that you edit all the time, with the
  versions worth keeping frozen as variants: Thanksgiving, the camping trip,
  the week the in-laws visit.
- **A notebook**, Roam- or Obsidian-style: lots of short notes, revised often,
  linking and quoting one another, with a few frozen when they settle.
- **A draft in public**: an essay or a manifesto you keep developing, freezing
  its stages so readers can see how it grew.
- **A game or a challenge**: someone posts an aphorism and freezes it; others
  copy it into their own blygs, change it and freeze their versions, and the
  copies record where they came from.

## Two dials: how often you revise, how much you freeze

Those uses differ along two dials. One is how often a post changes after you
publish it. The other is how many of its versions you **pin**, that is,
promise to keep online exactly as they were, forever.

| | **Few pins** | **Many pins** |
|---|---|---|
| **Few versions** | **The plain blog.** Publish once, move on. | **The document of record.** Stable text, every state on record: a constitution, a contract, a policy. |
| **Many versions** | **The living document.** Always current, with a dated log of changes: a notebook, an evergreen page. | **The portfolio of variants.** Every state worth keeping is kept: a book's editions, a list's variants, a designer's drafts. |

You don't have to choose once. Each post sits wherever you put it, and most
blygs have some of each.

## The ideas, in plain terms

**Two kinds of time.** Some media are about now: a social feed, where
everything is current and nothing is revised. Others are about change: a
book's editions, a project's history, where the record of the changing is the
point. Blygger tries to do both. Your feed shows what's new, including new
versions of old posts, and each post carries its own history.

**Versions.** Editing a published post makes a new version. Readers see the
latest one, plus a short log of when it changed and why. Older versions stay
private unless you pin them.

**Pins.** Pinning a version is a promise to keep that exact text online at its
own address for good, even if you edit or withdraw the post later. Pins are
editions: they're what makes it safe for someone to cite writing that's still
changing.

**Fragments and threads.** A fragment is a short post: a thought, a claim, a
paragraph. A thread is a longer one, and threads can be built out of other
posts.

**Quoting by reference.** Instead of copying someone's words, you name their
post, and a snapshot of it is built into yours, with a record of exactly which
version you quoted and where it came from. If they edit later, your quote
still shows what you responded to. You can quote a whole post or one passage.
The technical name is **transclusion**.

**Forks.** You can start a new post from a pinned version of someone else's,
and change it into your own. The fork keeps a permanent note of where it came
from.

**Stubs.** A stub is a post that says "this is a response to that one". More
on stubs below, because they're how conversation works here.

**Withdrawing.** Nothing published is deleted, but you can withdraw a post,
which tells other blygs to drop their copies. Pins stay up, because a pin is a
promise.

**Links and blogrolls.** You can also simply link to a post, which notifies
nobody. And you can publish a blogroll, a list of the blygs and feeds you read.

## Feeds: what you show and what you read

A blyg has two feeds, and you control both.

**The feed you publish** is your blyg's front page and its RSS feed. The RSS
feed is always newest first, because that's what feed readers expect. Your
front page can show either of two orders:

- **Chronological**, newest first: the familiar blog and timeline view, about
  what's happening now.
- **Pace-layered**, the view about what lasts. Every post sinks as new ones
  arrive, but at different speeds. Pinning a post, or having it quoted in
  pinned posts, moves it into a slower layer; there are six, named after
  Stewart Brand's pace layers from *fashion* down to *nature*. Revising a post
  lifts it one place. A post you keep pinning and revising holds the top, so a
  "pinned post" is something your blyg arrives at rather than a setting you
  flip.

Pace-layering is the project's recommended order for every client, being
written up as an RFC so other clients can match it, and it works from public
files alone, so a reader's client can show anyone's blyg this way. Blygger
Studio uses it on new blygs' front pages, with chronological a setting away.

**The feed you read** is equally yours. You choose what to subscribe to, from
blygs or any ordinary RSS feed, privately; you can gather posts into
collections by hand, browse other people's blogrolls, and order your reading
however your client allows. There is no central timeline and no algorithm you
didn't choose. Full clients such as Blygger Studio put the reader and the
editor side by side, because in the thicket they're one activity: you read,
quote, answer and get answered, and **thicketing** is that call and response.
You can also be as solitary as you like. A blyg nobody quotes is still a
perfectly good notebook, and reading without ever publishing is fine too.

## Why bother: the thicket

All of this is more involved than a blog, and it's fair to ask what the
complexity buys. The answer is the **[thicket](/thicket/)**: the network of
blygs, and of the quotes, pins, forks and replies that run between them. The
name comes from Aneesh Sathe, who set the thicket's undergrowth against the
platform's manicured garden.

The platforms bundled everything: your identity, your archive, your audience,
the conversation and the algorithm deciding who sees what. Leaving meant losing
all of it. A blyg unbundles them. Your writing lives in files on your own
domain. Your history is yours. And the connections between writers don't live
on anyone's server: they're written into the posts themselves, as quotes and
responses that point at exact versions, and any reader can follow them from
one blyg to the next.

That makes for a different kind of place:

- **No public feed.** There's no central timeline and no algorithm. Each reader
  follows the blygs they choose, privately, the way RSS has always worked, and
  nobody sees who follows whom.
- **Tangles, not streams.** Ideas grow by being quoted, answered, forked and
  quoted again, across sites. A short post can turn up in a dozen longer ones,
  each quoting the version it saw, and the trail back to it stays intact.
- **Feeds you curate yourself**, in what you read and in what you show
  ([above](#feeds-what-you-show-and-what-you-read)). Clients are starting to
  add personal ranking, which answers to you, not to an advertiser.
- **No counts.** No likes, follower numbers or view counts. Several blyggers
  describe this as the point: you write for the work, not the metrics.

The thicket is slower to walk than a feed, and that's part of what keeps it
healthy: there's no aggregate for anyone to farm.

## Responding without replies

There is no reply button in the protocol, and there won't be one. There is
one response act, the **stub**: a post of your own that says "this responds to
that". It notifies the other writer, and they can check it's real, because
their blyg reads your post and confirms it names theirs.

A stub is like a stem cell: one act that can grow into the familiar shapes,
depending on where you put your words and how much you quote.

- Your words **above** a quote of their whole post: a *quote post*.
- Your words **below** it: a *reply*.
- Your words around **one passage** of theirs: *commentary*, or an *inline
  reply*.
- A quote with **no words** of your own: a *repost*.
- Stubs of stubs: a **conversation**, carried across everyone's sites, each
  turn on the blyg of the person who said it.

Clients choose which of these shapes to put first. Blygger Studio has a single
"stub" action that opens with the quote ready; Burrow calls the same act
"Reply" and shows each post's lineage as a small glyph. Under every one of
those is the same stub.

**To take part, you publish.** Anyone can read the thicket without a blyg: any
feed reader can follow one, and every post is a public page. But the only way
to join in socially is to publish a post of your own. There's no second tier of
users who only comment.

That doesn't rule out comments sections; it changes what they are. A writer
can show the stubs their posts received underneath them, curated like any
comments section. And a site that wants to host comments from people without a
blyg can do it too: each comment is published as a real post, under the
commenter's name, on a blyg the site runs for the purpose, with the site taking
responsibility for what it hosts. To every other blyg, those comments are posts
like any other. Comments become a feature a publisher chooses to build, not a
lower class of participant built into the protocol. The approach is
[RFC-2](https://blyg.blygger.org/t/2mzqh4jt3ye14xm6sr5gf32cah/), open for
comment until 4 November 2026.

**Mentions, and why the protocol stays out of identity.** On a platform, an
@-mention is one company's account system pointing at another account in the
same system. Blygger has no account system to point into. The only thing it
authenticates is a blyg's own domain, and the people writing on blygs already
have identities elsewhere: their own website, a fediverse account, a Bluesky
handle, an Ethereum address. Rather than pick one, the protocol stays agnostic
and lets them all ride along.

The convention being proposed works like this. Your client keeps an address
book; you type a short `@name`, and the published post carries an ordinary link
to the person plus, in standard markup, the identifiers you know for them in
each of those systems. A reader whose client speaks some of those systems can
recognise the person, show them under the reader's own name for them, or open
their profile where they actually live. A client that speaks none of them shows
an ordinary link and loses nothing. Nobody has to adopt anyone else's identity
system for mentions to work between the clients that share one.

A mention doesn't notify anyone, though. In Blygger, notification is reserved
for citation: quoting someone, stubbing them, forking them or drawing on their
post when generating text sends their blyg a notice, which it checks against
your published post before accepting. Naming someone, like linking to them,
asserts nothing about their work that could be checked, so it sends nothing.
Attention arrives only as a citation, from someone who put their own name to a
post, so there's nothing to pile on with. The mention convention is
[RFC-1](https://blyg.blygger.org/t/7eeh3bfzfcnhh90d5pkvkc2r1n/), open for
comment on the official blyg until 4 November 2026.

## AI, with disclosure, and agents as co-authors

Blygger assumes you might write with AI, and it keeps the reader's side free of
it: readers need no model and no account anywhere. The ways it's hooked in so
far:

- **Fill-in-the-blank drafting.** In the editor, mark a gap with an
  instruction, `[TK]summarise the three quotes above[/TK]`, and your own model,
  with your own key, writes that passage. TK is the old copy-desk mark for "to
  come". The generated words are published marked as generated, and readers
  can see which ones they are.
- **Drawing on other people's posts.** When a model works from another
  writer's post, the post is listed as a source and its writer is notified,
  just as with a quote. A model's paraphrase is never a silent way to use
  someone's words.
- **Text written elsewhere.** Words you got from a chatbot somewhere else can be
  pasted in and marked, so they publish disclosed too.
- **Help around the edges.** Clients use models for chores like writing the
  note that describes an edit, which is also marked, and for ranking your
  reading, which is coming.

Disclosure is the writer's own statement, like a byline: nobody can verify it,
and the protocol doesn't pretend to.

**Agents.** The protocol never asks whether a person or a program wrote
something. An agent can run its own blyg, publish under its own name inside
yours, or work as a tool you've given access to: Blygger Studio lets other
apps and agents write into your blyg with permissions you grant and can
revoke. What matters is the same for everyone: a stub should be a real
response, not a machine re-posting a feed. Bylines for several authors on one
blyg, people or agents, are being worked out in public as an open proposal.

The [For Developers](#developers) tab explains the mechanics.

## Get started

**Starting from nothing.**

- **[Blygger Studio](https://github.com/blygger/blygger-studio)** is the
  reference client: a full blyg, with an editor, a reader and your settings,
  running on your own Cloudflare account and domain. A setup walk-through
  greets a fresh install. [Build a blyg](/start/) has the steps; an AI
  assistant can take you through them.
- Once it's running, write from wherever suits you:
  [Burrow](https://github.com/aneeshsathe/blygger-desktop), a fast desktop app
  for Mac and Windows; [drafts-blyg](https://github.com/miguelito4/drafts-blyg)
  for quick posts from your phone; or [blyxt](https://github.com/rpasetes/blyxt),
  from a Telegram group.
- **[Blynger](https://github.com/BradyDale/Blynger)** is a Mac app that runs a
  whole static personal website with a blyg built in.
- Or build your own. Several blyggers had an AI assistant write theirs straight
  from the [spec]({{SPEC_LINK}}), some without having written software before.

**Starting from something you already have.**

- **WordPress:** [Soapbox for Blygger](https://wordpress.org/plugins/soapbox-for-blygger/),
  a plugin in the WordPress.org directory, publishes your posts as a blyg.
- **Obsidian:** [blyg-publisher](https://github.com/brndnpink/blyg-publisher)
  publishes a folder of your vault.
- **Hugo:** [hugo-blyg](https://github.com/chrisbodhi/hugo-blyg). **Logseq-style
  gardens:** [goddinpotty](https://github.com/mtravers/goddinpotty).
- **Any blog with an RSS feed** can already be followed from a blyg, so
  blyggers can read you before you set anything up.

The [ecosystem index](/ecosystem/) lists every client, plugin, tool,
extension and modified Studio, with the blygs each one runs. When your blyg is
up, submit it to [blygger.com](https://blygger.com), where you'll also find the
rest of the thicket to read.

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
identity is next on the roadmap. The same agnosticism shapes @-mentions:
[RFC-1](https://blyg.blygger.org/t/7eeh3bfzfcnhh90d5pkvkc2r1n/), open for
comment, proposes that a mention carry the person's identifiers from whatever
systems they use (an `https` URL, a fediverse `acct:`, a `did:` for ATProto or
an Ethereum account) inside an ordinary link marked up as an h-card. Clients that
share a scheme resolve the person; the rest render a link. Mentions add nothing
to the wire beyond that HTML and notify nobody.

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
