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
| 3 | Settings page reorganised into sections | studio | 5 | next |  |  |
| 55 | CI reliability and speed: parallel jobs, PR-scoped e2e and mutation suites, Release reusing main's green Check, one CI retry for e2e | studio | 5 | shipped: studio 0.41.1 (#67, #69) | Triage of 40 runs: the e2e flakes were mostly `compose-pwa:179` (fixed by #64); mutation failures were real catches. Split the auth-security worker half further only if it stays the floor. | [studio#67](https://github.com/blygger/blygger-studio/pull/67) |
| 4 | Custom theme with live preview, shareable as a file, plus a reading typeface | studio | 3 | shipped: studio 0.40.0 (#58) |  | [studio#38](https://github.com/blygger/blygger-studio/issues/38) |
| 5 | A footer link to blygger.org and a public Collections menu, each removable in settings | studio | 2 | next |  |  |
| 7 | Release announcements for every client on the official blyg | org | 3 | shipped: `publish_releases.py`; third-party clients by hand |  |  |
| 9 | Stub editor: choose the quoted passage in the preview | studio | 5 | next |  |  |
| 10 | Images resized in the browser before upload | studio | 5 | next |  |  |
| 13 | Templated surfaces (§16.6e) promoted to normative text | spec | 2 | ready: Soapbox confirmed 2026-10-07; Fable promotes with the 0.4 document (row 24) |  | [spec#2](https://github.com/blygger/blygger-spec/issues/2) |
| 14 | Technical note TN-2: identity practice | spec | 5 | next |  |  |
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
| 24 | The 0.4 spec document opened | spec | 8 | next: Fable opens it (G8 open) |  |  |
| 25 | Author-chosen text for `[[id]]` links (new syntax in posts) | spec | ? | needs ruling |  |  |
| 26 | Unicode on the wire: normalization and origin comparison | spec | 8 | needs ruling |  | [spec#6](https://github.com/blygger/blygger-spec/issues/6) |
| 27 | Open findings from the first conformance report (partial quotes, closure walk, watermark, required members, grammar edge cases) | spec | 8 | needs ruling |  | [spec#11](https://github.com/blygger/blygger-spec/pull/11) |
| 28 | In-page anchors (footnotes) in imported HTML | studio | 5 | waiting: discussion |  | [studio#39](https://github.com/blygger/blygger-studio/issues/39) |
| 29 | Public pages update immediately after owner changes (edge-cache purge) | studio | ? | waiting: discussion |  |  |
| 30 | AI spending caps: daily, weekly and monthly, in settings | studio | 8 | later |  |  |
| 31 | Discovery from references: quote-chain view, "responds to" walk, second-degree blogrolls | studio | 13 | later |  |  |
| 32 | Self-host template with `npm run upgrade` | studio | 20 | later |  |  |
| 33 | A "you are behind" notice per listed node | com | 5 | later |  |  |
| 34 | Passkey sign-in | studio | 13 | later |  | [studio#50](https://github.com/blygger/blygger-studio/issues/50) |
| 49 | Lineage glyph on reading entries, as an operator-compiled extension | studio | 3 | shipped: studio 0.40.0 |  | [studio#53](https://github.com/blygger/blygger-studio/pull/53) |
| 36 | Technical note TN-4: a write surface | spec | 5 | later |  |  |
| 37 | Reference agent and technical note TN-5: the contract between a blyg and an agent | spec | 40 | later |  |  |
| 38 | YouTube links embed on public pages; a failed off-origin image shows as a link | studio | 3 | shipped: studio 0.40.0 (#62) |  | [studio#9](https://github.com/blygger/blygger-studio/issues/9) |
| 39 | Author-sized inline images | studio | 3 | needs ruling | The size has to be written in the post, so this is new syntax other clients will meet. | [studio#37](https://github.com/blygger/blygger-studio/issues/37) |
| 40 | Pour-over links: paste a URL and bring the source into the draft | studio | 5 | later |  | [studio#17](https://github.com/blygger/blygger-studio/issues/17) |
| 41 | TK generation through the Workers AI binding, with no API key | studio | 5 | shipped: studio 0.40.0 (#60), with OpenAI-compatible endpoints |  | [studio#8](https://github.com/blygger/blygger-studio/issues/8) |
| 42 | Human-readable permalinks (`page` slugs) | studio | 8 | later |  | [studio#19](https://github.com/blygger/blygger-studio/issues/19) |
| 43 | A richer editor without a vendored dependency | studio | 13 | later |  | [studio#16](https://github.com/blygger/blygger-studio/issues/16) |
| 44 | Publishing patterns: six client affordances | studio | 20 | later | Probably splits into six rows once each is sized. | [studio#18](https://github.com/blygger/blygger-studio/issues/18) |
| 45 | Tangling: publish a thread and its fragments together | studio | 13 | needs ruling | Proposes new syntax in posts. | [studio#20](https://github.com/blygger/blygger-studio/issues/20) |
| 46 | Optional `cid` on pinned versions (IPFS mirror and pin log) | spec | 8 | needs ruling |  | [spec#13](https://github.com/blygger/blygger-spec/issues/13) |
| 48 | The official blyg at blyg.blygger.org, with RFCs and technical notes | org | 5 | shipped |  |  |
| 51 | A discard-draft control in plain view, not only in the ⋯ menu | studio | 2 | next |  | [studio#56](https://github.com/blygger/blygger-studio/issues/56) |
| 52 | Smart Feed: reading ordered by a scoring model the owner chooses | studio | ? | later | Which scoring models, and whether core or an extension. | [studio#57](https://github.com/blygger/blygger-studio/issues/57) |
| 54 | The MCP server registers behind Cloudflare's MCP portals | studio | ? | in review: [studio#66](https://github.com/blygger/blygger-studio/pull/66), waiting on Kyle's rebase onto #67 | Whether the portal error was this omitted-resource failure: Surya retries after it ships. | [studio#54](https://github.com/blygger/blygger-studio/issues/54) |
| 57 | Import subscriptions from an OPML file: client-side parse and preview, paced `createSubscription` calls with an optional `backfill: false` (cron backfills), folders flattened, out of the blogroll unless the owner ticks a box | studio | 5 | next | Aneesh builds it; shared with Blygger Desktop through `/api`. Folders as hoppers later. | [studio#63](https://github.com/blygger/blygger-studio/issues/63) |
| 58 | Duplicate-upload guard: an identical file uploaded to the same item returns the existing row (`media.sha256`, migration 0028) | studio | 2 | waiting: Aneesh's PR | Per-version attachments (§5.4, a studio fix with no wire change) is a separate, larger PR. | [studio#7](https://github.com/blygger/blygger-studio/issues/7) |
| 56 | `GET /api/capabilities`: the operations and extensions enabled on a node (OpenAPI stays the full contract, OAuth decides access); MCP `tools/list` drops disabled extensions' tools | studio | 3 | waiting: Kyle | Offered to Kyle, who designed the API; ours if he declines. | [studio#61](https://github.com/blygger/blygger-studio/pull/61#issuecomment-6103218858) |
| 59 | Studio error log: a local ring buffer of errors (message, stack, operation, item id, build, time), a "details" link on each banner, and "copy diagnostics" in Settings for pasting into an issue; nothing leaves the device. Then retry a browser-dropped request (Safari "cancelled") once before showing a banner | studio | 3 | next | Prompted by an intermittent "canceled" banner while editing on iPad Safari (session 46): message not produced by the studio or its libraries, so likely WebKit dropping a fetch. |  |
| 60 | Pace-layered home page: the diachronic view, beside newest first. Items sink as new ones arrive, slower the more they are pinned (pins on quoting items count, halved per hop), and climb one place per new version. Core and the fresh-install default; extensions can add further orders | studio | 8 | shipped: studio 0.42.0 | Changelog-driven climbing (a major revision climbs further) is stubbed in `climbFor()`. | [plan](https://github.com/blygger/blygger-studio/blob/main/docs/pace-layered-feed.md) |
| 61 | Setup walk-through: every setting, one step at a time, beside its default, with reset; greets a fresh install, re-runnable from Settings | studio | 5 | shipped: studio 0.42.0 |  |  |
| 62 | Pace-layered ordering recommended to other clients (RFC or technical note), with worked fixtures to check against | spec | 3 | needs ruling | Normative or illustrative constants; a `pinned_at` on changelog entries (the wire says which versions are pinned, not when); whether pins re-send mentions so inbound pins can count. |  |
| 63 | Bespoke builds: document and encourage n=1 blygs, built from the spec by their owner's own generator. Agentic coding makes a one-person site cheap, and this end of the ecosystem should flourish: a guide on blygger.org (the spec, the conformance toolkit, what a minimal L2 static blyg needs), and the ecosystem page's "Bespoke builds" section pointing to it | org | 3 | next | The section exists (session 46): Ben Mayhew's blyg, plus `msn`, `sig-p4b-blyg` and `cchalc-site` moved from Clients. What is left is the guide. |  |

---

*Published from [blygger/blygger-spec@3b843fb](https://github.com/blygger/blygger-spec/commit/3b843fb).*
