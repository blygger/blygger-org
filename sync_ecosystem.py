#!/usr/bin/env /opt/homebrew/bin/python3
"""sync_ecosystem.py — the periodic check behind blygger.org/ecosystem/.

Writes `content/ecosystem/index.md` from three sources:

  1. `ecosystem/projects.toml`  — the curated list. Hand-edited, authoritative for
                                  *what is listed*. This script never adds to it.
  2. The live census            — every approved blyg in blygger.com's directory,
                                  fetched and read for its `generator` and `blyg`
                                  keys. This is the primary discovery mechanism:
                                  the manifest is public because the protocol
                                  requires it, so a client is visible as soon as
                                  someone publishes with it, whether or not its
                                  source is anywhere we can see.
  3. GitHub                     — repo metadata for entries that have a repo, plus
                                  a search sweep that reports repos not in the
                                  curated list.

Discovery, measured 2026-09-28: the census sees all 7 clients; GitHub search sees
9 repos but misses 5 of the 7 clients entirely, because their source is not on
GitHub; and **following forks sees nothing at all** — our three repos had zero
forks between them. People read the spec and write their own, or copy without
forking, so the fork graph is empty by construction. That is why the census is
primary and search is a supplement, and why a *tool* or a *mod* has to be
submitted: neither produces a manifest we can read.

`content/ecosystem/` is generated. `sync_ecosystem.py` is its only writer, the
same rule that governs `content/spec/` (see content/README.md).

Usage
  ./sync_ecosystem.py              refresh metadata, reuse cached summaries
  ./sync_ecosystem.py --summaries  also (re)generate summaries whose repo moved
  ./sync_ecosystem.py --offline    cache only, no network — for a build with no key
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tomllib
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CURATED = ROOT / "ecosystem" / "projects.toml"
CACHE = ROOT / "ecosystem" / "cache.json"
OUT = ROOT / "content" / "ecosystem" / "index.md"

DIRECTORY = "https://blygger.com"
USER_AGENT = "blygger-org-ecosystem/0.1.0 (+https://blygger.org)"
TIMEOUT = 20

# The client's current version is READ, never hand-kept. `projects.toml` carried
# it as a literal until 2026-09-28 and it drifted three releases behind: the page
# told five live nodes to upgrade to 0.4.0 while 0.7.0 was tagged. A known-latest
# that has to be remembered on every release is a known-latest that will be
# wrong, and wrong here is worse than absent — it is public advice to install an
# old build.
STUDIO_PKG = ROOT.parent / "blygger-studio" / "package.json"


def studio_generator() -> str | None:
    """`blygger-studio/<version>` from the sibling checkout's package.json."""
    try:
        version = json.loads(STUDIO_PKG.read_text("utf-8"))["version"]
    except (OSError, ValueError, KeyError):
        return None
    return f"blygger-studio/{version}"


