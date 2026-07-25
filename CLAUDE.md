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

Not yet built beyond this file, `README.md`, `.gitignore`, and `LICENSE`.

## Workflow Notes

- Git repo: `blygger/blygger-org` (public), branch `main`.
- Deployed to: `blygger.org` (not yet deployed).

## Status

See [`status.md`](status.md).
