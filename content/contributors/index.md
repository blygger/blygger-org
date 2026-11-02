# Contributors

Blygger is built in public, by more people every week. This page credits
them in two groups. The first tab is for work on
the protocol itself and on the reference client, [Blygger
Studio](https://github.com/blygger/blygger-studio): pull requests, bug
reports, proposals. The second is for people building **their own** clients,
integrations and tools — the independent implementations that show the
protocol works from its spec alone.

Everything here is drawn from the public record: pull requests and issues in
the [blygger](https://github.com/blygger) repositories, and the
[ecosystem index](/ecosystem/). If you are missing, or described wrongly,
[open an issue](https://github.com/blygger/blygger-org/issues/new/choose).

<div class="tabset" markdown="1">

<section class="tab-panel" data-tab="protocol" data-label="Protocol & reference client" markdown="1">

## Core contributors

### Venkatesh Rao — [@vgururao](https://github.com/vgururao)

Started the protocol. Author of the specification (0.1 through 0.4) and of
the decision log behind it; maintains Blygger Studio, this site, and the
[blygger.com](https://blygger.com) directory, and runs the first live node at
[venkateshrao.com/blyg/](https://venkateshrao.com/blyg/).

### Kyle Mathews — [@KyleAMathews](https://github.com/KyleAMathews)

Much of the reference client's current architecture:

- **Rebuilt Studio** as a React single-page app on a validated resource API
  with a generated SDK
  ([#21](https://github.com/blygger/blygger-studio/pull/21),
  [#22](https://github.com/blygger/blygger-studio/pull/22); 0.10.0).
- **Made the public homepage fast**: batched reads and indexed lookups took
  time to first byte from about 4 seconds to about 0.35
  ([#25](https://github.com/blygger/blygger-studio/pull/25); 0.11.1).
- **Scoped client access with OAuth and MCP**, so other software — including
  AI agents — can work with a node under tokens its owner grants and revokes
  ([#34](https://github.com/blygger/blygger-studio/pull/34); 0.28.0).
- **Cut database reads** from Studio's polling and the public feeds
  ([#40](https://github.com/blygger/blygger-studio/pull/40); 0.32.0).
- **A 60-second public page cache**
  ([#41](https://github.com/blygger/blygger-studio/pull/41); 0.33.0), Webmention
  delivery for long subscription origins
  ([#42](https://github.com/blygger/blygger-studio/pull/42)), and shared source
  schemas ([#43](https://github.com/blygger/blygger-studio/pull/43)).
- **Led the 0.49 API cleanup**, eleven pull requests tracked in
  [#92](https://github.com/blygger/blygger-studio/issues/92): the private API under the
  deployment mount, conditional item writes, bounded cursor pages, media
  addressed by digest, complete HTTP validators, and one set of operations
  shared by REST and MCP (0.49.1–0.49.12).

Runs [blyg.bricolage.io](https://blyg.bricolage.io/).

### Aneesh Sathe — [@aneeshsathe](https://github.com/aneeshsathe)

The protocol's most thorough reader so far, and the first to test it
systematically:

- **A conformance and intent toolkit**, with a first-round report
  ([blygger-spec#11](https://github.com/blygger/blygger-spec/pull/11)): every MUST, SHOULD and MAY in the 0.3 spec indexed, JSON Schemas
  for every document, a read-only crawler that checks the live network
  against the spec, and formal models of the rules that turned up gaps
  worth ruling on. Since extended to 0.4 with **a reader suite**: 100
  fixtures, written from the spec text, that any client's renderer can run
  ([blygger-spec#22](https://github.com/blygger/blygger-spec/pull/22)).
- **Twenty-nine issues** across the spec and Studio, twenty-four of them
  closed: grammar edge cases in transclusion and generation scopes, importer
  and lineage bugs, and the question that made `[[id]]` links inert inside
  code ([blygger-spec#4](https://github.com/blygger/blygger-spec/issues/4)).
  A suggestion of Aneesh's put public hoppers on pages of their own (0.24.0).
- **Studio redesigned for the phone**
  ([#32](https://github.com/blygger/blygger-studio/pull/32),
  [#36](https://github.com/blygger/blygger-studio/pull/36); 0.22.0).
- **Studio's extension mechanism**
  ([#52](https://github.com/blygger/blygger-studio/pull/52)), with Aneesh's lineage glyph
  and hex view as the first extension
  ([#53](https://github.com/blygger/blygger-studio/pull/53)).
- Read state for imported items, OPML import and attachments per version
  ([#44](https://github.com/blygger/blygger-studio/pull/44),
  [#74](https://github.com/blygger/blygger-studio/pull/74),
  [#80](https://github.com/blygger/blygger-studio/pull/80)), and the proposal that
  made public hoppers subscribable
  ([blygger-spec#18](https://github.com/blygger/blygger-spec/pull/18), ruled as
  decision #86).

Also builds [blygger-desktop](https://github.com/aneeshsathe/blygger-desktop)
(see the ecosystem tab), and runs
[blyg.aneeshsathe.com](https://blyg.aneeshsathe.com/).

## Contributors

- **akash** — [@akashtattva](https://github.com/akashtattva). The mobile
  navigation and Contents drawer on this site
  ([blygger-org#1](https://github.com/blygger/blygger-org/pull/1)), and blyg
  feeds that strict RSS readers accept
  ([blygger-studio#33](https://github.com/blygger/blygger-studio/pull/33)), and an
  SDK build that works on Windows
  ([#89](https://github.com/blygger/blygger-studio/pull/89)).
- **Robert Peake** — [@cyberscribe](https://github.com/cyberscribe). Proposed
  that the manifest say where the rest of a blyg lives, so sites that cannot
  follow the file layout — WordPress, for one — can still publish one
  ([blygger-spec#2](https://github.com/blygger/blygger-spec/issues/2)). Ruled
  in as decision #51 and scheduled for 0.4. Also found that the Webmention
  target check excluded pages and item documents that 0.4 lets live outside
  the base URL
  ([blygger-spec#17](https://github.com/blygger/blygger-spec/issues/17), decision #84).
- **Brady Dale** — [@BradyDale](https://github.com/BradyDale). The robot
  badge that discloses generated text began as a convention on
  [bradydale.com](https://bradydale.com/76.html); Studio adopted it in 0.27.0.
- **Anuraj R** — [@anuraj-rp](https://github.com/anuraj-rp). An RFC for an
  optional content identifier on pinned versions, for mirroring pins to IPFS
  ([blygger-spec#13](https://github.com/blygger/blygger-spec/issues/13)).
- **Matthew Sweet** — [@msmsim](https://github.com/msmsim). A proposed extension for
  Glass Bead Games
  ([blygger-spec#12](https://github.com/blygger/blygger-spec/issues/12)).
- **Mike Casey** — [@miguelito4](https://github.com/miguelito4). A custom
  theme with live preview and a reading typeface for Studio
  ([blygger-studio#58](https://github.com/blygger/blygger-studio/pull/58)).
- **Raynaud Simon** — [@keyral](https://github.com/keyral). Reported broken
  links in the spec's docs
  ([blygger-spec#3](https://github.com/blygger/blygger-spec/issues/3)).
- **djinna** — [@djinna](https://github.com/djinna). Asked for a way to size
  inline images
  ([blygger-studio#37](https://github.com/blygger/blygger-studio/issues/37)).
- **Surya Kasturi** — [@ksurya](https://github.com/ksurya). Asked for passkeys
  and a discard-draft button, and reported what it takes to put a blyg's MCP
  server behind Cloudflare's MCP portals
  ([blygger-studio#50](https://github.com/blygger/blygger-studio/issues/50),
  [#54](https://github.com/blygger/blygger-studio/issues/54),
  [#56](https://github.com/blygger/blygger-studio/issues/56)); reported that
  Webmentions could be used to flood a node
  ([#72](https://github.com/blygger/blygger-studio/issues/72)); asked for every
  endpoint under the mount ([#70](https://github.com/blygger/blygger-studio/issues/70))
  and for stubbing without subscribing
  ([#83](https://github.com/blygger/blygger-studio/issues/83)).
- **Ned Twigg** — [@nedtwigg](https://github.com/nedtwigg). Asked for
  comments inside transcluded ids
  ([blygger-spec#16](https://github.com/blygger/blygger-spec/issues/16)), which
  became the `[[id | label]]` form (decision #70), and for tooltips in Studio
  ([blygger-studio#48](https://github.com/blygger/blygger-studio/issues/48)).
- **Florian Lohse** — [@florianlohse](https://github.com/florianlohse). Moved
  a blyg to a new origin, and filed the issue that turned moving into a
  rule, origin succession
  ([blygger-studio#102](https://github.com/blygger/blygger-studio/issues/102),
  decision #88).
- **Rafael David** — [@rafaeldavid](https://github.com/rafaeldavid). Four
  reviews of the HTTP and agent-facing surface: validators and immutable pins
  ([blygger-studio#87](https://github.com/blygger/blygger-studio/issues/87)),
  fetched text as data for agent readers
  ([blygger-spec#19](https://github.com/blygger/blygger-spec/issues/19)),
  published JSON Schemas
  ([blygger-spec#20](https://github.com/blygger/blygger-spec/issues/20)), and
  soft 404s on this site
  ([blygger-org#4](https://github.com/blygger/blygger-org/issues/4)).
- **Shannon** — [@shannonbux](https://github.com/shannonbux). Studio's
  controls moved onto shared Base UI primitives, with a component gallery
  ([blygger-studio#88](https://github.com/blygger/blygger-studio/pull/88), in progress).
- **Ruthvik Peddawandla** — [@ruthvik-947](https://github.com/ruthvik-947).
  The `nodejs_compat` flag in the config `npm run init` writes
  ([blygger-studio#46](https://github.com/blygger/blygger-studio/pull/46)).

</section>

<section class="tab-panel" data-tab="ecosystem" data-label="Ecosystem" markdown="1">

## Ecosystem contributors

People building their own clients, integrations and tools, alongside the
reference client. The [ecosystem page](/ecosystem/) indexes the projects and
the live blygs they serve.

- **Brady Dale** — [@BradyDale](https://github.com/BradyDale).
  [Blynger](https://github.com/BradyDale/Blynger), an independent client on
  its own version line, publishing at [bradydale.com/blyg](https://bradydale.com/blyg/).
- **Robert Peake** — [@cyberscribe](https://github.com/cyberscribe).
  [Soapbox](https://github.com/cyberscribe/soapbox-blyg), a WordPress plugin
  that publishes a blyg — the first client built on the manifest-located
  surface proposed in blygger-spec#2, publishing at
  [robertpeake.com/blyg](https://www.robertpeake.com/blyg/).
- **Aneesh Sathe** — [@aneeshsathe](https://github.com/aneeshsathe).
  [blygger-desktop](https://github.com/aneeshsathe/blygger-desktop), a native
  macOS studio for blygs in Rust.
- **Mike Casey** — [@miguelito4](https://github.com/miguelito4).
  [drafts-blyg](https://github.com/miguelito4/drafts-blyg), one-tap fragments
  from a phone via Drafts, and
  [static-to-studio](https://github.com/miguelito4/static-to-studio), which
  moves a static blyg into Blygger Studio at the same address. Wrote a static
  client, `caseyjr-blyg`, before moving
  [caseyjr.org/blyg](https://caseyjr.org/blyg/) into Studio with it.
- **Brandon Pink** — [@brndnpink](https://github.com/brndnpink).
  [blyg-publisher](https://github.com/brndnpink/blyg-publisher), an Obsidian
  plugin that publishes a blyg from a folder of your vault.
- **Christopher Boette** — [@chrisbodhi](https://github.com/chrisbodhi).
  [hugo-blyg](https://github.com/chrisbodhi/hugo-blyg), a blyg from a Hugo
  site, published at [newschematic.org/blyg](https://newschematic.org/blyg/),
  and [blygd](https://github.com/chrisbodhi/blygd), a headless, multi-tenant
  studio in Go that speaks 0.4.
- **Mike Travers** — [@mtravers](https://github.com/mtravers). Taught
  [goddinpotty](https://github.com/mtravers/goddinpotty), a digital-garden
  generator for Logseq graphs, to emit a blyg:
  [AMMDI](https://ammdi.hyperphor.com/blyg/).
- **Patrick Atwater** — [@patwater](https://github.com/patwater).
  [pioneering-spirit-blyg](https://github.com/patwater/pioneering-spirit-blyg),
  Blygger Studio extended to run [Pioneering Spirit](https://blyg.pioneeringspirit.xyz/)
  beside its old archive, and
  [a Windows port](https://github.com/patwater/burrow-blyg-windows-) of
  blygger-desktop, and [blygcaster](https://github.com/patwater/blyg-caster),
  Studio extended to read Farcaster, stub casts and cross-post to it.
- **Matthew Sweet** — [@msmsim](https://github.com/msmsim). [msn](https://github.com/msmsim/msn),
  an independent client, publishing at [msweet.net/notes](https://www.msweet.net/notes/).
- **Protocols for Business** — [@protocolvision](https://github.com/protocolvision).
  The Protocol Institute research group's own static client,
  [sig-p4b](https://github.com/protocolvision/sig-p4b), publishing at
  [protocolsforbusiness.com/blyg](https://protocolsforbusiness.com/blyg/).
- **Russell Antonie Pasetes** — [@rpasetes](https://github.com/rpasetes).
  [blyxt](https://github.com/rpasetes/blyxt), a Telegram client: messages in a
  group topic publish as fragments, and another topic follows other blygs.
  Publishing at [rslantonie.com/blyg](https://rslantonie.com/blyg/).
- **ananth** — [@ananth1100](https://github.com/ananth1100).
  [blygger-reference-client](https://github.com/ananth1100/blygger-reference-client),
  a pure-stdlib Python client for 0.3, with a second, browser-only client that
  publishes to GitHub Pages.
- **Surya Kasturi** — [@ksurya](https://github.com/ksurya).
  [BlyggerPress](https://github.com/ksurya/blyggerpress), a local-first studio
  with pinned-spec contracts and its own conformance fixtures.
- **Ben Mayhew** — [@Allethrin](https://github.com/Allethrin). A blyg built
  into [benmayhew.com](https://github.com/Allethrin/benmayhew.com), at
  [benmayhew.com/blyg](https://benmayhew.com/blyg/).
- **Halcyonic Systems** — [@halcyonic-systems](https://github.com/halcyonic-systems).
  [blyg-watch](https://github.com/halcyonic-systems/blyg-watch), which watches
  the network as a system, measuring how concentrated it is by client and
  host, without publishing counts.
- **Florian Lohse** — [@florianlohse](https://github.com/florianlohse).
  Published at [florianlohse.com/blyg](https://florianlohse.com/blyg/) with a
  client of their own, `my-garden-site`, before moving to Blygger Studio at
  [blyg.florianlohse.com](https://blyg.florianlohse.com/).
- **Christopher Chalcraft** — [@cchalc](https://github.com/cchalc). His
  [Astro site](https://github.com/cchalc/site) emits a static blyg of its
  articles at [featherandwire.dev/blyg](https://featherandwire.dev/blyg/),
  beside a Blygger Studio for short posts.

### Clients known only by their blygs

These publish with clients of their own whose authors haven't been matched to
a profile yet. If one is yours, [say so](https://github.com/blygger/blygger-org/issues/new/choose).

- [thinking.drwip.com/blyg](https://thinking.drwip.com/blyg/) — the first
  independent implementation, before the September 2026 talk.
- [blyg.sachinbenny.xyz](https://blyg.sachinbenny.xyz/) — `sachin-blyg`.
- [artlu.xyz](https://artlu.xyz/) — `astro-gyoza`.
- [rafael.fyi/blyg](https://rafael.fyi/blyg/) — `rafael-fyi-blyg`, adapted
  from Protocols for Business's client.

</section>

</div>
