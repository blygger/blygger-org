#!/opt/homebrew/bin/python3
"""publish_releases.py — announce blygger-studio releases on the official blyg
at https://blyg.blygger.org/ (decision #66, roadmap row 7).

One thread per release, built from that release's section of
blygger-studio/CHANGELOG.md. The changelog is the single source; the item is
published once and a release's announcement is never edited. Only versions that
have a git tag in blygger-studio are announced (a tag is what makes a release).
Third-party clients' releases are announced by hand on the blyg.

The map lives in blygger-spec at docs/blyg-releases.json: version -> item id,
published version, and the SHA-256 of the changelog section announced.

Usage:
  ./publish_releases.py                   announce tagged versions newer than the newest in the map
  ./publish_releases.py 0.35.1 0.36.0     announce exactly these (backfill; must be tagged)
  ./publish_releases.py --dry-run [...]   report what would be announced
  ./publish_releases.py --model ID        model credited in the item's generated[] (default below)

Auth and the Blyg client are shared with publish_blyg.py. Stdlib only.
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

import publish_blyg as pb

HERE = Path(__file__).resolve().parent
STUDIO = HERE.parent / "blygger-studio"
MAP = pb.SPEC / "docs" / "blyg-releases.json"
RELEASES = "https://github.com/blygger/blygger-studio/releases/tag/"
DEFAULT_MODEL = "claude-opus-5-5"


def vkey(v: str) -> tuple:
    return tuple(int(p) for p in v.split("."))


def tagged() -> set:
    out = subprocess.run(["git", "-C", str(STUDIO), "tag", "--list", "v*"], capture_output=True, text=True, check=True).stdout
    return {t[1:] for t in out.split() if re.fullmatch(r"v\d+\.\d+\.\d+", t)}


def sections() -> dict:
    """version -> (date, body) from CHANGELOG.md."""
    text = (STUDIO / "CHANGELOG.md").read_text("utf-8")
    parts = re.split(r"^## (\d+\.\d+\.\d+) — (\d{4}-\d{2}-\d{2})\s*$", text, flags=re.M)
    return {parts[i]: (parts[i + 1], parts[i + 2].strip().rstrip("-").strip()) for i in range(1, len(parts), 3)}


def announcement(version: str, date: str, body: str, model: str) -> str:
    link = f"[v{version} on GitHub]({RELEASES}v{version})"
    head = f"# Blygger Studio {version}\n\n*Released {date}, the reference client. {link}.*\n\n"
    foot = ("*This announcement is drafted from the release's section of "
            "[`CHANGELOG.md`](https://github.com/blygger/blygger-studio/blob/main/CHANGELOG.md), "
            "which is where it is maintained. To comment, respond to this item from your own blyg.*")
    return pb.wrap(model, head + body) + "\n\n" + pb.wrap(pb.FOOTER_MODEL, foot)


def main() -> None:
    args = sys.argv[1:]
    dry = "--dry-run" in args
    model = DEFAULT_MODEL
    if "--model" in args:
        i = args.index("--model"); model = args[i + 1]; del args[i:i + 2]
    wanted = [a for a in args if not a.startswith("--")]
    entries = json.loads(MAP.read_text()) if MAP.exists() else {"$note": "Map from blygger-studio release versions to their announcements on https://blyg.blygger.org/. Written by blygger-org/publish_releases.py.", "releases": {}}
    done = entries["releases"]
    secs, tags = sections(), tagged()
    if wanted:
        versions = wanted
    elif done:
        newest = max(done, key=vkey)
        versions = sorted((v for v in tags if vkey(v) > vkey(newest) and v in secs), key=vkey)
    else:
        sys.exit("map is empty: name the versions to announce (e.g. ./publish_releases.py 0.35.1)")
    blyg = None if dry else pb.Blyg()
    for v in versions:
        if v not in tags: print(f"{v}: not tagged in blygger-studio; skipped"); continue
        if v not in secs: print(f"{v}: no CHANGELOG section; skipped"); continue
        if v in done: print(f"{v}: already announced ({done[v]['id']})"); continue
        date, body = secs[v]
        if dry: print(f"{v}: would announce ({len(body)} chars of changelog)"); continue
        item = blyg.api("POST", "/items", {"kind": "thread", "content_md": announcement(v, date, body, model)})["id"]
        ver = blyg.api("POST", f"/items/{item}/publish", {"note": f"Studio {v} released."})["version"]
        done[v] = {"id": item, "version": ver, "source_sha256": hashlib.sha256(body.encode()).hexdigest()}
        MAP.write_text(json.dumps(entries, indent=2) + "\n")
        print(f"{v}: published v{ver} -> {pb.BASE}/t/{item}/")


if __name__ == "__main__":
    main()
