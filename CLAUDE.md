# blygger-org

> **Environment rules, keys & safety policies:** see [Code/CLAUDE.md](../../CLAUDE.md) — read before starting work.
> **Protocol spec + reference implementation:** [`../blygger-spec/`](../blygger-spec/) — read `blygger-spec/CLAUDE.md` and `blygger-spec/docs/` before touching anything that isn't purely presentational; this repo is a *client* of the protocol, not where protocol decisions get made.

The public face of the Blygger protocol at **blygger.org**: commons/spec-adjacent —
the namespace-URI domain, protocol documentation for humans, and a live `/blyg`
deployment that doubles as one of the two initial cross-client test instances (the
other is [`../blygger-com/`](../blygger-com/)).

Scaffolded session 6 (2026-07-24), part of the brand-rename + scaffolding session
that also produced `blygger-spec` and `blygger-com`. **Deployment plan (stack,
content, /blyg wiring) lives in `blygger-spec/docs/deploy-stub-sites-plan.md`** —
read that before building anything here; nothing beyond this stub scaffold has
been built yet.

## Stack

Static site: Python (`build.py` + `markdown` package) renders `content/*.md`
through `templates/page.html` into `dist/`, styled by `site.css`. Deployed to
Cloudflare Pages (project `blygger-org`) via `deploy.sh`. The `/blyg`
reference-client deployment (separate, `blygger-spec/worker`) is still per the
deployment plan doc — not built here.

## Structure

- `content/` — publishable site content (session 7): `overview.md` (landing-page
  protocol overview, canonical here), `spec/0.1/index.md` (publish copy of the
  DRAFT v0.1 spec — canonical lives in `blygger-spec/docs/protocol-v0.1.md`,
  never edit the copy). Publish mapping + source-of-truth rule: `content/README.md`.
- `templates/page.html`, `site.css` — shared page shell + stylesheet. Signature
  design element: a monospace "log rail" in the left margin turning each page's
  headings into a numbered index (real section numbers on the spec page,
  positional on the overview page) — echoes the protocol's own
  "your feed is the changelog" idea.
- `build.py` — renders `content/` → `dist/` (gitignored). `deploy.sh`
  (gitignored, holds the Cloudflare deploy token) — `wrangler pages deploy`.

## Workflow Notes

- Git repo: `blygger/blygger-org` (public), branch `main`.
- Deployed to: Cloudflare Pages, live at
  [blygger-org.pages.dev](https://blygger-org.pages.dev). Custom domain
  `blygger.org` registered against the Pages project but pending a manual DNS
  step — see `status.md`.

## Status

See [`status.md`](status.md).
