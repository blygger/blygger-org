# Front-page rewrite — raw materials

Session 49, 2026-10-17. Input for rewriting blygger.org's front page as two tabs,
**For Publishers** (default) and **For Developers**. Nothing here is copy. It is
the material a rhetorical strategy gets chosen from, in three parts:

- **A. Commentary from the thicket:** what five active blyggers have written about
  using Blygger, with quotes and item links.
- **B. Project state:** what is true now, what is coming, and what the current
  front page gets wrong.
- **C. Cross-cutting threads:** themes that recur across A and B, sorted by tab.

This directory is not built or published (`build.py` renders only `content/`).
The scaffold is `content/home.md`, built with `build.py --new-home`.

**Sources.** Each blyg's full public corpus was fetched through the protocol
(`items/index.json`, then every `items/{id}.json`) on 2026-10-17:

| Blygger | Origin | Items | Since |
|---|---|---|---|
| Aneesh Sathe | https://blyg.aneeshsathe.com/ | 116 | 2026-09-25 |
| Matthew McDowell-Sweet | https://www.msweet.net/notes/ | 274 | 2026-08-01 |
| Brady Dale | https://bradydale.com/blyg/ | 518 (5 more 404) | archive from 2018; blyg posts since 2026-09 |
| Surya Kasturi | https://blyg.suryakasturi.com/ | 32 | 2026-10-08 |
| Kyle Mathews | https://blyg.bricolage.io/ | 41 | 2026-09-27 |

Item links take the form `{origin}items/{id}.json`; the item's own page is linked
from there. Quotes are verbatim from `content_md`.

---

## A. Commentary from the thicket

### The word "thicket"

- **Aneesh, 2026-09-29** (`6d18a53bqh415pk1gm5cjqftmm`): "Blyg gives me the same
  extra cosy healthy thicket feels as the Disney short 'Burrow'… Even the poster
  reminds of connected blygs." Same day (`4wg6e1nsay4kq2rayy7jgqr9mp`) he renames his
  blyg *And Yet Here We Are*, a "Thicket+Culture name".
- **Aneesh, 2026-09-30** (`5qa0gy3fbhhbhtq6tfth4phdqd`): his desktop client is renamed
  **Burrow**, with themes of "thicket and oceanic sensibilities".
- **Aneesh, 2026-10-10** (`26v6rrp1shpfx356xvfg5r42r0`): "Blygs are great for remixing
  and *thicketing* but the surface for synthesis is still my blog… Blygger in the sheets
  blogger in the streets." (The verb.)
- **Venkat, 2026-10-16** (venkateshrao.com/blyg `65399vt9v05kjmm5kmc9f9s0f7`):
  "I think we should officially rename the blygosphere the thicket. HT Aneesh."
  Answered the same day from hungrybreadelevator.pages.dev/blyg: "Hello Thicket!", and
  Aneesh quoting that: "The thicket waves back 👋" (`7se19w08w7st22dbvge1c4390w`).
- **Aneesh, 2026-10-17** (`672mq3mb0ttrk0vsj1s3gr1652`), the best definition so far:
  "A blyg post is humus. identifiable in itself, but left there to decompose, combine,
  nourish, and be taken up elsewhere. It does not need to know what it will become. It
  only needs to be available to the thicket. And then the thicket grows with it."
- **Aneesh, 2026-10-17** (`57fc588wfp6k7sm97e2g5fkfw7`): "Thicketing is interesting, in
  that it turns the activity of researching into Place arranging… But thicketing still
  pretty unnatural to do—at least for me it is."
- **Kyle, 2026-09-29** (`1hxbrqnr9bx9x90261qgap5x6g`), the earlier naming round:
  "Blyggerstan, Blyggerville, Blyggerton, Blygernia, Blygernania 😜 Blygosphere wins for
  continuity." (The name the thicket replaces.)
- **The origin: Aneesh's essay "Logic of the Thicket and the Unsearchable Web"**
  (aneeshsathe.com, dated 20 December 2025, before Blygger existed;
  https://aneeshsathe.com/2025/12/19/logic-of-the-thicket-and-the-unsearchable-web/,
  written for the Contraptions Book Club). The word is in the title; the body argues
  against the platform as a Renaissance garden ("a rough draft to be corrected"), the
  social graph as Moreno's sociogram, and the global platform as "a pesticide… effective
  everywhere… indifferent to locality", which strips "noodiversity". It moves through
  the digital garden ("less a profile and more a dwelling") and finds the garden "too
  brittle, its walls too high": "To step away from the belvedere is to complete the
  descent from sight into touch, moving from the panoramic mastery of the graph toward a
  mode of navigation that relies on the immediate texture of the undergrowth. In this
  digital forest, we find the quiet virtue of opacity—a space where the individual is
  not fully mapped or categorized". Ends: "plant a single, idiosyncratic seed that the
  model cannot predict".
  → *Note the tension for the Thicket explorer: the essay prizes opacity and
  unsearchability, and the explorer would map the thicket. Matthew's version (below)
  answers it: traversal is slow and deliberate, done "blyg to blyg". Worth deciding
  whether the explorer follows trails (item to item, as a block explorer does) rather
  than offering a panorama.*
