# blygger.org

The commons face of the [Blygger protocol](https://github.com/blygger/blygger-spec) —
an AI-native decentralized public writing medium (fragments + threads + TK-transclusion
over static files + RSS).

`blygger.org` is the protocol's namespace-URI domain and its public-facing spec/docs
home. It will also run a live `/blyg` deployment — one of the two initial
cross-client test instances (the other lives at [blygger.com](https://blygger.com),
[`blygger-com`](https://github.com/blygger/blygger-com)).

**Status: landing page live** at [blygger.org](https://blygger.org). The `/blyg`
reference-client deployment is not yet done. See
[`blygger-spec/docs/deploy-stub-sites-plan.md`](https://github.com/blygger/blygger-spec/blob/main/docs/deploy-stub-sites-plan.md)
for that plan.

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