def studio_released_generators() -> list[str]:
    """Every version this client has ever released, from its own git tags.

    Aliases matter for exactly the population the alert is for — nodes still on
    an old build — so a hand-kept list is the wrong shape for the same reason a
    hand-kept latest is: the entries you forget are the ones you needed.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(STUDIO_PKG.parent), "tag", "--list", "v*"],
            capture_output=True, text=True, timeout=10, check=True,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return []
    return [f"blygger-studio/{t.strip().lstrip('v')}" for t in out.splitlines() if t.strip()]


def current_generator(p: dict) -> str | None:
    """The version this project's operators should be on.

    Derived from the repo for our own client; the `projects.toml` literal is the
    fallback and is only authoritative for projects we do not build.
    """
    if p.get("ours") and p.get("repo") == "blygger/blygger-studio":
        return studio_generator() or p.get("generator")
    return p.get("generator")


def gen_keys(p: dict) -> list[str]:
    """Every `generator` string a project answers to, current and historical.

    Aliases are load-bearing, not cosmetic. When a client is renamed or bumped, the
    nodes in the wild keep reporting the OLD string until each operator upgrades —
    which is the whole reason the version-alert mechanism exists. Without aliases,
    a rename makes a project's own deployments look like an unidentified third
    client: after blyg-ref became blygger-studio, all five of our live nodes
    reported `blyg-ref/0.3.0` and were credited to nobody.
    """
    keys = []
    if p.get("generator"):
        keys.append(p["generator"])
    keys.extend(p.get("generator_aliases") or [])
    # Our own client answers to every version it has ever shipped, derived rather
    # than listed. Dedup preserves order: current first, history after.
    if p.get("ours") and p.get("repo") == "blygger/blygger-studio":
        keys.extend(studio_released_generators())
    return list(dict.fromkeys(keys))


def gen_base(g: str) -> str:
    """A generator's client name: `Blynger/0.9.31` -> `Blynger`,
    `thinking.drwip.com/1.0.0` -> `thinking.drwip.com`, and a parenthetical
    ignored. The join falls back to this so a version bump does not orphan a
    client — sachin-blyg and thinking.drwip.com both bumped and read as
    unidentified beside their own entries (session 38)."""
    return g.split(" ")[0].split("/")[0]


def project_nodes(p: dict, cen: dict) -> list[dict]:
    """Live nodes credited to a project: exact generator or alias first, then
    any generator with the same client name."""
    keys = gen_keys(p)
    bases = {gen_base(k) for k in keys}
    return [n for g, row in cen.items() if g in keys or gen_base(g) in bases
            for n in row["nodes"]]


def display_name(p: dict) -> str:
    """A human name. Falls back to the generator with its version stripped, since
    `Blynger/0.8.2` is a build identifier and `Blynger` is what to call it."""
    if p.get("name"):
        return p["name"]
    if p.get("repo"):
        return p["repo"].split("/")[-1]
    gen = p.get("generator") or ""
    return gen.rsplit("/", 1)[0] if "/" in gen else (gen or "—")


CATEGORY_ORDER = ["client", "integration", "tool", "mod", "reader", "library"]
CATEGORY_TITLE = {
    "client": "Clients",
    "integration": "Integrations",
    "tool": "Authoring tools",
    "mod": "Mods of Blygger Studio",
    "reader": "Readers and aggregators",
    "library": "Libraries and unclassified",
}
CATEGORY_BLURB = {
    "client": "Publish a blyg of their own, and so carry their own `generator` string. "
              "A client is discoverable the moment it publishes — this is the one "
              "category we can census without being told.",
    "integration": "Teach an existing publishing system — Hugo, Obsidian, a "
                   "note-taking tool — to emit a conformant blyg.",
    "tool": "Author *into* a blyg that already exists, rather than producing one. "
            "They carry no `generator`, so they are invisible to the census and are "
            "here because someone told us.",
    "mod": "Modified copies of the reference client. The hardest category to "
           "enumerate: our repos have no forks, so a mod announces itself nowhere "
           "unless its `generator` string changes or its author says so.",
    "reader": "Read blygs without publishing one.",
    "library": "Building blocks, and projects whose shape we have not yet confirmed "
               "with their author.",
}


def fetch(url: str, accept: str = "*/*") -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def gh(path: str) -> object | None:
    """GitHub API via the gh CLI, so it uses the operator's existing auth."""
    try:
        out = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=45)
        if out.returncode != 0:
            return None
        return json.loads(out.stdout)
    except Exception:
        return None


# ── The live census ────────────────────────────────────────────────────────────

def census() -> dict:
    """Read every blyg listed at blygger.com and report what client serves it.

    The directory page is the public list; we scrape its links rather than asking
    for a private API, because whatever a stranger can see is what this page
    should be built from.
    """
    status, html = fetch(DIRECTORY)
    if status != 200:
        print(f"  ! directory unreachable (HTTP {status}) — census skipped")
        return {}
    origins = sorted(set(re.findall(r'href="(https://[^"]+)"', html)))
    origins = [o for o in origins if "blygger.com" not in o and "blygger.org" not in o]

    seen: dict[str, dict] = {}
    for origin in origins:
        base = origin if origin.endswith("/") else origin + "/"
        st, body = fetch(base + "blyg.json", accept="application/json")
        if st != 200:
            continue
        try:
            m = json.loads(body)
        except Exception:
            continue
        if not isinstance(m, dict) or "blyg" not in m:
            continue
        gen = str(m.get("generator") or "(unnamed)")
        row = seen.setdefault(gen, {"generator": gen, "nodes": [], "protocols": set()})
        row["nodes"].append({"origin": base, "title": m.get("title"),
                             "protocol": m.get("blyg"), "updated": m.get("updated"),
                             "generator_seen": gen})
        row["protocols"].add(str(m.get("blyg")))
    for row in seen.values():
        row["protocols"] = sorted(row["protocols"])
        row["nodes"].sort(key=lambda n: n["origin"])
    print(f"  census: {len(seen)} client(s) across "
          f"{sum(len(r['nodes']) for r in seen.values())} live blyg(s)")
    return seen


# ── GitHub enrichment and discovery ────────────────────────────────────────────

def repo_meta(repo: str) -> dict | None:
    d = gh(f"repos/{repo}")
    if not isinstance(d, dict) or "full_name" not in d:
        return None
    return {
        "repo": d["full_name"],
        "description": d.get("description"),
        "language": d.get("language"),
        "license": ((d.get("license") or {}) or {}).get("spdx_id"),
        "stars": d.get("stargazers_count"),
        "forks": d.get("forks_count"),
        "pushed_at": d.get("pushed_at"),
        "created_at": d.get("created_at"),
        "archived": d.get("archived"),
        "homepage": d.get("homepage") or None,
        "topics": d.get("topics") or [],
        "default_branch": d.get("default_branch") or "main",
    }


