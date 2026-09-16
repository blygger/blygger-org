# blygger.org

The commons face of the [Blygger protocol](https://github.com/blygger/blygger-spec) —
an AI-native decentralized public writing medium (fragments + threads + TK-transclusion
over static files + RSS).

`blygger.org` is the protocol's namespace-URI domain and its public-facing spec/docs
home: the normative spec at `/spec/`, technical notes at `/notes/`, and the namespace
page at `/ns/0.1`.

**Status: live** at [blygger.org](https://blygger.org), publishing the spec via
`sync_spec.py`. It does **not** run a blyg. The two live test nodes went elsewhere in
session 11 — `venkateshrao.com/blyg/` and `blyg.protocol-institute.org` — because
`blygger.org`'s job is to be the stable, citable home of the normative text, which is a
different job from being a test deployment.

## Build & deploy

Static site generated from `content/*.md` via `build.py` (Python + `markdown`),
templated by `templates/page.html`, styled by `site.css`. Deployed to Cloudflare
Pages (project `blygger-org`) via `deploy.sh` (gitignored — holds the deploy
token; see `Code/.env.keys`).

```bash
/opt/homebrew/bin/python3 build.py   # render content/ -> dist/
./deploy.sh                          # build + wrangler pages deploy
```

## License

[MIT](LICENSE).
