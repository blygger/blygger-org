# blygger-org

> **Environment rules, keys & safety policies:** see [Code/CLAUDE.md](../../CLAUDE.md) — read before starting work.
> **Protocol spec + reference implementation:** [`../blygger-spec/`](../blygger-spec/) — read `blygger-spec/CLAUDE.md` and `blygger-spec/docs/` before touching anything that isn't purely presentational; this repo is a *client* of the protocol, not where protocol decisions get made.

The public face of the Blygger protocol at **blygger.org**: commons/spec-adjacent —
the namespace-URI domain and the published home of the normative spec (`/spec/`),
technical notes (`/notes/`) and the namespace page (`/ns/0.1`).

**It does not run a blyg, and is not a test node.** The session-6 scaffold said it
would be one of the two initial cross-client test instances; session 11 put those on
`venkateshrao.com/blyg/` and `blyg.protocol-institute.org` instead, and this site's
job settled into being the stable citable home of the normative text. The relevant
plan doc is [`blygger-spec/docs/spec-publishing-plan.md`](../blygger-spec/docs/spec-publishing-plan.md)
(executed sessions 11–12, 20), not `deploy-stub-sites-plan.md`.

## Stack

Static site: Python (`build.py` + `markdown` package) renders `content/*.md`
through `templates/page.html` into `dist/`, styled by `site.css`. Deployed to
Cloudflare Pages (project `blygger-org`) via `deploy.sh`. The `/blyg`
reference-client deployment (separate, `blygger-spec/worker`) is still per the
deployment plan doc — not built here.

## Structure

- `content/` — publishable site content (session 7): `overview.md` (landing-page
  protocol overview, canonical here); `spec/` (session 11, 2026-08-09 —
  **entirely generated**, see below). Publish mapping + source-of-truth rule:
  `content/README.md`.
- `templates/page.html`, `site.css` — shared page shell + stylesheet. Signature
  design element: a monospace "log rail" in the left margin turning each page's
  headings into a numbered index (real section numbers on the spec page,
  positional on the overview page) — echoes the protocol's own
  "your feed is the changelog" idea.
- `sync_spec.py` (session 11) — the only writer of `content/spec/`. Publishes
  the canonical spec from the sibling `../blygger-spec/docs/protocol-v0.1.md`
  checkout; also (re)generates `content/spec/index.md`, the version/snapshot
  table. Design doc: `blygger-spec/docs/spec-publishing-plan.md`.
- `build.py` — renders `content/` → `dist/` (gitignored); walks `content/spec/`
  recursively so it picks up the index page, each version's latest revision,
  and any dated snapshots without needing per-page edits. `deploy.sh`
  (gitignored; reads `CLOUDFLARE_API_TOKEN`/`CLOUDFLARE_ACCOUNT_ID` from
  `Code/.env.keys`, never hardcodes them) — runs `sync_spec.py` then
  `build.py` then `wrangler pages deploy`.

### Publishing a spec update

Day-to-day: edit `../blygger-spec/docs/protocol-v0.1.md`, commit + push there,
then from this repo run `./deploy.sh` (syncs latest, builds, deploys) — no
manual copying, ever.

Cutting a citable dated snapshot (a deliberate editorial act, not routine —
see `spec-publishing-plan.md` §2 "Snapshot policy"): from this repo,
`/opt/homebrew/bin/python3 sync_spec.py snapshot`. Requires a **clean,
pushed** `../blygger-spec` tree (refuses otherwise — a snapshot must
correspond to a real, citable commit). This creates + pushes a
`spec/0.1/YYYY-MM-DD` tag in `blygger-spec`, writes the immutable dated page,
regenerates latest's "Previous version" link, and regenerates the index —
then run `./deploy.sh --no-build` (or plain `./deploy.sh`) to publish it.

## Workflow Notes

- Git repo: `blygger/blygger-org` (public), branch `main`.
- Deployed to: Cloudflare Pages, live at both
  [blygger.org](https://blygger.org) and
  [blygger-org.pages.dev](https://blygger-org.pages.dev) — the custom domain's
  DNS record was added by hand and activated 2026-08-04 (see `status.md`).

## Status

See [`status.md`](status.md).