- **Matthew, 2026-10-17** (msweet.net/notes/121-onyx-kites, `4s8axky65tq51dba4pmcnhyt94`),
  the fullest public statement of the thicket as a stage in the web's history:
  "Platforms are our plantation, and they're well into ruin: the dead internet, ghost
  forums, link rot… Our first response was to hide, either in dark forests or in the
  cozyweb of group chats and private channels. But hiding isn't regrowth. What's
  actually growing back is Aneesh Sathe's thicket. It's tempting to mistake *new* for
  *primitive*… Blygger is the same. Static files, RSS and the blogroll look like a step
  backwards, but they're two decades of platform lessons compressed into a tiny spec:
  fragments and threads, but no replies, no likes and no graph to farm, because we've
  seen what gets farmed. Traversing a thicket is slow by design. There's no feed to
  scroll, no discovery layer, no algorithm to hand one the next thing. One moves blyg to
  blyg, along blogrolls and transclusions, the way animals move along trails they've worn
  themselves… Tourists bounce off… Extractors bounce off too, because there's no
  aggregate to harvest… But it isn't a walled garden either… every blyg is a public URL,
  and any feed reader gets in… Thickets are thorny… That friction isn't a bug to be
  engineered away. It's the immune system of an evolutionarily advanced ecosystem".
  Opens with Tsing's matsutake, which "come up in logged-over ruins".
  → *Publishers: this is almost a finished history-of-media paragraph (plantation →
  ruin → dark forest / cozyweb → thicket). Tension with the Publishers tab's goal of
  easy onboarding: "Tourists bounce off". Developers: "two decades of platform lessons
  compressed into a tiny spec".*
- Earlier usages of the word in Brady's corpus (3 items): see his section.

### Kyle Mathews — blyg.bricolage.io

Contributor to Blygger Studio (the `/api`, SDK, React studio, OAuth and MCP work).
Writes as a builder thinking about where the medium goes.

- **A new medium on an old layer.** (`1f3bb4y5r873cb883gh4r7zetn`, 09-29) "there's
  multiple layers here all named 'Blyg' — the underlying protocol up [to] Venkat's
  envisioned new style of blogging/tweeting — if you're using Blyg the protocol but
  basically just 'blogging' still then you're a blogger… But if Blyging becomes a
  genuine new medium then it deserves its own name. Potentially though Blyg the protocol
  could birth other mediums just like RSS helped enable Podcasting."
  → *Publishers (history: RSS → podcasting) and Developers (protocol vs. medium).*
- **First impression.** (`56amcjf6rkr77sgf76np9nm3vk`, 09-27) "There definitely feels
  like there's a there there with Blygger. Though distributed anything is rough for
  normies — needs a Bluesky-style frontend for that perhaps." Quotes "Something old,
  something new, something borrowed, something blue."
  → *The honest barrier for publishers; the case for hosted/easy clients.*
- **AI-assisted publishing from where you think.** (`4t9cns5ed3gk08hfvw4jsyw053`, 09-27)
  Added an MCP server so research sessions ("Field Labs") can save drafts and publish
  fragments: "I wanted a way to share interesting bits as they emerge." On `[TK]`: "TK
  does make for a nice balance between direct control and automation."
  → *Developers (agents and tools publish too); Publishers (TK as a writing aid).*
- **TK's history.** (`2nbb5wwsfqagwp5rj9g2bhagwz`, 09-27, his first blyg) Copy-desk
  shorthand for "to come", deliberately misspelled so it can't be mistaken for text;
  "a placeholder that announces its own incompleteness, holds its place in the argument,
  and waits to be replaced by the sentence it was standing in for."
  → *A ready-made explanation of `[TK]` for publishers.*
- **Social objects, and a progression from one author to many.**
  (`17a8qygtw9adthrtk1sf9gfhkf`, 10-11) Wikis separate *Activity* (recent changes),
  *Landscape* (what exists, how organised) and *History* (how an object developed);
  "we're trying to represent a collection of persistent, evolving intellectual objects
  through an interface originally designed to display publication events." Citing Jyri
  Engeström's social-object theory: "One author: A commonplace book… Two authors: A
  correspondence… Many authors: Something resembling the historical Republic of
  Letters… The basic test is whether Blygger is genuinely useful at the first stage.
  GitHub didn't have to invent a reason for people to interact with repositories."
  → *Publishers (useful alone first; the Republic of Letters as the many-author
  picture). Possibly the spine of the Publishers tab.*
- **Venkat's reply, quoted by Kyle** (`0etvbskt10hrmw15k43kahz02p`, 10-12): "time is
  sufficiently important to be a first-class organizing principle… one of the
  motivations for blygger was putting time back into relatively atemporal information
  architectures like wikis and digital gardens. A governing conceit is that everything
  lives inside time. No eternal or atemporal objects." Kyle: the studio is "highly geared
  towards micro-blogging"; a garden or a book wants a way "to subscribe to the right
  layer of updates… the raw change stream or a changelog or the intellectual artifact's
  blog (which is how repos work too)."
  → *Both tabs: time as the organising principle. Developers: layers of subscription.*
- **The Snowclone Fork Challenge.** (`2p2311b0zasaj9h90b6zxa74d5`, 09-30) "a fun way to
  get a feel for pins and forks": post an aphorism, pin it, others fork the pin, edit,
  pin their own. Worked example: Clarke → Schroeder → Paquet.
  → *Publishers: a concrete, playful picture of pins and forks.*
- **Legislator and physicist.** (`261bgm66kbgqxg7n8h8g44qeht`, 10-07) "We define a
  protocol and discover behaviors nobody explicitly designed, but which follow inevitably
  from its rules. At the layer where you create an abstraction, you're a legislator. One
  layer above, you're a physicist."
  → *Developers: the spirit of a pre-1.0 spec that changes as building finds things.*

### Surya Kasturi — blyg.suryakasturi.com

Runs Blygger Studio and files studio issues; a repo named `ksurya/blyggerpress`
appeared 10-16 (no description yet), after his "Maybe with a BlyggerPress" below.
Writes about interfaces and AI.

