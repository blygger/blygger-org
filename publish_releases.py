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
  ./publish_releases.py --batch [...]     one thread for every version announced in this run,
                                          newest first; each version maps to that one item
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


def tag_date(version: str) -> str:
    """The tagged commit's date, for entries whose heading carries a title instead."""
    return subprocess.run(["git", "-C", str(STUDIO), "log", "-1", "--format=%cs", f"v{version}"],
                          capture_output=True, text=True, check=True).stdout.strip()


def sections() -> dict:
    """version -> (date, title, body) from CHANGELOG.md.

    Headings are `## X.Y.Z — YYYY-MM-DD` up to 0.49.6 and `## X.Y.Z — Title` since
    0.49.7. Matching only the dated form silently dropped every titled release
    (0.49.12–0.52.0, found session 59). A titled release's date is its tag's.
    """
    text = (STUDIO / "CHANGELOG.md").read_text("utf-8")
    parts = re.split(r"^## (\d+\.\d+\.\d+) — (.+?)\s*$", text, flags=re.M)
    out = {}
    for i in range(1, len(parts), 3):
        version, label, body = parts[i], parts[i + 1], parts[i + 2].strip().rstrip("-").strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", label):
            out[version] = (label, None, body)
        else:
            out[version] = (None, label, body)
    return out


def shipped(version: str, secs: dict, tags: set) -> str:
    """The body to announce: this version's section, plus the sections of any
    untagged versions it is the first release of, newest first. 0.49.12 shipped
    0.49.2–0.49.11 (never released on their own), whose sections carry migrations
    0034–0036; announcing 0.49.12's own section alone said "Migrations: none"
    (found session 59)."""
    earlier = [t for t in tags if vkey(t) < vkey(version)]
    floor = max(earlier, key=vkey) if earlier else None
    between = sorted((v for v in secs if vkey(v) < vkey(version) and v not in tags
                      and (floor is None or vkey(v) > vkey(floor))), key=vkey, reverse=True)
    body = secs[version][2]
    if not between:
        return body
    parts = [body, f"### Also in this release\n\n{version} is the first release since {floor}, so it also "
             f"ships {', '.join(between)}, which were never released on their own. Their notes follow; "
             "read their **Migrations** lines before upgrading."]
    for v in between:
        date, title, text = secs[v]
        parts.append(f"### {v} — {title or date}\n\n" + re.sub(r"^## ", "#### ", re.sub(r"^### ", "#### ", text, flags=re.M), flags=re.M))
    return "\n\n".join(parts)


def announcement(version: str, date: str, title: str | None, body: str, model: str) -> str:
    # The item is one impyrt scope, so a literal [TK] in the changelog reads as a
    # nested scope and publishing fails, even inside backticks (the nesting check
    # in blygger-studio src/tk.ts does not skip code spans; session 45).
    body = body.replace("[TK]", "TK")
    link = f"[v{version} on GitHub]({RELEASES}v{version})"
    name = f"Blygger Studio {version}" + (f": {title}" if title else "")
    head = f"# {name}\n\n*Released {date}, the reference client. {link}.*\n\n"
    foot = ("*This announcement is drafted from the release's section of "
            "[`CHANGELOG.md`](https://github.com/blygger/blygger-studio/blob/main/CHANGELOG.md), "
            "which is where it is maintained. To comment, respond to this item from your own blyg.*")
    return pb.wrap(model, head + body) + "\n\n" + pb.wrap(pb.FOOTER_MODEL, foot)


def batch_announcement(rows: list, model: str) -> str:
    """One thread for several releases (Venkat, session 61): newest first, each under
    its own heading with its date, its GitHub link and its whole section, Migrations
    line included, so an operator reading one post sees every upgrade step."""
    newest, oldest = rows[0][0], rows[-1][0]
    head = (f"# Blygger Studio {oldest} to {newest}\n\n*{len(rows)} releases of the reference client, "
            "newest first. Read each one's **Migrations** line before upgrading.*\n\n")
    parts = []
    for v, date, title, body in rows:
        body = body.replace("[TK]", "TK")
        body = re.sub(r"^## ", "#### ", re.sub(r"^### ", "#### ", body, flags=re.M), flags=re.M)
        parts.append(f"## {v}" + (f": {title}" if title else "") +
                     f"\n\n*Released {date}. [v{v} on GitHub]({RELEASES}v{v}).*\n\n{body}")
    foot = ("*This announcement is drafted from the releases' sections of "
            "[`CHANGELOG.md`](https://github.com/blygger/blygger-studio/blob/main/CHANGELOG.md), "
            "which is where they are maintained. To comment, respond to this item from your own blyg.*")
    return pb.wrap(model, head + "\n\n".join(parts)) + "\n\n" + pb.wrap(pb.FOOTER_MODEL, foot)


def main() -> None:
    args = sys.argv[1:]
    dry = "--dry-run" in args
    batch = "--batch" in args
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
    rows = []
    for v in versions:
        if v not in tags: print(f"{v}: not tagged in blygger-studio; skipped"); continue
        if v not in secs: print(f"{v}: no CHANGELOG section; skipped"); continue
        if v in done: print(f"{v}: already announced ({done[v]['id']})"); continue
        date, title, _ = secs[v]
        date = date or tag_date(v)
        body = shipped(v, secs, tags)
        if batch:
            rows.append((v, date, title, body))
            continue
        if dry: print(f"{v}: would announce ({len(body)} chars of changelog), released {date}" + (f", \"{title}\"" if title else "")); continue
        # Studio 0.49 (contract 5.0.0): camelCase bodies; publish names the observed revision.
        draft = blyg.api("POST", "/items", {"kind": "thread", "contentMd": announcement(v, date, title, body, model)})
        item = draft["id"]
        ver = blyg.api("POST", f"/items/{item}/publish", {"note": f"Studio {v} released.", "expectedRevision": draft["revision"]})["version"]
        done[v] = {"id": item, "version": ver, "source_sha256": hashlib.sha256(body.encode()).hexdigest()}
        MAP.write_text(json.dumps(entries, indent=2) + "\n")
        print(f"{v}: published v{ver} -> {pb.BASE}/t/{item}/")
    if batch and rows:
        rows.sort(key=lambda r: vkey(r[0]), reverse=True)
        names = ", ".join(r[0] for r in rows)
        content = batch_announcement(rows, model)
        if dry:
            print(f"batch: would announce {names} as one thread ({len(content)} chars)")
            return
        draft = blyg.api("POST", "/items", {"kind": "thread", "contentMd": content})
        item = draft["id"]
        ver = blyg.api("POST", f"/items/{item}/publish", {"note": f"Studio {rows[-1][0]} to {rows[0][0]} released.", "expectedRevision": draft["revision"]})["version"]
        for v, _, _, body in rows:
            done[v] = {"id": item, "version": ver, "source_sha256": hashlib.sha256(body.encode()).hexdigest(), "batch": [r[0] for r in rows]}
        MAP.write_text(json.dumps(entries, indent=2) + "\n")
        print(f"batch {names}: published v{ver} -> {pb.BASE}/t/{item}/")


if __name__ == "__main__":
    main()
