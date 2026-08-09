# content/ — publishable pages for blygger.org

Source content for the blygger.org site, written session 7 (2026-08-03).
`build.py` renders every `.md` here into `dist/`.

## Publish mapping

| File | URL | Role |
|---|---|---|
| `overview.md` | `blygger.org/` | Human-readable high-level protocol overview — the landing-page content |
| `spec/index.md` | `blygger.org/spec/` | Generated index of all spec versions + dated snapshots |
| `spec/{version}/index.md` | `blygger.org/spec/{version}/` | Generated: latest revision of that protocol version |
| `spec/{version}/{date}/index.md` | `blygger.org/spec/{version}/{date}/` | Generated: immutable dated snapshot |

## Source-of-truth rule

**Everything under `spec/` is generated — `sync_spec.py` is the only writer.
Hand-editing is prohibited** (session 11, 2026-08-09; retires the earlier
hand-copy convention). The canonical spec lives in
`../blygger-spec/docs/protocol-v0.1.md` — all edits happen there; run
`/opt/homebrew/bin/python3 sync_spec.py` (latest mode) or `sync_spec.py
snapshot` to republish. Every generated file carries a `GENERATED FILE — do
not edit directly` banner comment and a footer provenance stamp naming the
source commit. See `blygger-spec/docs/spec-publishing-plan.md` for the full
design and `../CLAUDE.md` for the day-to-day how-to.

`overview.md` is canonical *here* — it is site copy, not protocol doctrine; the
spec and `blygger-spec` docs win on any conflict.