- **"Email Twitter."** (`4efjbqmttbavw44zj25r7rmx9y`, 10-10) "I didn't read the Blygger
  protocol, but with that caveat in mind… Blygger feels like Email Twitter. Individuals
  publish to their outbox, and everyone else can optionally subscribe. People write a
  reply by posting to their outbox, and the authors in the reply get a ping. Replies
  capture the entire content not just the link. Post provenance is like in email, and
  versioning is like in Git/books. I appreciate there are no likes, views displayed on
  the posts, bringing focus entirely to the post written, and people have stronger
  control over curating their feed. A better discovery mechanism would be cool when the
  blygroll is big… feels like the pieces are in place to capture long form, with better
  writing interface. Maybe with a BlyggerPress"
  → *Publishers: the clearest newcomer's description in the corpus, from someone who
  hadn't read the spec. "Outbox" is a strong plain-language handle.*
- **Email as a cautionary history.** (`3npqvc3v96j4x144s59tpdxf2k`, 10-14) SMTP was open,
  plain text, built for trusted communities; "the inventors had not foreseen that their
  project would break out of small trusted communities into the zero-trust masses… Spam
  scale and incentives made email practically no longer an open utility."
  → *Publishers (history: open protocols and what happened to them). Developers: why
  mentions are verified structurally.*
