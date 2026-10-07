# Contributors

Blygger is built in public, by more people every week. This page credits
them in two groups. The first tab is for work on
the protocol itself and on the reference client, [Blygger
Studio](https://github.com/blygger/blygger-studio): pull requests, bug
reports, proposals. The second is for people building **their own** clients,
integrations and tools, which is how a protocol finds out whether it can
be implemented by anyone but its authors.

Everything here is drawn from the public record: pull requests and issues in
the [blygger](https://github.com/blygger) repositories, and the
[ecosystem index](/ecosystem/). If you are missing, or described wrongly,
[open an issue](https://github.com/blygger/blygger-org/issues/new/choose).

<div class="tabset" markdown="1">

<section class="tab-panel" data-tab="protocol" data-label="Protocol & reference client" markdown="1">

## Core contributors

### Venkatesh Rao — [@vgururao](https://github.com/vgururao)

Started the protocol. Author of the specification (0.1 through 0.3) and of
the decision log behind it; maintains Blygger Studio, this site, and the
[blygger.com](https://blygger.com) directory, and runs the first live node at
[venkateshrao.com/blyg/](https://venkateshrao.com/blyg/).

### Kyle Mathews — [@KyleAMathews](https://github.com/KyleAMathews)

The largest outside contribution to the reference client so far, most of it
architecture:

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
- In review: a 60-second public page cache
  ([#41](https://github.com/blygger/blygger-studio/pull/41)), Webmention
  delivery for long subscription origins
  ([#42](https://github.com/blygger/blygger-studio/pull/42)), and shared
  source schemas ([#43](https://github.com/blygger/blygger-studio/pull/43)).

Runs [blyg.bricolage.io](https://blyg.bricolage.io/).

### Aneesh Sathe — [@aneeshsathe](https://github.com/aneeshsathe)

The most thorough outside reader of the protocol so far, and the first to
test it systematically:

- **A conformance and intent toolkit**, with a first-round report
  ([blygger-spec#11](https://github.com/blygger/blygger-spec/pull/11), in
  review): every MUST, SHOULD and MAY in the 0.3 spec indexed, JSON Schemas
  for every document, a read-only crawler that checks the live network
  against the spec, and formal models of the rules that turned up gaps
  worth ruling on.
- **Twenty-three issues** across the spec and Studio, seventeen of them
  fixed: grammar edge cases in transclusion and generation scopes, importer
  and lineage bugs, and the question that made `[[id]]` links inert inside
  code ([blygger-spec#4](https://github.com/blygger/blygger-spec/issues/4)).
  A suggestion of Aneesh's put public hoppers on pages of their own (0.24.0).
- **Studio redesigned for the phone**
  ([#32](https://github.com/blygger/blygger-studio/pull/32),
  [#36](https://github.com/blygger/blygger-studio/pull/36); 0.22.0).
- A lineage glyph, hex view and action ring
  ([#35](https://github.com/blygger/blygger-studio/pull/35)), held as the
  first candidate for Studio's extension mechanism rather than the base
  client.

Also builds [blygger-desktop](https://github.com/aneeshsathe/blygger-desktop)
(see the ecosystem tab), and runs
[blyg.aneeshsathe.com](https://blyg.aneeshsathe.com/).

## Contributors

- **akash** — [@akashtattva](https://github.com/akashtattva). The mobile
  navigation and Contents drawer on this site
  ([blygger-org#1](https://github.com/blygger/blygger-org/pull/1)), and blyg
  feeds that strict RSS readers accept
  ([blygger-studio#33](https://github.com/blygger/blygger-studio/pull/33)).
- **Robert Peake** — [@cyberscribe](https://github.com/cyberscribe). Proposed
  that the manifest say where the rest of a blyg lives, so sites that cannot
  follow the file layout — WordPress, for one — can still publish one
  ([blygger-spec#2](https://github.com/blygger/blygger-spec/issues/2)). Ruled
  in as decision #51 and scheduled for 0.4.
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
  theme and reading typeface for Studio
  ([blygger-studio#38](https://github.com/blygger/blygger-studio/issues/38)).
- **Raynaud Simon** — [@keyral](https://github.com/keyral). Reported broken
  links in the spec's docs
  ([blygger-spec#3](https://github.com/blygger/blygger-spec/issues/3)).
- **djinna** — [@djinna](https://github.com/djinna). Asked for a way to size
  inline images
  ([blygger-studio#37](https://github.com/blygger/blygger-studio/issues/37)).

</section>

<section class="tab-panel" data-tab="ecosystem" data-label="Ecosystem" markdown="1">

## Ecosystem contributors

People building their own clients, integrations and tools rather than
working on ours. The [ecosystem page](/ecosystem/) indexes the projects and
the live blygs they serve.

- **Brady Dale** — [@BradyDale](https://github.com/BradyDale).
  [Blynger](https://github.com/BradyDale/Blynger), an independent client on
  its own version line, publishing at [bradydale.com/blyg](https://bradydale.com/blyg/).
- **Robert Peake** — [@cyberscribe](https://github.com/cyberscribe).
  Soapbox, a WordPress plugin that publishes a blyg, in progress — the first
  client built on the manifest-located surface proposed in blygger-spec#2.
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
  site, published at [newschematic.org/blyg](https://newschematic.org/blyg/).
- **Mike Travers** — [@mtravers](https://github.com/mtravers). Taught
  [goddinpotty](https://github.com/mtravers/goddinpotty), a digital-garden
  generator for Logseq graphs, to emit a blyg:
  [AMMDI](https://ammdi.hyperphor.com/blyg/).
- **Patrick Atwater** — [@patwater](https://github.com/patwater).
  [pioneering-spirit-blyg](https://github.com/patwater/pioneering-spirit-blyg),
  Blygger Studio extended to run [Pioneering Spirit](https://blyg.pioneeringspirit.xyz/)
  beside its old archive, and
  [a Windows port](https://github.com/patwater/burrow-blyg-windows-) of
  blygger-desktop.
- **Matthew Sweet** — [@msmsim](https://github.com/msmsim). [msn](https://github.com/msmsim/msn),
  an independent client, publishing at [msweet.net/notes](https://www.msweet.net/notes/).
- **Protocols for Business** — [@protocolvision](https://github.com/protocolvision).
  The Protocol Institute research group's own static client,
  [sig-p4b](https://github.com/protocolvision/sig-p4b), publishing at
  [protocolsforbusiness.com/blyg](https://protocolsforbusiness.com/blyg/).

### Clients we know only by their blygs

These publish with clients of their own whose authors we have not matched to
a profile. If one is yours, [tell us](https://github.com/blygger/blygger-org/issues/new/choose).

- [thinking.drwip.com/blyg](https://thinking.drwip.com/blyg/) — the first
  independent implementation, before the September 2026 talk.
- [blyg.sachinbenny.xyz](https://blyg.sachinbenny.xyz/) — `sachin-blyg`.
- [artlu.xyz](https://artlu.xyz/) — `astro-gyoza`.
- [florianlohse.com/blyg](https://florianlohse.com/blyg/) — `my-garden-site`.
- [rafael.fyi/blyg](https://rafael.fyi/blyg/) — `rafael-fyi-blyg`, adapted
  from Protocols for Business's client.

</section>

</div>
