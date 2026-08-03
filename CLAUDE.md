# blygger-org

> **Environment rules, keys & safety policies:** see [Code/CLAUDE.md](../../CLAUDE.md) — read before starting work.
> **Protocol spec + reference implementation:** [`../blygger-spec/`](../blygger-spec/) — read `blygger-spec/CLAUDE.md` and `blygger-spec/docs/` before touching anything that isn't purely presentational; this repo is a *client* of the protocol, not where protocol decisions get made.

The public face of the Blygger protocol at **blygger.org**: commons/spec-adjacent —
the namespace-URI domain, protocol documentation for humans, and a live `/blygg`
deployment that doubles as one of the two initial cross-client test instances (the
other is [`../blygger-com/`](../blygger-com/)).

Scaffolded session 6 (2026-07-24), part of the brand-rename + scaffolding session
that also produced `blygger-spec` and `blygger-com`. **Deployment plan (stack,
content, /blygg wiring) lives in `blygger-spec/docs/deploy-stub-sites-plan.md`** —
read that before building anything here; nothing beyond this stub scaffold has
been built yet.

## Stack

TBD — see the deployment plan doc. Likely Cloudflare Pages/Workers to match
`blygger-spec`'s toolchain, but not yet decided.

## Structure

- `content/` — publishable site content (session 7): `overview.md` (landing-page
  protocol overview, canonical here), `spec/0.1/index.md` (publish copy of the
  DRAFT v0.1 spec — canonical lives in `blygger-spec/docs/protocol-v0.1.md`,
  never edit the copy). Publish mapping + source-of-truth rule: `content/README.md`.
- No renderer or deploy yet — that's the deployment plan's job.

## Workflow Notes

- Git repo: `blygger/blygger-org` (public), branch `main`.
- Deployed to: `blygger.org` (not yet deployed).

## Status

See [`status.md`](status.md).