- **Titles.** (`0bnfkpepzw7hejzk8yc1ftwet4`, 10-13) "Never made sense why blogs ask for a
  title… Titles block the stream of consciousness." Prefers hashed IDs to naming URLs.
  → *Publishers: no title field, ids not slugs (decision #46) seen as a feature.*
- **Provenance of thought.** (`0z475jcx88crhzvy0k4wcxhgc6`, 10-08) "How to establish
  provenance of thought? we can potentially establish provenance of the artifact at the
  time of its creation".
  → *Disclosure of generated text.*
- **Conversations as raw material without an anchor.** (`2zn14jjw560mw0gxdbcjrtce3t`,
  10-13) "human x AI conversations capture human thinking much more precisely than any
  singular essay… we need a sharable internet anchor to communicate these."
  → *The "AI brought into time" argument, from a user's side.*
- **The new word problem.** (`05bnk2nvsev51pbr8n7ctdd255`, 10-11) "Claude et al do not
  yet recognize the words Blyg and Blygger. I have to literally refer them to the spec
  every time… As Claude et al diachronically grow, we can then compare".
  → *Developers: point readers' agents at the spec; maybe an llms.txt.*
- **Disclosure in practice.** (`4aw592sdq11wz7fkjty7vr6fkx`, 10-09) An essay with a
  provenance footer: "Original observations and central design insight by Surya
  Kasturi. Text developed collaboratively using OpenAI's GPT-6… The essay body is
  AI-generated and author-approved."
  → *Shows authors disclosing by hand, beside `generated[]`.*
- **Feeds and intent.** (`2wxaj0m3wfdd5qrvv8vxyx7e39`, 10-11) "All feeds have the same
  limitation: they incorrectly assume past behavior is indicative of future intent."
  → *Background for the Smart Feed (row 52).*
- Issues filed: studio#72 (Webmention flooding), #57 (feed scoring), #54 (MCP portals),
  #50 (passkeys), #49 (NextDNS), #56 (discard draft), #70 (endpoints under the mount).

### Aneesh Sathe — blyg.aneeshsathe.com

Runs Blygger Studio and builds **Burrow** (`aneeshsathe/blygger-desktop`), a
local-first, keyboard-first Mac and Windows client, released roughly weekly since
09-29; author of the conformance toolkit (spec#11), studio PRs and the extension
registry proposal (studio#59). The source of "thicket" (above). Item pages are
`{origin}f/{id}/` (fragments) and `{origin}t/{id}/` (threads).

**Disclosure note.** Two of his longest posts carry a `generated[]` record and read as
model output he published: "How to Blyg" (`594r3c8n14h0f9qgqbpsvnqeqp`) and "From Social
Media to Self-Sovereign Intermedia" (`3c6rc4ye8e3e6yt954syzgj5rw`); so does
`78cq34t2r33dtsrtw61mbmkje8` (`codex`). Quote them as published by Aneesh and disclosed
as generated. The humus fragment, "Blygger in the sheets" and the short posts below
carry no disclosure.

- **Self-sovereign intermedia** (`3c6rc4ye…`, 10-15, disclosed as generated). "it is not
  really an attempt to build a better social network. It suggests something more
  fundamental: that we may have mistaken the social network itself for a necessary
  piece of infrastructure." Platforms "bundled together almost every function of public
  life online… identity, publishing, discovery, distribution, conversation, social
  graphs, archives"; "To participate in the network, we must inhabit somebody else's
  territory." "In a platform, the network owns the nodes. In an intermedia, the nodes
  own themselves and the network emerges from their relationships." "It works with
  deliberately ordinary primitives: websites, files, feeds, links, quotations, and
  provenance." On AI: "The sophistication can live in the tools surrounding the
  sovereign node rather than in a centralized service." The message has to move from
  "This kind of web can be built" to "**I can do this.**" The catalytic project:
  "Imagine twenty writers… each operating their own blyg… If such a small ecology became
  genuinely lively… **Sociality does not require social media.**" "our ability to speak
  publicly should not require surrendering ownership of the place from which we speak."
  "The real success of Blygger would therefore arrive when owning one's public presence
  no longer feels like an eccentric technical choice. It simply feels like how the web
  works."
  → *Publishers: arguably the best one-page case for the medium in the corpus; the
  unbundling argument is the history-of-media frame.*
- **How to Blyg** (`594r3c8n…`, 10-17, disclosed as generated). "don't ask 'what topics
  should I post about?' Ask 'what units of thought deserve an address?'" "Post moves,
  not subjects" (a distinction, a connection, a named phenomenon, an observation, a
  question, a contradiction, a metaphor, a small finding, a revision). Threshold: "Would
  I want to be able to point to this exact thought six months from now? If yes, it
  deserves an ID." "Blygger does something stranger: it gives the pre-essay thought a
  durable public identity." "A thread is then one traversal through the graph, rather
  than the container… The essay stops being the fundamental object. The idea becomes
  fundamental." Cites Venkat on titling causing "functional fixedness" and
  "stem-celliness": "Fragments should retain optionality. Threads expend optionality to
  make an argument… the organism does not consume the stem cell." Loop: "notice →
  publish → notice → publish → connect → revise → compose" instead of "research →
  outline → draft → edit → publish". "An essay is a tree… A stream is a river… A Blygger
  archive can actually become a thicket: persistent little things growing independently,
  crossing, grafting onto each other… Publish things before you know what they're for."
  "Density comes first; structure emerges afterward."
  → *Publishers: a ready-made "how to write here". Tree / river / thicket is the cleanest
  three-way contrast found.*
- **Humus** (`672mq3mb…`, 10-17, his own): quoted in the thicket section above.
- **Weaving** (`78cq34t2…`, 10-17, disclosed `codex`). "Watching others use fragments
  expands the umwelt of the whole system. This is what made quote tweets so interesting…
  Versions, pinning, quotes etc. provides more dimensions to a fragment".
- **Where blygs sit for him** (`26v6rrp1…`, 10-10): "blygs _don't_ satisfy the basic urge
  to write something long… Blygs are great for remixing and thicketing but the surface
  for synthesis is still my blog… Blygger in the sheets blogger in the streets."
  → *Honest positioning: a blyg beside a blog, not instead of one.*
- **The setup gap** (`0h9rf84s…`, 09-27, replying to Kyle): "getting normies to spin up
  with own worker is going to be the hardest thing." OG: a domain, a website and blog;
  now also: a Cloudflare Worker, a way to post, AI, people to follow. "I'm hoping AI
  lowers the barriers sufficiently". And (`4d3ba442…`, 09-30): "a kit website where you
  work with your agent to slowly unbox and assemble the blyg… The creative power a domain
  name gives you is something that is not yet appreciated."
  → *Publishers: the barrier, named by a user. A guided, agent-assisted setup page.*
- **The newcomer's confusion** (`70rpja29…`, 09-29): "what is this blyg stub fork
  business?? How do i comment and retweet?"
  → *Publishers need the stub/fork/quote vocabulary mapped onto reply/retweet.*
- **The OG internet** (`5pn1kkk2…`, 10-01): "This is what the OG internet is about, you
  have to have your own identity and have something to say… Webmentions provide a little
  nudge that somebody cited your work, but if you reply or not is completely up to you."
- **Introverts and ambiverts** (`2d37sbk4…`, 09-29): "Extroverts need social media /
  Introverts need static websites / Ambiverts need static websites with social aspects."
- **Malleability** (`5hkd6hcm…`, 10-07): "Is it weird to have a dream that people be free
  of platforms and silos? The fun part of blygs is that it's malleable… I can mold my
  experience on the web anyway I want."
- **Rented ground** (`34tcxpq6…`, 10-09): "strange—that Substack should be the link to
  source of truth rather than the blyg. When did the internet stop feeling like it was
  ours?" And (`0xc2wt15…`, 10-07) quoting a Substack writer: "I only vaguely knew what a
  feed reader or RSS was" — "This is sadness".
  → *Publishers: RSS literacy can't be assumed.*
- **Discovery** (`7psyn4x3…`, 09-29): "Why are so many people's blogrolls empty?? Seems
  blygger.com is the only reliable way to find blygs right now."
- **Socialising the idea changes it** (`5zdf6q2y…`, 10-07): "we should wait before trying
  to figure out what Blygger is. Socializing the idea and tech through minds and hands
  changes it." And "Early protocol adoption is the new early adoption" (`719ep3qn…`).
  → *Developers: the spirit of a medium shaped by its builders.*
- **Protocols as kitchens** (`6ma5gfx1…`, 10-04): "Protocols need kitchens. A few
  appliances and the idea for a recipe." (`0ydrgtfx…`, 10-17): "Protocols and most tools
  we make are rather like kitchen tools rather than algorithms."
  → *Developers: the reference client as one kitchen among several.*
- **Eldritch blogging** (`5451d3jv…`, 10-01) quoting Venkat's Substack note: "Blygging is
  hereby declared to be Eldritch-blogging… The elderblog is a garden gone wild. The
  eldritch blog is a garden that has begun gardening you."
  → *Publishers (history): elderblogs → eldritch blogs → the thicket; Venkat's own
  lineage of ideas about blogging.*
- **Burrow release notes** as evidence of an independent client tracking the spec:
  0.7 "works with any blyg on blygger-studio 0.9 or later"; 0.8 a "lineage glyph… It
  never shows how many" (counts added later as opt-in); 0.10 Windows (ported by Patrick
  Atwater) and extensions (Obsidian notes; cross-post to Substack Notes); 0.11 OPML import;
  0.12 "a stock blyg is enough… Until now some of what it did leaned on patches to my own
  Worker. Those are gone"; "'Generated' is the publisher's word… nobody has verified it."
  → *Developers: the second-client story, told by its builder.*
- **Small culture**: "Back-stubbing would be a fun thing to come into parlance"
  (`534ypbq5…`); "Welcome Brady to the blyg universe! 🖖" (`4dbx2ez2…`); pronunciation
  "Bligh"; "the people will be Blyggeratti" (`11dhmv36…`); "I actually like to see
  protocol test posts… it gives the community an opportunity to welcome protocol
  initiates" (`50cecdm0…`).

### Matthew McDowell-Sweet — www.msweet.net/notes/

Publishes his notes stream as a blyg with his own generator (`msn-build/0.1`, a
"bespoke build" in the ecosystem's sense, roadmap row 63). Mostly link-and-comment
fragments; writes about protocol thinking. Proposed the Glass Bead Game extension
(blygger-spec#12, declined session 38 because the pattern already works). Item pages
are `msweet.net/notes/{page}`.

- **The thicket as regrowth after the platform ruin** (`4s8axky6…`, 10-17): see the
  thicket section above. His most quotable post.
- **Arrival** (`4z85svtm…`, 10-03): "No backsies; this little stream of thoughts-as-notes
  has entered the Blygosphere."
- **Protocol brain, and the Glass Bead Game** (`1h0t7hze…`, 10-03): "Product Brain must
  evolve to Protocol Brain. Don't make *the* client or *the* platform; make the
  protocol-ish engine that can power numerous arbitrary, value-adding manifestations of
  clients and platforms." Describes Blygger's "ethos and resulting protocol" as "blogs ×
  wikis × Twitter × git changelogs, built on static files and RSS". Works backwards from
  a weekly SIG game: brief = an item; moves = fragments and threads on each player's own
  blyg; lineage = `stub_of`; lock-in = a pin, "a permanent, irrevocable promise";
  notification = Webmention; the record = a thread transcluding every pinned move, then
  pinned. "Almost all of this already exists… Timing, turn order, spectators and judging
  stay out of the protocol entirely, just as AI does." (`716xtd4s…`, 09-27, has the
  earlier sketch with a worked fugue / desire-lines / oral-poets exchange.)
  → *Publishers: a concrete picture of what people do together in a blyg. Developers:
  a worked example of mapping a social practice onto the primitives without new wire.*
- **The reference client as a cooking demo** (`632rapqy…`, 09-27), quoting Venkat's
  Substack note: "The reference client is merely like a YouTube demo of cooking a
  recipe, not necessarily the thing you use… The protocol is some combo of the
  approximate recipe and the test suite you have to pass." His line: "Sufficiently
  advanced product thinking is indistinguishable from protocol thinking."
  → *Developers: the spirit of the project in one image (cf. Aneesh's kitchens).*
- **Protocol thinking for product people** (`5vt4cvsx…`, 10-04): eight shifts —
  "Expanding available moves over achieving specified outcomes; Surrendering majority
  stakes in value capture and credit; Higher standards and tighter reins around change
  governance; Evolutionary search and selection over solutions engineering; Care given
  via individual stewardship and collective goodwill, not exchange; Measuring what's
  given away… not what's captured; Making constant failure and certain death generative;
  De-centring humans amongst many other participating agents".
  → *Developers: how the project is run, said by a participant.*
- **Protocol bucket, platform spades** (`7y55ww5z…`, 10-13): "Git, with GitHub, GitLab
  and every editor as spades; email, with Gmail, Outlook and Apple Mail… a folder of
  Markdown, with Obsidian… and the web itself, with every browser as a spade." Versus
  "platform bucket, protocol spades" (Salesforce, Notion, Slack): the record held
  "inside a vendor-mediated product… all on their surprisingly mutable terms."
  → *Both tabs: a blyg is a protocol bucket; clients are spades.*
- **Algorithmic capture** (`76nts9ez…`, 09-18): "mistaking the narrowing of the system's
  You-model with a narrowing of your actual self… 'You' is bigger than a feed or a set
  of followers."
  → *Publishers: why no algorithmic feed.*
- **The closure of the internet** (`3t04swd9…`, 08-15), quoting Arctotherium: "the
  Internet is my culture, and watching this happen and living through it was and is
  agonizing." His line: "Reminder: 'We still early', 'There are many alternatives'".

### Brady Dale — bradydale.com/blyg/

A journalist (crypto, culture; Substack *Frontstage Exit*) who had never built software.
Built **Blynger** (`BradyDale/Blynger`, a Mac app) with ChatGPT and Codex to run his
existing static site and its blyg together: "Blynger is a static personal website
manager with Blygger interoperability built in." Posts daily: a reading series
(*October of Zarathustra*) and stubs across the thicket. His archive back to 2018 is
imported. Pages are `bradydale.com/blyg/{f|t}/{id}/`.

- **The non-programmer's arrival** (`4cgbkk3z…`, 09-26): "I vibecoded this up using Codex
  by showing it the Blygger protocol site. So hopefully it publishes correctly. In
  theory, this post is up to the spec… I think?" On disclosure: "that grey block above
  was generated with ChatGPT… Whenever I use that function on here, it will be indicated
  with that little grey box. To me this is a nice liminal place for writers who want to
  save some time on the boring bits of writing with AI while being transparent about
  it." (His grey indicator was later adopted in Blygger Studio 0.27; `383c1r8g…`: "very
  cool extension of the little AI graphical indicator I came up with!")
  → *Publishers: you can build your own with an AI assistant and the spec; disclosure as
  a writer's courtesy.*
- **"Software really is a whole thing."** (`7x21y2zg…`, 09-30): "Me two days ago: Blynger
  is basically in a useable state. Me this morning: I have a list of like 10 features to
  add". (`2a5g9xtw…`, 10-03): "this is my first time doing 'software development.' That
  is, telling ChatGPT what I want, having it make it. Asking different instances to
  check its work… It's been really fun and interesting". (`1114fka0…`, 10-15): "I don't
  think Blynger is going to go to v 1.0.0 until Blygger proper does."
  → *Both tabs: the honest texture of building from the spec with AI; the bespoke-build
  category (row 63).*
- **Learning the vocabulary** (`4e84b0ge…`, 10-03): "this is my first stub. I didn't
  undestand how stubs and quotes are different!… I tried doing a fork… I don't know that
  anyone would look at this page and think: 'Oh he's making a modification of the quoted
  post.'"
  → *Publishers: stubs, quotes and forks need plain explanations with pictures.*
- **Still blogging** (`6ph9kwb1…`, 09-29): "Probably a minority take, but I think the best
  term for people who use Blygger is just: bloggers. Blygger is a useful update to
  blogging. It extends blogging, but it's not separate… we're still in the blogosphere,
  if you ask me." On "thicket" (`3y84na8a…`, 10-16): "I can get behind that. Kinda nice
  to have a word that's not related to the protocol's name. It's like counter-cultural."
  → *Publishers: "a useful update to blogging" matches the talk's "minimal update".*
- **The return to the open web** (`0850yaj8…`, 09-30): "My bet? We're all returning to open
  web blogging. No one is really that invested in that many blogs yet. We've all been
  relegated to platforms for years." Old blogging got people acquainted through
  challenges (LiveJournal's "Draw Batgirl" meme, 1,000+ artists); asks Venkat to set
  challenges (which became the Snowclone Fork Challenge). "What's an old school blog you
  miss?"
  → *Publishers (history): blog culture's social rituals, now with forks.*
- **Own land, better crossings** (`2r07snmf…`, 10-15, on Aneesh's intermedia essay):
  "Squatting on your own hunk of digital land is what I've missed, but it was clear that
  the interaction across domains just wasn't good enough. Links and blogrolls weren't
  cutting it. We needed a more robust cross site interaction protocol. Feels good, man."
  → *Publishers: the single sentence of why, from a blogger's side.*
- **Conversational, not social** (`5tm5wern…`, 09-30): "since your identity is less
  important than the identity of your *content* in Blygger, it more seems like
  conversational media could be the better framing. It's designed for replying and
  iterating. **It's not designed for aligning**." And (`6rm3z649…`): no central feed as
  "headless architecture".
- **Writing for himself** (`01xnz7mj…`, 10-15, stubbing Venkat's "Blygger is kinda
  killing my motivation to write on substack"): "I'm writing more short punchy things
  here. My personal build is liberating, because my site doesn't log visitors in any
  way. I couldn't check stats if I wanted to. So it really does feel like I'm just
  writing for myself here. Making notes of my thoughts and etching them into the stone of
  the internet."
  → *Publishers: no metrics, felt as freedom.*
- **The short post returns** (`2z49aje7…`, 10-03): "Blog posts that were just a sentence
  long were once a thing, but that kind of mostly stopped (even as blogs mostly
  stopped). But what's old is new again… I think it's going to be interesting how the
  graph of Blygger diffuses across multiple URLs."
- **RSS literacy** (`51c4p61v…`, 10-07, on Aneesh's "This is sadness"): a younger coder
  "had never heard of RSS readers before", and "so, so many newer sites just don't even
  bother to build in RSS any longer… It's basically deprecated in new CMS's."
  → *Publishers: don't lead with "it's just RSS" as reassurance; explain it.*
- **Pinning a draft in public** (`5jatk96e…`, 10-01, "A social manifesto"): "In the true
  spirit of Blygger, I'm starting a post… I'm going to try to edit this and develop it…
  I'll pin it at certain points to preserve how it develops." Now at V.2 (10-13).
  → *Publishers: a real example of a living document with pinned stages.*
- **The block explorer** (`4her79p5…`, 10-13, stubbing Venkat's "Wonder if could have a
  blygexplorer like a block explorer"): "what if blocks are created when posts are
  stubbed? That seems like a sort of proof of work. Random posts that just sit there on
  their own and get no reaction don't go into the explorer? It seems like a post
  activates the protocol when it crosses borders. Posts with no reaction are basically
  uncle blocks." See section B (The Thicket).
- **The Eye of Sauron is gone** (`05e0k8zk…`, 10-17): "thanks to the thicket, I have been
  made aware that there is drama on Farcaster… since Elon bought X so many people have
  left to till other fields! It doesn't feel like there's an Eye of Sauron of social
  networks any longer."
- **Building your own stage** (`34kzerxr…`, 10-17): "In the gatekeeper era… you could get
  on stage with a shrug… In a democratized era, no one is going to pull you on stage. You
  have to build your own stage, right?"
- **Small culture**: "The OG blyg. The Genesis blyg." (`1p1rknaxdt…`, of venkateshrao.com/blyg);
  "This is *actually different.* So it could end up being something." (`4r5p5yy2…`); "New
  users' favorite thing to talk about is the medium" (`3fsw41n5…`); "Nice, nice, very nice
  — So many different people In the same device" (Vonnegut, `383c1r8g…`); Clone.fyi as a
  hand-curated link aggregator "Blygger users need to know about".

---

## B. Project state (as of 2026-10-17)

Sources: `blygger-spec/ROADMAP.md`, `docs/roadmap.md`, `docs/roadmap-tracks.md`,
`docs/backlog.md`, the locked decisions in `blygger-spec/CLAUDE.md`, the Symposium talk
(`talks/2026-09-24-blygger/talk.md`), the ecosystem census, blygger.com.

### What is true now

- **The thicket:** 16 clients across 23 live blygs in blygger.com's directory (census
  2026-10-17). Most clients were written by people other than the protocol's author,
  several by people building software for the first time with an AI assistant (Brady's
  Blynger). The ecosystem page groups them as clients, **bespoke builds** (n=1 sites from
  the owner's own generator: Matthew's `msn`, Ben Mayhew, `cchalc`, `sig-p4b`),
  **integrations** (Obsidian `blyg-publisher`, Logseq `goddinpotty`, `hugo-blyg`,
  **Soapbox for Blygger**, a WordPress plugin listed in the WordPress.org directory),
  **authoring tools** (Burrow for Mac and Windows; `drafts-blyg`; `static-to-studio`),
  **mods** of Blygger Studio and studio **extensions**.
- **The reference client:** Blygger Studio 0.46.3 (MIT, Cloudflare Workers), released
  near-daily; runs venkateshrao.com/blyg, blyg.protocol-institute.org, the official
  blyg at blyg.blygger.org (decision #66: announcements, release notes, RFCs), and other
  people's nodes. Recent publisher-visible features: a setup walk-through (0.42), the
  pace-layered "diachronic" home page (0.42), a static front page (0.43), a links
  section and main menu (0.44), own posts in hoppers (0.45), Settings on one page (0.46),
  OAuth and MCP access for other tools (0.28 onward), extensions (0.37 onward).
- **The spec:** 0.3 is the living document (cross-client threads, stubs, forks, partial
  quotes, Webmention with structural verification, generation disclosure). **0.4 is about
  to open** (a Fable round is staged today): generation that draws on other blygs'
  items with a `source` mention (built, studio 0.41), and the manifest locating the rest
  of the surface through URI templates, which is what let Soapbox put WordPress on the
  wire. No version before 1.0 is stable (decision #21).
- **Open for comment until 2026-11-04:** RFC-1 (mentions across identifier schemes:
  address book, @-mentions, member bylines) and RFC-2 (comments sections as an owner's
  curated display of real stubs), on blyg.blygger.org.
- **Conformance:** Aneesh's conformance and intent toolkit (spec#11) is in review;
  blygger.com is to run it daily (com#1).

### What is coming (from the roadmap, top first)

- Spec: 0.4 opened with templated surfaces promoted (row 13, 24); author-chosen link
  text `[[title | id]]` (row 66, asked for by Venkat and by Ned Twigg on spec#16); TN-2
  identity practice (row 14); Unicode on the wire (row 26).
- Studio, publisher-visible: stub passage chooser in preview (9), browser-side image
  resize (10), owner API under the mount (64), links from [TK] output (67), blogroll
  entries as links (68), reading order as a setting (69), discard draft in plain view
  (51), OPML import (57), error log (59); later: full backup and restore (15, 53),
  mentions as a reading channel (16), opt-in listing at blygger.com from the studio
  (17), password reset with a recovery code (18), RFC-1 features (20), AI spending caps
  (30), discovery from references: quote-chain view, "responds to" walk, second-degree
  blogrolls (31), self-host template with upgrade (32), passkeys (34), Smart Feed (52),
  pour-over links (40), permalinks with slugs (42).
- Org: bespoke builds documented and encouraged (63); **the Thicket explorer** (new,
  this session; see below).
- Com: daily conformance runs (22), a "you are behind" notice per node (33).

### The Thicket explorer: what has been said

- **Venkat, 2026-10-13** (venkateshrao.com/blyg `6khf649fapt3m5k8hzhsbgypng`): "Wonder if
  could have a blygexplorer like a block explorer. The blygosphere thicket (we should
  just start calling it the thicket) is better connected than old web so should make for
  a better exploration space. And since the links are structural in a way that hopefully
  resists atomization, discovery, crawling, and 'garbage collection' so to speak should
  remain well-posed even if aggregators emerge. **I'd like to evolve blygger.com into
  something that resembles etherscan rather than a flat directory. Map the thicket and
  make it navigable without legibilizing it.**" Links *How to Take Your Brain Off-Road*
  (ribbonfarm, 2016).
- **Brady, same day:** blocks created when posts are stubbed, "a sort of proof of work";
  "a post activates the protocol when it crosses borders. Posts with no reaction are
  basically uncle blocks."
- **Aneesh's essay** prizes "the quiet virtue of opacity" over "the panoramic mastery of
  the graph"; **Matthew**: traversal "blyg to blyg… the way animals move along trails";
  **Surya** (`2mdp4cvepbwtr8kj1s6wh90bde`): "There's really no good interface for humans
  to perceive knowledge in multi-dimensional, non-linear relationships"; side panels of
  breadth-first or depth-first relations help.
- **Already on the roadmap and related:** row 31 (quote-chain view, "responds to" walk,
  second-degree blogrolls), Burrow's lineage glyph and ⌘J "follow the thread".
- **Ruled (Venkat, 2026-10-17):** the explorer goes on **blygger.com**; the idea
  description lives at **blygger.org/thicket/**, which says so and links across.

### What the current front page gets wrong or leaves out

The current `content/overview.md` (and the September talk it draws on):

- **Speaks to both audiences at once:** the synchronic/diachronic essay, the GitHub
  table, wire details (`![[id]]`, `/blyg/`, Webmention) and the version history are
  interleaved, so a publisher meets jargon in paragraph two and a developer meets
  philosophy before the spec link.
- **Out of date:**
  - "Status" leads with the first two live nodes "subscribed to each other since August
    2026"; the thicket is now 23 live blygs on 16 clients.
  - The talk's "Nothing to install yet, honestly" and "a second implementation… It is
    undesigned. It could be yours" are both overtaken: there are many second
    implementations, a WordPress plugin, a desktop client.
  - No mention of the thicket, blyg.blygger.org (the official blyg, RFCs), Soapbox /
    WordPress, Burrow, the bespoke-build category, the setup walk-through, the
    pace-layered home page, or MCP/OAuth for agents and tools.
  - "Mentions… Spam dies at the door": true of structural verification; the endpoint
    also has rate limits now (studio#72 reply, 2026-10-17).
- **Missing for publishers:** any route in that doesn't start with Cloudflare; what
  stubs, quotes and forks look like (users asked: "How do i comment and retweet?", "I
  didn't undestand how stubs and quotes are different!"); what RSS is (users report it
  is no longer common knowledge).
- **Missing for developers:** the conformance toolkit, the ecosystem as evidence the
  spec is implementable from the text alone, the RFC process, the decision record, the
  `generator`/census convention, how to get listed.
- Still right and worth keeping: the four ancestors (blogs, Twitter, wikis, git), the
  name's three readings, books as slow editions ("keep the edition, drop the latency"),
  "a network of soapboxes, not a conversation medium", "AI-native, AI-free wire",
  "DNS is the namespace", "no promises before 1.0".

### Design commitments a developer should meet early (from the decisions)

Static file contract (#1); AI never in the protocol, disclosure on the wire (#5, #20,
#59); identity never in the protocol, the origin is the publisher (#11, invariant 6);
no reply primitive, ever, transclusion is the primitive (#12, #27); discovery by
blogrolls and verified mentions, no follower graph (#13, #28); mount independence
(#14); versions are a bare counter and pins carry significance (#19); every feed is a
valid RSS 2.0 feed and unknown constructs are ignored (invariants 1–2); no normative
write API (#31) though tokens, OAuth and MCP exist in the reference client (#52); the
protocol is agent-agnostic (#38); the version boundary rule (#43); refused for good:
replies, follower graphs, addressable authors, metrics of any kind, a title field.
Process: pre-1.0 spec is always draft (#21); building finds things and the spec changes;
RFCs on the official blyg with a comment period before the studio blesses a convention.

---

## C. Cross-cutting threads

Grouped by the tab each serves best. Quotes in A.

### For Publishers

1. **The unbundling story.** Platforms bundled identity, publishing, discovery,
   distribution, conversation, graph and archive (Aneesh's intermedia essay); the
   plantation went to ruin and people hid in dark forests and the cozyweb (Matthew);
   the thicket is what grows back. Spine candidate for "Where this comes from", with
   the older lineage: homepages → blogs and RSS (blogrolls, challenges, the one-sentence
   post) → platforms (the Eye of Sauron, rented ground) → newsletters (Substack as "the
   link to source of truth") → the thicket. RSS → podcasting (Kyle) as the precedent for
   a protocol birthing a medium.
2. **"A useful update to blogging"** (Brady), "a minimal update… not a new one" (talk),
   "Blygger in the sheets, blogger in the streets" (Aneesh). Modest framing that
   publishers trust; a blyg sits beside a blog or a Substack.
3. **Own land, better crossings.** "Squatting on your own hunk of digital land… Links
   and blogrolls weren't cutting it" (Brady); "our ability to speak publicly should not
   require surrendering ownership of the place from which we speak" (Aneesh); "I can do
   this" as the message.
4. **Plain-language handles:** "Email Twitter" / an outbox (Surya); "a network of
   soapboxes" (current page); tree / river / thicket (Aneesh's "How to Blyg");
   "protocol bucket, platform spades" (Matthew).
5. **Units of thought with addresses.** "what units of thought deserve an address?";
   fragments as stem cells, threads as organisms; humus "available to the thicket";
   titles optional ("Titles block the stream of consciousness", Surya).
6. **What people do together:** fork challenges (Kyle, Brady, Venkat), the Glass Bead
   Game (Matthew), back-stubbing, welcoming newcomers, a manifesto pinned as it grows
   (Brady).
7. **No metrics, felt as freedom:** "I couldn't check stats if I wanted to… writing for
   myself" (Brady); "no likes, views displayed… bringing focus entirely to the post"
   (Surya); "You is bigger than a feed" (Matthew).
8. **AI, disclosed:** the grey box (Brady); TK as copy-desk tradition (Kyle); provenance
   footers (Surya); AI as the thing that lowers the setup barrier (Aneesh, Brady).
9. **Honest friction:** setup is the hardest part (Aneesh, Kyle); "Thickets are thorny…
   Tourists bounce off" (Matthew) versus "I can do this" (Aneesh). The tab has to pick
   how much friction to own and how much to lower (Soapbox for WordPress, the setup
   walk-through, Burrow, building your own with an assistant).

### For Developers

1. **Protocol over product:** the reference client as a cooking demo; "the protocol is
   some combo of the approximate recipe and the test suite you have to pass" (Venkat via
   Matthew); "Protocols need kitchens" (Aneesh); "Product Brain must evolve to Protocol
   Brain" (Matthew); eight shifts of protocol thinking (Matthew).
2. **Proof by implementation:** Burrow tracking the studio until "a stock blyg is
   enough"; Blynger built by a non-programmer from the spec; Soapbox fitting WordPress
   via templates; bespoke builds. "Implement from the spec alone" is now demonstrated,
   not aspirational.
3. **Legislator and physicist** (Kyle): the spec makes rules, building discovers their
   consequences, and the spec changes before 1.0 because of what building finds (#21).
   "Socializing the idea and tech through minds and hands changes it" (Aneesh).
4. **Two planes** (talk): item documents are state, the feed is notification; the index
   reconciles. Plain RSS as the floor.
5. **Layers of subscription** (Kyle): raw changes / changelog / artifact blog, as repos
   work; wikis' activity / landscape / history.
6. **Agents and tools publish too:** MCP and OAuth in the reference client (Kyle's Field
   Labs), the protocol agent-agnostic (#38); point your agent at the spec (Surya: models
   don't know the word yet).
7. **What the spec refuses, and why:** anything it can't verify, it declines to represent
   (talk: replies, metrics, identity, significance markup, AI).
8. **Mapping practices onto primitives without new wire:** the Glass Bead Game worked
   example (Matthew) and its ruling (spec#12: the pattern already works).

### Terms

- **thicket** (official from 2026-10-16; replaces *blygosphere*; Aneesh's coinage,
  essay of 2025-12-20). Link every use to `/thicket/`. Verb in use: *thicketing*.
- Other coinages seen: *blygverse*, *Blygger-verse*, *blyggerverse*, *Blyggeratti*,
  *back-stubbing*, *eldritch blogging*, *blygexplorer*, *intermedia*. None official.

### Decisions to make before drafting

1. Rhetorical spine for Publishers: the history of media (unbundling → ruin → thicket),
   the practice (units of thought with addresses), or the people (the thicket's own
   voices quoted)?
2. How much to quote ecosystem members on the page, and whether to ask them first.
3. How to handle setup friction: own it ("thorny"), route around it (WordPress, desktop,
   assistant-built), or both.
4. ~~Where the explorer lives~~ — ruled: blygger.com; the idea page is blygger.org/thicket/.
5. Whether the shared lede above the tabs says "thicket" at all, or leaves it to the
   Publishers tab.
6. Design: the "On this page" rail lists both tabs' headings at once; per-tab rail items
   would read better (a small `tabs.js`/build change).
