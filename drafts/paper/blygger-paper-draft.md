---
title: "Blygger: A New Publishing Medium"
author: "Venkatesh Rao"
date: "Draft, 19 October 2026"
---

*Rough draft. Synthesized from the Protocol Symposium 2026 talk (24 September 2026) and the publisher and developer introductions on blygger.org. Figures, references and current-state claims need checking before circulation.*

# Abstract

Blygger is a decentralized protocol for public writing, built on static files and RSS, that tries to do something most media have avoided: hold two kinds of time in one place. Social feeds live in *synchronic* time, where everything is now and nothing is revised. Version-controlled documents live in *diachronic* time, where the record of change is the point. Each kind of medium handles the other kind of time badly. Blygger braids the two together with a small set of primitives: versioned items, irrevocable *pins*, quotation by reference (*transclusion*), and a single response act called the *stub*. It also treats generative AI as something that happens at the level of individual blocks of text at authoring time, disclosed in the published record but absent from the protocol itself. This paper describes the problem the medium answers, how it feels to write in it, how it works underneath, and a set of deliberate refusals that turn out to be the closest thing the design has to a thesis.

# 1. Introduction: a minimal change, not a new medium

I want to start with a deflationary claim. Blygger is not a new medium in the sense that the web, or the blog, or Twitter were new media. It is a *minimal* update to two existing experiences, the blog and the early-Twitter microblog, made so that each can do something it currently cannot. A blyg (the word for a site that publishes this way) is readable today by any RSS reader ever written. A reader that has never heard of the protocol sees an ordinary feed and loses nothing. Everything interesting happens in the margin between what an old reader sees and what a client built for the protocol can do with the same files.

The name stacks three near-puns. *Blyg* is Swedish for "shy," and one vowel away from "blog." *Blygger* tips its hat to Blogger. And the *ygg* gestures at Yggdrasil, the Norse world tree, which is never finished and always still growing. The more mundane reason for the spelling is that both domains were free.

Some ancestry is worth naming up front. Robin Sloan's *Spring '83* (2022) showed that a small, opinionated protocol for personal publishing could feel fresh again. Ted Nelson's *Computer Lib / Dream Machines* (1974) supplied both of the odd words I lean on, *transclusion* and *intertwingled*. The protocol is pre-1.0, currently at version 0.4, with a reference client (Blygger Studio) and a growing set of independent clients. Nothing about the wire format is yet promised to hold still.

# 2. The problem: two kinds of time

Media keep time in two ways, and the distinction does most of the work in this paper, so it is worth stating carefully. I'm borrowing the terms loosely from Saussure's linguistics.

**Diachronic** time is time as a *sequence of states*. The thing changes, and the record of its changing is the point. A git log is diachronic. So is a blog series, a book's run of editions, or a software changelog. Each commit carries a message about what changed and why. The informal handle I use for this is "GitHub time."

**Synchronic** time is time as a *present moment*. The snapshot is the point. A Twitter feed, a group chat and a livestream are synchronic. Hot takes are all *now* and are never revised. The informal handle is "Twitter time."

Neither is better. They are different things that media are for. The trouble is that almost every serious act of public thinking needs both. You want to say something now, in conversation, and you also want to keep developing it. Other people want to respond to what you said *then*, while you keep revising what you think *now*. Existing media make you pick one, and every attempt to bolt the other on has gone badly:

- **Threads are clumsy.** A tweet thread is a synchronic medium doing an impression of a diachronic one: a long argument chopped into a stream, which cannot be revised as a whole.
- **Editable posts break provenance.** If a post can change silently, what did you actually say? Edit buttons on social platforms have always run into this problem, and the usual fixes (edit windows, edit histories nobody opens) are partial.
- **Nobody reads changelogs.** A diachronic record with no synchronic surface is invisible. The history exists, but nothing in the reading experience brings it forward.
- **Citation gets messy.** This is the scholarly end of the same complaint. If a document moves, a citation to it either rots or quietly comes to mean something else. You have to cite either a version or a moving target, and most media won't let you do the first.

These are four failed attempts at one problem, not four separate gripes. Each fix for one kind of time damages the other.