def discover(known: set[str]) -> list[dict]:
    """Report repos we can find that are not in the curated list.

    Three queries with deliberately disjoint coverage. None of them is
    sufficient, and together they still miss any client whose source is not on
    GitHub — which is most of them.
    """
    found: dict[str, str] = {}
    queries = [
        ("topic:blygger", "search/repositories?q=topic:blygger&per_page=50"),
        ("name/desc/readme", "search/repositories?q=blygger+in:name,description,readme&per_page=50"),
        ("code: blyg.json", "search/code?q=blyg.json&per_page=30"),
    ]
    for label, path in queries:
        d = gh(path)
        if not isinstance(d, dict):
            print(f"  ! discovery query failed: {label}")
            continue
        for item in d.get("items", []):
            name = item.get("full_name") or (item.get("repository") or {}).get("full_name")
            if name and name not in known and not name.startswith("blygger/"):
                found.setdefault(name, label)
    return [{"repo": k, "via": v} for k, v in sorted(found.items())]


# ── Generated summaries ────────────────────────────────────────────────────────

SUMMARY_PROMPT = """You are writing one entry in a public directory of community projects
built on the Blygger protocol. Below is a project's README.

Write ONE sentence, at most 28 words, saying plainly what the project does and for whom.
Rules: no marketing adjectives; no "this project"; do not mention Blygger unless the
distinguishing fact is *how* it relates to Blygger; do not guess at anything the README
does not say; if the README is too thin to summarise, reply exactly NOT ENOUGH.

README:
---
{readme}
---
Sentence:"""


