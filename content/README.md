# content/ — publishable pages for blygger.org

Source content for the blygger.org site, written session 7 (2026-08-03). The
site build/deploy mechanics are specced in
`blygger-spec/docs/deploy-stub-sites-plan.md` (not yet executed); until then
these are plain markdown awaiting a renderer.

## Publish mapping

| File | URL | Role |
|---|---|---|
| `overview.md` | `blygger.org/` (or `/protocol/`) | Human-readable high-level protocol overview — the landing-page content |
| `spec/0.1/index.md` | `blygger.org/spec/0.1/` | Protocol spec v0.1 (DRAFT), at its permanent versioned slug |

## Source-of-truth rule

`spec/0.1/index.md` is a **publish copy**. The canonical spec lives in
`blygger-spec/docs/protocol-v0.1.md` — all edits happen there and are copied
here at publish time; never edit the copy directly. While the spec is DRAFT
the copy tracks canonical; once v0.1 is declared stable, the copy at this slug
freezes (a new protocol version gets a new slug, e.g. `/spec/0.2/`).

`overview.md` is canonical *here* — it is site copy, not protocol doctrine; the
spec and `blygger-spec` docs win on any conflict.