There is one old medium that actually solves the problem, and it is instructive: the book. An *edition* is a diachronic event that a synchronic reader can see and cite. "Second edition, page 214" is a stable reference to a text that kept changing. But editions work *because* they are rare: years apart, a handful per book. You cannot run a conversation at that tempo.

So the design brief for Blygger fits in one line: **keep the edition, drop the latency.**

# 3. How it feels to use

## 3.1 Fragments, threads and visible history

A blyg publishes *items*, and items come in two kinds. A **fragment** is a small unit: a note, a claim, a paragraph. A **thread** is a longer item, and threads can be built by composing other items. Most media give you one unit and make you pretend everything is that shape. Two units turn out to be enough to cover most of what people actually write.

Every item has a permanent identifier and a numbered version history. Editing a published item creates the next version. Readers see the latest one, plus a short public log of when it changed and why. On my own blyg, a fragment that happens to be a shopping list carries a line of page furniture that reads `v3 · pinned: v1, v3`. That single line is the diachronic surface sitting inside a synchronic feed, and it needs no explanation; it is just there on the page.

The older versions themselves stay private unless the author pins them. That brings us to the medium's central primitive.

## 3.2 Pins: editions at conversation speed

A **pin** is an irrevocable promise to keep one exact version of an item online, at its own address, forever, even if the author later edits or withdraws the item. Pins are editions. They are what make it safe to cite something that is still changing.

The version counter itself is deliberately bare: a number that goes up by one each time you publish. There is no semantic versioning and no "major edition" field. Significance is expressed by the pin, not the number. My shorthand for this is that an edition bump is cheap talk, and a pin is a costly signal. A pin is the only thing in the protocol that costs the author something, because it gives up the right to take that text back.

Nothing is ever hard-deleted, either. The one way out is **withdrawal**, which leaves a permanent, visible endcap at the item's address and tells other blygs to drop their copies. Pins survive withdrawal, because that is what a pin is for. Unpinned history, on the other hand, is unreachable by any route; otherwise withdrawal would be theater.

This gives a simple way to see how different kinds of writing fit the medium. Picture two dials: how often an item is revised, and how many of its versions are pinned.

| | **Few pins** | **Many pins** |
|---|---|---|
| **Few versions** | *The plain blog.* Publish once, move on. | *The document of record.* A constitution, a contract, a policy: stable text with every operative version on record. |
| **Many versions** | *The living document.* A notebook or an evergreen page, always current, with a dated log of changes. | *The portfolio of variants.* A book's editions, the drafts of a manifesto, a packing list kept in Thanksgiving and camping-trip variants. |

So the medium suits more kinds of writing than a blog does, including a book written in the open (chapters as items, editions as pins) and a Roam-style notebook. Most blygs have some of each.

## 3.3 Transclusion: quoting by reference

The load-bearing act in written culture is quoting, and most digital media have made it worse. Copy-paste loses the source. Embeds break or drift, because the embedded thing can change or vanish under you.

In Blygger, a thread quotes another item by writing a single line, `![[id]]`. At publish time, the author's client *bakes* a snapshot of the source into the thread and records exactly what it quoted: which origin, which item, which version. The reader gets the bytes the author saw, permanently, with a provenance line under the quote. If the source is later edited, or even withdrawn, the quote does not change. This is transclusion in Nelson's sense, implemented as a snapshot rather than a live embed. That choice is the whole difference between a quote that breaks and one that doesn't.

The same syntax works across sites. A thread on one blyg can quote an item on another, and the published page shows a citation block (what this responds to, at which version, with the URL and the date it was read) followed by the quoted passage and then the author's own words. Two details matter here.

First, **you can only quote what you have already read.** The identifier names an item, not an address, and it is resolved against copies already imported from subscriptions; the network is never touched. So publishing never depends on someone else's server being up, and their later edit can never reach into your page. Second, a quote is **not a fork**. A fork fetches a *pinned* version of someone else's item and starts a new draft from it, recording its lineage permanently. A quote embeds a copy you already hold.

## 3.4 Responding without replies