def generate_summary(repo: str, branch: str) -> str | None:
    """Summarise a repo's README with Claude. Optional: no key, no summary."""
    key = os.environ.get("AI_PROVIDER_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    readme = None
    for name in ("README.md", "readme.md", "README.markdown", "README"):
        st, body = fetch(f"https://raw.githubusercontent.com/{repo}/{branch}/{name}")
        if st == 200 and body.strip():
            readme = body[:12000]
            break
    if not readme:
        return None
    payload = json.dumps({
        "model": "claude-opus-5",
        "max_tokens": 200,
        "messages": [{"role": "user", "content": SUMMARY_PROMPT.format(readme=readme)}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=payload,
        headers={"content-type": "application/json", "x-api-key": key,
                 "anthropic-version": "2023-06-01"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        text = "".join(b.get("text", "") for b in d.get("content", [])).strip()
    except Exception as e:
        print(f"  ! summary failed for {repo}: {e}")
        return None
    if not text or "NOT ENOUGH" in text:
        return None
    return " ".join(text.split())


# ── Rendering ──────────────────────────────────────────────────────────────────

def md_text(s: str | None) -> str:
    """Escape what would break a markdown link label. One live blyg is titled
    "[jdbb] studio blyg", whose brackets turned its link into literal text."""
    if not s:
        return ""
    for ch in "[]":
        s = s.replace(ch, "\\" + ch)
    return s


def rel_age(iso: str | None) -> str:
    if not iso:
        return "—"
    try:
        then = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except Exception:
        return "—"
    days = (datetime.now(timezone.utc) - then).days
    if days <= 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    if days < 365:
        return f"{days // 30} month{'s' if days // 30 > 1 else ''} ago"
    return f"{days // 365} year{'s' if days // 365 > 1 else ''} ago"


def host_of(origin: str) -> str:
    return origin.split("//")[-1].rstrip("/")


def render(projects: list[dict], cen: dict, discovered: list[dict], generated_at: str) -> str:
    """A bare index: every known project, segmented by category, with links.

    Venkat, session 38: "a bare index without editorial commentary. Just a
    properly segmented list of all known projects with links to them." So no
    summaries, blurbs or counts — a name, where it lives, who made it, and the
    live blygs it serves. `summary` in projects.toml is no longer rendered.
    The version-drift signal this page used to print is reported on the
    console by main() instead, where the person running the sync sees it.
    """
    listed_bases = {gen_base(g) for p in projects for g in gen_keys(p)}
    uncredited = sorted(g for g in cen if gen_base(g) not in listed_bases)

    L: list[str] = []
    A = L.append
    A("<!-- GENERATED FILE — do not edit directly. Written by sync_ecosystem.py. -->")
    A("<!-- Curated source: ecosystem/projects.toml. Run ./sync_ecosystem.py to refresh. -->")
    A("")
    A("# The Blygger ecosystem")
    A("")
    A("Every known project that implements or extends Blygger. Listing is not "
      "endorsement. **[Add a project](https://github.com/blygger/blygger-org/issues/new/choose)**.")
    A("")

    for cat in CATEGORY_ORDER:
        group = [p for p in projects if p.get("category") == cat]
        if not group:
            continue
        A(f"## {CATEGORY_TITLE[cat]}")
        A("")
        group.sort(key=lambda p: (not p.get("ours"), display_name(p).lower()))
        for p in group:
            name = display_name(p)
            link = (f"https://github.com/{p['repo']}" if p.get("repo") else p.get("url") or p.get("live"))
            line = f"- **[{name}]({link})**" if link else f"- **{name}**"
            if p.get("repo"):
                owner = p["repo"].split("/")[0]
                line += f" — [@{owner}](https://github.com/{owner})"
            origins = sorted({n["origin"] for n in project_nodes(p, cen)})
            if not origins and p.get("live"):
                origins = [p["live"]]
            if p.get("retired"):
                line += " · retired"
            if origins:
                shown = origins[:3]
                line += " · live: " + ", ".join(f"[{host_of(o)}]({o})" for o in shown)
                if len(origins) > len(shown):
                    line += f" and {len(origins) - len(shown)} more"
            A(line)
        A("")

    if uncredited:
        A("## Unidentified clients")
        A("")
        for g in uncredited:
            nodes = cen[g]["nodes"]
            A(f"- `{g}` · live: " + ", ".join(f"[{host_of(n['origin'])}]({n['origin']})"
                                              for n in nodes[:3]))
        A("")

    if discovered:
        A("<!-- Discovered on GitHub and NOT in ecosystem/projects.toml. Triage these,")
        A("     then add or deliberately skip each one:")
        for d in discovered:
            A(f"       {d['repo']}  (via {d['via']})")
        A("-->")
        A("")

    A("---")
    A("")
    A(f"*Checked {generated_at}.*")
    return "\n".join(L) + "\n"


def report_drift(projects: list[dict], cen: dict) -> None:
    """Live nodes running an older build than their project's current one — the
    version-alert signal (roadmap-tracks 3.1). It used to be printed on the
    public page; it is operator information, so it goes to the console."""
    for p in projects:
        current = current_generator(p)
        if not current:
            continue
        nodes = project_nodes(p, cen)
        behind = [n for n in nodes if n.get("generator_seen") and n["generator_seen"] != current]
        if behind:
            print(f"  ~ {display_name(p)}: {len(behind)} of {len(nodes)} live node(s) behind {current}: "
                  + ", ".join(f"{host_of(n['origin'])} ({n['generator_seen']})" for n in behind))


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> int:
    offline = "--offline" in sys.argv
    do_summaries = "--summaries" in sys.argv

    data = tomllib.load(CURATED.open("rb"))
    curated = data.get("project", [])
    skipped = set(data.get("skip", []))
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    repo_cache = cache.get("repos", {})
    summary_cache = cache.get("summaries", {})

    print(f"Syncing ecosystem ({len(curated)} curated projects)"
          + (" [offline]" if offline else ""))

    cen = cache.get("census", {}) if offline else census()
    if offline:
        for r in cen.values():
            r.setdefault("nodes", [])

    projects = []
    for entry in curated:
        p = dict(entry)
        repo = p.get("repo")
        if repo:
            meta = None if offline else repo_meta(repo)
            if meta is None:
                meta = repo_cache.get(repo)
                if meta and not offline:
                    print(f"  ! {repo}: metadata unavailable, using cache")
            else:
                repo_cache[repo] = meta
            p["meta"] = meta or {}
            if not p.get("summary") and not (meta or {}).get("description"):
                cached = summary_cache.get(repo)
                stale = cached and cached.get("pushed_at") != (meta or {}).get("pushed_at")
                if not offline and (do_summaries or not cached or stale):
                    s = generate_summary(repo, (meta or {}).get("default_branch", "main"))
                    if s:
                        summary_cache[repo] = {"text": s, "pushed_at": (meta or {}).get("pushed_at")}
                        cached = summary_cache[repo]
                        print(f"  summarised {repo}")
                if cached:
                    p["generated_summary"] = cached["text"]
        projects.append(p)

    known = {p["repo"] for p in curated if p.get("repo")} | skipped
    # Offline reuses the cached discovery list rather than dropping it: the triage
    # comment it produces is the only record that an uncurated repo was ever seen.
    discovered = cache.get("discovered", []) if offline else discover(known)
    discovered = [d for d in discovered if d["repo"] not in known]
    if discovered:
        print(f"  ! {len(discovered)} repo(s) found and NOT curated:")
        for d in discovered:
            print(f"      {d['repo']}  (via {d['via']})")

    report_drift(projects, cen)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(projects, cen, discovered, generated_at))
    print(f"  wrote {OUT.relative_to(ROOT)}")

    CACHE.write_text(json.dumps(
        {"checked": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "census": cen, "repos": repo_cache, "summaries": summary_cache,
         "discovered": discovered}, indent=1, default=list) + "\n")
    print(f"  wrote {CACHE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
