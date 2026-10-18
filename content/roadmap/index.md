<!--
  GENERATED FILE — do not edit directly.
  Source: blygger-spec/ROADMAP.md
  Regenerate: blygger-org/sync_spec.py (see docs/spec-publishing-plan.md)
-->

# Blygger roadmap

What is being worked on across the four Blygger repositories, in priority
order: the top of the list is next. It is one list on purpose. Discussion
happens on the linked issues, and this file only says where each item stands.

- **Area** is the repository: `spec` ([blygger-spec](https://github.com/blygger/blygger-spec)),
  `studio` ([blygger-studio](https://github.com/blygger/blygger-studio), the reference client),
  `org` ([blygger-org](https://github.com/blygger/blygger-org), blygger.org and the official
  blyg) or `com` ([blygger-com](https://github.com/blygger/blygger-com), the blygger.com directory).
- **Est** is relative effort in planning-poker points (1, 2, 3, 5, 8, 13, 20, 40),
  not hours. `?` means it cannot be sized until a question is answered.
- **Status**: `next` (up soon), `later`, `in review` (a contribution is waiting
  for review), `waiting` (on a person or a date, named in the row), `needs ruling`
  (a protocol question decided before any build), `shipped` (with the version;
  shipped rows drop off after a release or two, and the changelogs are the
  permanent record).
- **Open question** is anything to settle before the work starts. It is
  answered when the item is picked up, not in advance.

**To propose something,** open an issue on the repository it belongs to; the
issue templates say which. An issue that is accepted gets a row here linking
to it, and the issue stays open for discussion until the work ships. Protocol
proposals are decided against the spec's rules first. The spec's version ladder
is a different document: [docs/roadmap.md](https://github.com/blygger/blygger-spec/blob/main/docs/roadmap.md).

| # | Item | Area | Est | Status | Open question | Link |
|---|---|---|---|---|---|---|
| 3 | Settings page reorganised into sections: one page with a sidebar of anchors (General, Feed, Appearance, Links, AI, Network), each AI function's model beside its instructions | studio | 5 | shipped: studio 0.46.0 |  |  |
| 5 | A links section on every public page, below the content or as a left or right sidebar: chosen threads, public collections, the owner's own links, and links to the blogroll OPML, blygger.org and blygger.com, each removable in settings | studio | 5 | shipped: studio 0.44.0 | Grew from "a footer link to blygger.org and a public Collections menu" (session 47). |  |
| 9 | Stub editor: choose the quoted passage in the preview | studio | 5 | next |  |  |
| 10 | Images resized in the browser before upload | studio | 5 | next |  |  |
| 13 | Templated surfaces (§16.6e) promoted to normative text | spec | 2 | shipped: spec 0.4 (§4, §5.8, §6.1, §12, §15.3–15.4; session 49) |  | [spec#2](https://github.com/blygger/blygger-spec/issues/2) |
| 14 | Technical note TN-2: identity practice | spec | 5 | next |  |  |
| 64 | Owner API under the mount: serve REST at `{mount}/api` and advertise only that; `/api` stays as an alias for two releases, OAuth accepts both resource identifiers meanwhile, root-mounted nodes unchanged. A mounted blyg then needs one route, `{host}/{mount}*` | studio | 5 | next | Whether the owner cookie can then be scoped to `{mount}` on shared domains (check its current `Path` first). `/api` at the host root was an accident of route ordering in session 11, not a design choice. | [studio#70](https://github.com/blygger/blygger-studio/issues/70) |
| 65 | Static front page: a published thread at the mount root, as WordPress does; the latest items at `{mount}/posts/` (address settable, reserved names refused); set from Settings or a thread's ⋯ menu; a withdrawn front page falls back to the latest items | studio | 8 | shipped: studio 0.43.0 | Decision #69 (canonical to the root), Fable review pending. |  |
| 66 | `[[id \| text]]`: a `[[id]]` link or `![[id]]` directive with an author's label after the id | spec, studio | 3 | ruled: decision #70 (session 49); next: studio build | Ruled id-first, the double-bracket order of MediaWiki and Obsidian (`[[target\|label]]`), under decision #71: received conventions trump cosmetic preference. On a link the label is the anchor text; on a directive a comment. Studio: the three bracket regexes, the palette, *copy ID* emits the long form. Row 25 merged here. | [spec#16](https://github.com/blygger/blygger-spec/issues/16) |
| 67 | Links written by [TK] generation come out as literal brackets: a generated paragraph ending `![[id]]` published as raw text ([example](https://venkateshrao.com/blyg/t/4tsyw2ccaps3h0w1dveqc1f35x/)) | studio | 3 | next | Settled (session 49, Fable): keep generation from emitting the grammar — prompt + strip. Generated text is not grammar (studio#5, #60). No ruling needed for the build. |  |
| 68 | Links section: optionally list each blogroll entry as its own link, beside the OPML file | studio | 2 | next | A checkbox in Settings → links section, off by default. The home page's "Also reading" already lists them there. |  |
| 69 | Reading view order: newest first or pace-layered, as a setting, like the home page | studio | 8 | next | Pace-layered reads only wire data (changelog, pins, quotes), so it can order subscriptions' items too; it needs their version histories from the imported changelog, and inbound weight across blygs waits on whether pins re-send mentions (Fable queue item 16). |  |
| 70 | The owner's own posts in hoppers, beside what they read, shown on public hopper pages | studio | 3 | shipped: studio 0.45.0 | Membership uses the subscription marker `~own`; no migration. |  |
| 71 | Autosave disabled publish and save draft while typing (reported by Venkat) | studio | 2 | shipped: studio 0.45.0 |  |  |
| 72 | Publishing took up to a minute to show on public pages: the edge cache (studio#41) served the old copy and reloads validated against it (reported by Venkat) | studio | 2 | shipped: studio 0.46.1 | Cache key carries the public `change_state` revision. Hiding an inbound mention still waits out the 60 s: `mentions_in` has no change domain. |  |
| 73 | Editor toolbar buttons had no hover text (reported by Ned Twigg) | studio | 1 | shipped: studio 0.46.3 |  | [studio#48](https://github.com/blygger/blygger-studio/issues/48) |
| 74 | The `oauth-interop` CI job puts GitLab, Docker Hub and npm on the release path (its pinned conformance images vanished and blocked v0.46.2) | studio | 1 | waiting: Kyle | Own workflow out of the release path, scoped in Check, as is, or mirrored to GHCR. | [studio#73](https://github.com/blygger/blygger-studio/issues/73) |
| 15 | Full backup: download the whole blyg, every version and file, as one archive | studio | 5 | later |  |  |
| 53 | Restore a full backup into a fresh node | studio | 8 | later | Waits on row 15. |  |
| 16 | Mentions as a reading and discovery channel: read responses inline, subscribe in one click | studio | 13 | later |  |  |
| 17 | Opt-in blygger.com from the studio: list this blyg, and browse the directory with one-click subscribe | studio | 8 | later |  |  |
| 18 | Owner password change and reset in settings; recovery by a one-time code, or a new `OWNER_PASSWORD` secret as the last resort | studio | 8 | later |  |  |
| 19 | RFC-1 and RFC-2 comment periods | spec | – | waiting: closes 2026-11-04 |  | [spec#14](https://github.com/blygger/blygger-spec/issues/14), [#15](https://github.com/blygger/blygger-spec/issues/15) |
| 20 | RFC-1 in the studio: address book, @-mentions, member bylines | studio | 20 | waiting: RFC-1 closes |  | [spec#14](https://github.com/blygger/blygger-spec/issues/14) |
| 21 | Conformance and intent toolkit merged | spec | 3 | in review: intent ledger corrected, merging |  | [spec#11](https://github.com/blygger/blygger-spec/pull/11) |
| 22 | The directory runs the conformance toolkit daily | com | 8 | waiting: spec#11 |  | [com#1](https://github.com/blygger/blygger-com/issues/1) |
| 23 | Remote generation sources: generation that draws on another blyg's items, with a `source` mention | studio | 20 | shipped: studio 0.41.0; exercised PI → venkateshrao 2026-10-10 (G8 open) |  |  |
| 24 | The 0.4 spec document opened | spec | 8 | shipped: spec 0.4 opened 2026-10-17 (decision #72); 0.3 superseded |  |  |
| 26 | Unicode on the wire: normalization and origin comparison | spec | 8 | needs ruling |  | [spec#6](https://github.com/blygger/blygger-spec/issues/6) |
| 27 | Open findings from the first conformance report (partial quotes, closure walk, watermark, required members, grammar edge cases) | spec | 8 | needs ruling |  | [spec#11](https://github.com/blygger/blygger-spec/pull/11) |
| 28 | In-page anchors (footnotes) in imported HTML | studio | 5 | waiting: discussion |  | [studio#39](https://github.com/blygger/blygger-studio/issues/39) |
| 29 | Public pages update immediately after owner changes (edge-cache purge) | studio | ? | waiting: discussion |  |  |
| 30 | AI spending caps: daily, weekly and monthly, in settings | studio | 8 | later |  |  |
| 31 | Discovery from references: quote-chain view, "responds to" walk, second-degree blogrolls | studio | 13 | later |  |  |
| 32 | Self-host template with `npm run upgrade` | studio | 20 | later |  |  |
| 33 | A "you are behind" notice per listed node | com | 5 | later |  |  |
| 34 | Passkey sign-in | studio | 13 | later |  | [studio#50](https://github.com/blygger/blygger-studio/issues/50) |
| 36 | Technical note TN-4: a write surface | spec | 5 | later |  |  |
| 37 | Reference agent and technical note TN-5: the contract between a blyg and an agent | spec | 40 | later |  |  |
| 39 | Author-sized inline images | studio | 3 | ruled: decision #75 (spec 0.4 §16.10); next: studio build | Pandoc's attribute form after the image, `{width=33%}` / `{height=…}`, integer pixels or percent, baked onto the `<img>`. A stylesheet max-height needs no ruling. | [studio#37](https://github.com/blygger/blygger-studio/issues/37) |
| 40 | Pour-over links: paste a URL and bring the source into the draft | studio | 5 | later |  | [studio#17](https://github.com/blygger/blygger-studio/issues/17) |
| 42 | Human-readable permalinks (`page` slugs) | studio | 8 | later |  | [studio#19](https://github.com/blygger/blygger-studio/issues/19) |
| 43 | A richer editor without a vendored dependency | studio | 13 | later |  | [studio#16](https://github.com/blygger/blygger-studio/issues/16) |
| 44 | Publishing patterns: six client affordances | studio | 20 | later | Probably splits into six rows once each is sized. | [studio#18](https://github.com/blygger/blygger-studio/issues/18) |
| 45 | Tangling: publish a thread and its fragments together | studio | 13 | later | Protocol side settled (session 49, decision #70): no construct; a client-private bracket form is rewritten before publish and never reaches the wire. Open for the studio: the spelling (Fable recommends not `[[text]]`, since a forgotten id would mint a fragment whose content is the label), the feed-flood cap, and whether the studio should carry it at all. | [studio#20](https://github.com/blygger/blygger-studio/issues/20) |
| 46 | Optional `cid` on pinned versions (IPFS mirror and pin log) | spec | 8 | ruled: decision #74 (spec 0.4 §16.9); waiting: a client that emits it | The CID names the pinned document's bytes, not a bundle; mirroring pinned bytes is retention. CID profile and pin log are a technical note. | [spec#13](https://github.com/blygger/blygger-spec/issues/13) |
| 51 | A discard-draft control in plain view, not only in the ⋯ menu | studio | 2 | next |  | [studio#56](https://github.com/blygger/blygger-studio/issues/56) |
| 52 | Smart Feed: reading ordered by a scoring model the owner chooses | studio | ? | later | Which scoring models, and whether core or an extension. Motivating case (Surya, session 49): rank subscriptions by how they relate to the owner's own writing, on a fast cheap model of its own. | [studio#57](https://github.com/blygger/blygger-studio/issues/57) |
| 54 | The MCP server registers behind Cloudflare's MCP portals | studio | ? | waiting: Surya retries on 0.46.3 ([studio#66](https://github.com/blygger/blygger-studio/pull/66) shipped: omitted `resource` defaults to MCP) | Whether the portal error was this omitted-resource failure. | [studio#54](https://github.com/blygger/blygger-studio/issues/54) |
| 57 | Import subscriptions from an OPML file: client-side parse and preview, paced `createSubscription` calls with an optional `backfill: false` (cron backfills), folders flattened, out of the blogroll unless the owner ticks a box | studio | 5 | next | Aneesh builds it; shared with Blygger Desktop through `/api`. Folders as hoppers later. | [studio#63](https://github.com/blygger/blygger-studio/issues/63) |
| 58 | Duplicate-upload guard: an identical file uploaded to the same item returns the existing row (`media.sha256`, migration 0028) | studio | 2 | waiting: Aneesh's PR | Per-version attachments (§5.4, a studio fix with no wire change) is a separate, larger PR. | [studio#7](https://github.com/blygger/blygger-studio/issues/7) |
| 56 | `GET /api/capabilities`: the operations and extensions enabled on a node (OpenAPI stays the full contract, OAuth decides access); MCP `tools/list` drops disabled extensions' tools | studio | 3 | waiting: Kyle | Offered to Kyle, who designed the API; ours if he declines. | [studio#61](https://github.com/blygger/blygger-studio/pull/61#issuecomment-6103218858) |
| 59 | Studio error log: a local ring buffer of errors (message, stack, operation, item id, build, time), a "details" link on each banner, and "copy diagnostics" in Settings for pasting into an issue; nothing leaves the device. | studio | 3 | next | Prompted by an intermittent banner while editing on iPad Safari (session 46). The banner read `CancelledError` (misreported as "canceled"): TanStack cancellations reaching the banner, fixed by Kyle's [studio#71](https://github.com/blygger/blygger-studio/pull/71) (merged session 47, ships next release). The planned retry of browser-dropped requests is dropped; the log stays useful for the next intermittent bug. |  |
| 60 | Pace-layered home page: the diachronic view, beside newest first. Items sink as new ones arrive, slower the more they are pinned (pins on quoting items count, halved per hop), and climb one place per new version. Core and the fresh-install default; extensions can add further orders | studio | 8 | shipped: studio 0.42.0 | Changelog-driven climbing (a major revision climbs further) is stubbed in `climbFor()`. | [plan](https://github.com/blygger/blygger-studio/blob/main/docs/pace-layered-feed.md) |
| 61 | Setup walk-through: every setting, one step at a time, beside its default, with reset; greets a fresh install, re-runnable from Settings | studio | 5 | shipped: studio 0.42.0 |  |  |
| 62 | Pace-layered ordering recommended to other clients (RFC-3), with worked fixtures to check against | spec | 3 | ruled: decision #73; next: Opus drafts RFC-3, Fable edits, publishes on blyg.blygger.org | Constants are reference values. `pinned_at` on pinned changelog entries is a ruled shape (§16.9) the studio can emit now. |  |
| 63 | Bespoke builds: document and encourage n=1 blygs, built from the spec by their owner's own generator. Agentic coding makes a one-person site cheap, and this end of the ecosystem should flourish: a guide on blygger.org (the spec, the conformance toolkit, what a minimal L2 static blyg needs), and the ecosystem page's "Bespoke builds" section pointing to it | org | 3 | next | The section exists (session 46): Ben Mayhew's blyg, plus `msn`, `sig-p4b-blyg` and `cchalc-site` moved from Clients. What is left is the guide. |  |

---

*Published from [blygger/blygger-spec@4c03351](https://github.com/blygger/blygger-spec/commit/4c03351).*