There is no reply button in the protocol, and there will not be one. There is a single response act, the **stub**: an item of your own that declares itself a response to exactly one other item. Publishing a stub notifies the other author, whose blyg checks the claim by fetching your item and confirming that it really names theirs.

I think of the stub as a kind of stem cell, one act that can grow into every familiar conversational shape depending on where you put your words and how much you quote:

- your words *above* a quote of their whole item make a quote-post;
- your words *below* it make a reply;
- your words around *one passage* make commentary, or an inline reply;
- a quote with no words of your own is a repost;
- and stubs of stubs make a conversation that is carried across everyone's sites, with each turn on the blyg of the person who said it.

There is an honest concession to make here. If quotation is the only form of response, then every response is structurally a quote-tweet, and quote-dunking is the shape of one of the internet's worst habits. What is different is everything missing around the gesture: there are no counts, no ratios, no reply-guy surface, and the quote is a frozen snapshot rather than a live embed. The gesture remains, but the incentive to perform it for an audience does not.

Responses can be shown under the item they answer, off by default and chosen per item, but only as a **list**: who, from which origin, in what relation, and when. Nowhere is there a number. A count is the one thing on your page a stranger can move; a row in the list costs them a real published item on a real domain that passed verification. The list is also rendered outside the item's versioned record, so nothing someone else publishes ever changes your bytes.

The same logic shapes participation. Anyone can read without a blyg, but joining in means publishing something of your own; there is no second tier of users who only comment. A site can still offer comments by hosting them as real items on a blyg it runs for the purpose, a convention now out for public comment as an RFC.

## 3.5 Two feeds, and pace layers

A blyg has two feeds, and the author controls both. The feed you *read* is private: subscriptions to blygs or any RSS feed, hand-curated collections, other people's blogrolls. There is no central timeline and no algorithm you didn't choose.

The feed you *show* is newest-first in RSS, but a front page can use the order the project recommends: **pace-layering**, after Stewart Brand's pace layers. Every item sinks as new ones arrive, but at different speeds. Pinning an item, or having it quoted in pinned items, moves it into a slower layer; revising it lifts it a place. A "featured post" becomes something a blyg *arrives at* through the author's behavior, not a setting.

## 3.6 The thicket

All of this is more involved than a blog, and it is fair to ask what the extra complexity buys. The answer is what the community has come to call the **thicket**, a name proposed by Aneesh Sathe to set the undergrowth against the platform's manicured garden. The thicket is the network of blygs and of the quotes, pins, forks and stubs that run between them.

Platforms bundled identity, archive, audience, conversation and ranking, so leaving meant losing all of it. A blyg unbundles these. The writing lives in files on the author's domain, and the connections between writers live on no one's server: they are written into the items themselves, as references to exact versions. Ideas grow by being quoted, answered and forked across sites, producing tangles rather than streams. The thicket is slower to walk than a feed, which is part of what keeps it healthy: there is no aggregate for anyone to farm.

# 4. AI at the block level

The talk that introduced Blygger carried a deliberately ungainly subtitle: *AI-intertwingled diachronic-synchronic social publishing*. The AI half of that phrase needs explaining, because it is easy to misread.

The philosophical motivation is this. Today's AI lacks *liveness*. A chat transcript is dead on arrival: nothing cites it, nothing revises it, and nobody else can build on it. Models are also, in a precise sense, *atemporal*. They are trained on the past and answer from outside time. My older argument was that AI is better understood as superhistory than as superintelligence: machines digest centuries of human experience per week, while individual human lives stay informationally sparse. If that is right, then one useful thing a medium can do is bring generated text back *into time*, putting it into a dated, versioned, citable, forkable record where it can live and be metabolized like any other writing.

Mechanically, the reference client does this with a century-old copy-desk mark, **TK** ("to come"), which signals text known to be missing. While drafting, an author can write an instruction inline:

`[TK]summarize the three quotes above[/TK]`

