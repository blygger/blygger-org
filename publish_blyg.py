#!/opt/homebrew/bin/python3
"""publish_blyg.py — publish blygger-spec's RFCs and technical notes to the
official blyg at https://blyg.blygger.org/ (decision #66).

The git file is the single source. Each file in the map is published as a thread
under Venkat's byline (the blyg's author setting), wrapped as one whole-item
`impyrt` span naming the model(s) that wrote it, so the item's `generated[]`
discloses it (#66 review (b)). A short footer, written by this script and
disclosed as such, links the canonical source. A changed file republishes as a
new version of the same item, never as a hand-edited copy.

The map lives in blygger-spec at docs/blyg-published.json: file -> item id,
model, whether to pin each published version (RFCs: the version under comment
is pinned), and the SHA-256 of the source last published.

Usage:
  ./publish_blyg.py              publish every entry whose source changed
  ./publish_blyg.py --create     only create drafts for entries without an id
  ./publish_blyg.py --dry-run    report what would change

Auth: the blyg's owner password, BLYG_BLYGGER_ORG_OWNER_PASSWORD in
Code/.env.keys. Stdlib only.
"""
import hashlib, http.cookiejar, json, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = HERE.parent / "blygger-spec"
MAP = SPEC / "docs" / "blyg-published.json"
KEYS = HERE.parent.parent / ".env.keys"
BASE = "https://blyg.blygger.org"
GITHUB = "https://github.com/blygger/blygger-spec/blob/main/"
FOOTER_MODEL = "claude-opus-5-5"  # wrote the footer template below


def wrap(model: str, text: str) -> str:
    return f"[TK]impyrt {model}=\n{text.strip()}\n[/TK]"


def footer(entry: dict) -> str:
    src = entry["file"]
    link = f"[`{src}`]({GITHUB}{src})"
    if entry.get("canonical"):
        return (f"*This note's canonical text is at [{entry['canonical'].removeprefix('https://')}]({entry['canonical']}), "
                f"and its source is {link} in blygger-spec. The page there is what the spec cites. "
                "To comment, respond to this item from your own blyg.*")
    return (f"*Source: {link} in blygger-spec, which is where revisions are made; each one is "
            "published here as a new version. To comment, respond to this item from your own blyg: "
            "a stub is a comment, a partial quote names the passage, and a fork of the pinned version "
            "is a counter-proposal.*")


def content(entry: dict) -> str:
    body = (SPEC / entry["file"]).read_text("utf-8")
    # No trailing newline: blygger-studio 0.34.0 renders a final impyrt scope
    # followed by a single newline as an inline span instead of a block.
    return wrap(entry["model"], body) + "\n\n" + wrap(FOOTER_MODEL, footer(entry))


class Blyg:
    def __init__(self):
        pw = next(l.split("=", 1)[1].strip() for l in KEYS.read_text().splitlines()
                  if l.startswith("BLYG_BLYGGER_ORG_OWNER_PASSWORD="))
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        # Cloudflare refuses Python's default User-Agent with a 403.
        self.h = {"Origin": BASE, "User-Agent": "blygger-org/publish_blyg.py"}
        self.op.open(urllib.request.Request(BASE + "/studio/login", headers=self.h,
                                            data=urllib.parse.urlencode({"password": pw}).encode()))

    def api(self, method: str, path: str, body=None):
        req = urllib.request.Request(BASE + "/api" + path, method=method,
                                     headers={**self.h, "Content-Type": "application/json"},
                                     data=None if body is None else json.dumps(body).encode())
        try:
            with self.op.open(req) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            sys.exit(f"{method} {path} -> {e.code}: {e.read().decode()[:500]}")


def main() -> None:
    create_only, dry = "--create" in sys.argv, "--dry-run" in sys.argv
    entries = json.loads(MAP.read_text())
    blyg = None if dry else Blyg()
    for e in entries["items"]:
        text = content(e)
        sha = hashlib.sha256((SPEC / e["file"]).read_bytes()).hexdigest()
        if not e.get("id"):
            if dry:
                print(f"{e['file']}: would create"); continue
            e["id"] = blyg.api("POST", "/items", {"kind": "thread", "content_md": text})["id"]
            print(f"{e['file']}: created draft {e['id']}")
        if create_only or e.get("source_sha256") == sha:
            continue
        if dry:
            print(f"{e['file']}: would publish"); continue
        blyg.api("PATCH", f"/items/{e['id']}", {"content_md": text})
        note = e["notes"]["first" if not e.get("version") else "revision"]
        v = blyg.api("POST", f"/items/{e['id']}/publish", {"note": note})["version"]
        if e.get("pin"):
            blyg.api("PUT", f"/items/{e['id']}/versions/{v}/pin")
        e.update(version=v, source_sha256=sha)
        print(f"{e['file']}: published v{v}{' (pinned)' if e.get('pin') else ''} -> {BASE}/t/{e['id']}/")
    if not dry:
        MAP.write_text(json.dumps(entries, indent=2) + "\n")


if __name__ == "__main__":
    main()