Running it asks the author's own model, with the author's own key, to fill that gap. The instruction and its output then sit side by side in the draft, so the passage can be regenerated or edited without losing anything. That is what *intertwingled* means here. It is not a chat window beside the editor or a mode you switch into, but an instruction typed in the middle of a sentence that stays there after it runs. One subtle rule follows: inside a TK scope, `![[id]]` means *source* rather than *quote*. It names material for the model to work from, and the author of that material is cited and notified just as if they had been quoted, so a model's paraphrase can never be a silent way to use someone's words.

Generation is always an explicit act the author reviews; publishing never generates anything. What reaches the published record is ordinary text plus *generation provenance*: a list saying which spans a model wrote, from which sources, with which model and when, and a CSS class on those spans in the HTML.

In the talk I showed a real published page, a heading and two paragraphs, and asked how much a model had written. The answer was both paragraphs. Nobody could tell, and that is deliberate. The disclosure is complete (view-source shows it in seconds) but not decorative, because the claim is self-asserted and nothing can verify it. A visible tint would dress an unverifiable claim up as a verified badge. In my own editor, the same paragraphs *are* tinted, because as the author I need to know what I still owe a careful read. Same bytes, two surfaces, two obligations.

The protocol never asks whether a person or a program wrote something. An agent can run its own blyg or write into someone else's with revocable permissions. The one norm for everyone is that a stub should be a real response, not a machine re-posting a feed.

# 5. How it works

This section is for readers who want the machinery.

**It's just files.** A blyg is a directory at an *origin*, a base URL on the publisher's own domain: a manifest (`blyg.json`), a feed (`feed.xml`), one JSON document per item (`items/{id}.json`), an archive index, and a page per item, with pinned versions at their own paths (`items/{id}/v{n}.json`). The protocol includes no database and governs only the published files. Copy the directory to any static host and it still works; the reference client checks this by exporting to flat files and diffing against the live server. "Just files" is the only durable answer to what happens when the company shuts down.

**It's still RSS.** Every blyg feed is a valid RSS 2.0 feed with self-contained HTML entries, and a blyg can subscribe to any RSS or Atom feed without the publisher's cooperation. An existing blog is already half inside the system: readable today. Upgrading buys being *quotable*, since transclusion needs the item documents and versions plain RSS lacks.

**Two planes.** Item documents and the archive index are the state of record; the feed is only a notification that something changed. Because readers reconcile against the index, a dropped or malformed feed entry costs a slower sync rather than lost data. This inversion is what lets the notification layer be as lossy as RSS really is. Version numbers never silently go backward: a regression is surfaced as a suspected history rewrite. Item identifiers are random 128-bit values, deliberately not content-addressed, so identity survives edits.

**The network.** Notification uses the W3C Webmention standard with one addition: a mention counts only if the sender's published item *structurally* names the target in a defined field. Mere link presence was the trackback check spam defeated two decades ago. Subscriptions are private and one-sided, as in RSS; the only public graph is what publishers choose to show, blogrolls going out and verified mentions coming in.

**Conformance levels** are strict supersets: **L0** is any RSS feed, **L1** a single blyg with versions, pins and threads, **L2** everything across origins. Readers ignore constructs they don't understand rather than rejecting the document, so the protocol can advance without breaking anyone.

**What the spec leaves open** is a long list: presentation, feed ordering, how authors write into a blyg (there is no normative write API), which models are used, and discovery. The few presentation rules that exist protect disclosure: CSS classes marking quotes and generated spans, which a theme may style but may not hide.

# 6. The refusals

Over several months of design, four separate decisions came out the same way, and I did not notice the pattern until the fourth. Each time, the question was whether to enshrine something in the protocol, and each time the answer was no:

- **AI.** Generation happens in the client at authoring time. The wire carries output plus provenance.
- **Identity.** There are no accounts and no handles. Your domain is your name, because DNS already works, and every *new* namespace is a registry with an owner, which is the thing the design is trying not to have. The protocol authenticates only the origin the bytes came from; author names are unverified, like a masthead. A proposed @-mention convention lets a mention carry whatever identifiers a person already has (website, fediverse, ATProto, Ethereum) inside an ordinary link. Mentions notify nobody; notification is reserved for citation.
- **Editorial convenience.** There is no reply primitive, because transclusion is the primitive.
- **Significance markup.** There is no semantic versioning and no edition field, because pins carry the weight instead.

The full list of refusals is longer and is written into the spec: no follower graph, no addressable author, no metrics of any kind, no title-extraction heuristics. The principle underneath them is stated as one sentence: **anything the protocol cannot verify, it declines to represent.** The reason is that a field which looks authoritative and isn't corrupts the fields that are.

This principle also resolves the apparent paradox in the talk's subtitle. "AI-intertwingled" and "AI is never in the protocol" are one claim seen from two sides. The AI is intertwingled in the *medium*, at authoring time and at the level of the block, and absent from the *wire*. The gap between those two is the distinction between the studio (the author's private tool) and the page (the public artifact), and that gap is why the distinction exists.

# 7. Method and status

Blygger is built implementation-first: constructs are exercised on live nodes before they become normative text, and building clients is how the protocol gets tested. Decided-but-unbuilt rulings are published, marked non-normative, so the reasoning can be argued with while change is cheap, and proposed conventions go through public RFCs. Comments are made, naturally, by stubbing.

At the September talk there was essentially one implementation, and I said plainly that one implementation is not a protocol but a program with a spec next to it. That has largely changed. Independent clients now publish a large share of live blygs: standalone clients, desktop and mobile authoring tools, a WordPress plugin, and integrations for Obsidian, Hugo and Logseq-style gardens. Several writers had an AI assistant write their client straight from the spec, some without having written software before, which is a modest test of whether the text is complete. The ecosystem index on blygger.org lists the clients; the directory at blygger.com lists live blygs.

Two gaps remain. One is a **local-first** client: a folder on a laptop, deployed to a dumb static host, with no server in the publishing path, which is the real test of the static-files claim. The other is a **conformance checker** anyone can run, now in review. And the caveat stands: before 1.0, nothing is stable, including the wire. What is stable, because it costs nothing to promise, is that every blyg feed is valid RSS, the published surface is static files, and nothing requires a company in the middle.

# 8. Conclusion: a tree that is never finished

Books solved the problem of two kinds of time by being very slow. Social media gave up on one of them. Version control solved it for code at the cost of being unreadable to anyone not reading the diff. Blygger's wager is that a handful of small, well-chosen primitives can let ordinary public writing have both: a present tense people can converse in, and a history they can cite. The primitives are versions, pins, quotation by snapshot, a single response act, and disclosed generation at the level of the block.

The aspirational name now seems more apt than it did when it was chosen mostly for domain availability. Yggdrasil is a tree that is never finished. A blyg, too, is a body of writing that keeps growing in public without losing track of what it was. The thicket of blygs is a forest of such trees, tangled together by quotations that point at exact moments in each other's growth.

If you write, the useful thing to report is whether writing this way changes *what* you write, or only how fast. If you publish, you already have the hard part: a domain nobody can take from you, and probably an RSS feed that makes you readable from a blyg today. If you decide this isn't for you, a clear account of why is the most useful failure report there is. And if you build, the open gaps are well-defined, undesigned, and waiting.

# References (to be completed)

- Brand, Stewart. *The Clock of the Long Now.* Basic Books, 1999 (pace layers; see also *How Buildings Learn*, 1994).
- Nelson, Ted. *Computer Lib / Dream Machines.* 1974.
- Rao, Venkatesh. "Superhistory, Not Superintelligence." *Contraptions*, 2021.
- Rao, Venkatesh. "Blygger: AI-intertwingled diachronic-synchronic social publishing." Talk, Protocol Symposium 2026, 24 September 2026.
- Protocolized. "From Destination AI to Intelligence Media." protocolized.io.
- Sathe, Aneesh. [Source for "the thicket" — to add.]
- Saussure, Ferdinand de. *Course in General Linguistics.* 1916 (synchronic/diachronic).
- Sloan, Robin. *Spring '83.* 2022.
- W3C. *Webmention.* W3C Recommendation, 2017.
- RSS Advisory Board. *RSS 2.0 Specification.*
- Blygger specification, v0.4. blygger.org/spec/. Blygger Studio reference client, github.com/blygger/blygger-studio.
