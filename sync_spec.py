#!/usr/bin/env python3
"""
sync_spec.py — the only writer of content/spec/. Publishes the canonical spec
from the sibling blygger-spec checkout into this site's content tree.

Source of truth: ../blygger-spec/docs/protocol-v0.1.md. Never hand-edit files
under content/spec/ — edit canonical there and rerun this script.

Usage:
    /opt/homebrew/bin/python3 sync_spec.py            # latest mode (default)
    /opt/homebrew/bin/python3 sync_spec.py snapshot    # cut a dated snapshot
    /opt/homebrew/bin/python3 sync_spec.py snapshot --version 0.1

See docs/spec-publishing-plan.md (blygger-spec repo) for the full design.
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
SPEC_REPO = ROOT / ".." / "blygger-spec"
CONTENT_SPEC = ROOT / "content" / "spec"

# Flip a version's status here when it's declared stable/frozen — the only
# edit needed at that point. Keys are the versions this script knows how to
# publish; add an entry (and the matching CANONICAL_FILES mapping) when 0.2
# exists.
SPEC_VERSIONS = {
    "0.1": "DRAFT",
}
CANONICAL_FILES = {
    "0.1": SPEC_REPO / "docs" / "protocol-v0.1.md",
}

SITE_ORIGIN = "https://blygger.org"
GITHUB_REPO = "blygger/blygger-spec"
GITHUB_URL = f"https://github.com/{GITHUB_REPO}"

MARKER_BEGIN = "<!-- spec-links:begin -->"
MARKER_END = "<!-- spec-links:end -->"
BULLET_RE = re.compile(r"^- \*\*([^:]+):\*\*\s?(.*)$")


def run(*args: str, cwd: Path) -> str:
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()


def spec_repo_sha() -> str:
    return run("git", "rev-parse", "--short", "HEAD", cwd=SPEC_REPO)


def spec_repo_is_dirty() -> bool:
    return bool(run("git", "status", "--porcelain", cwd=SPEC_REPO))


def spec_repo_head_is_pushed() -> bool:
    try:
        local = run("git", "rev-parse", "HEAD", cwd=SPEC_REPO)
        upstream = run("git", "rev-parse", "@{u}", cwd=SPEC_REPO)
    except subprocess.CalledProcessError:
        return False
    return local == upstream


def existing_snapshots(version: str) -> list[str]:
    """Dated snapshot dirs for a version, ascending (oldest first). Stateless — derived by globbing."""
    version_dir = CONTENT_SPEC / version
    if not version_dir.is_dir():
        return []
    dates = [p.name for p in version_dir.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name)]
    return sorted(dates)


def rewrite_links_block(canonical_text: str, this_version_url: str, latest_url: str, previous_url: str | None) -> str:
    """Surgically replace This/Latest/Previous version bullets; pass every other bullet
    (XML namespace, Source of truth, Reference implementation, License, ...) through verbatim."""
    m = re.search(rf"{re.escape(MARKER_BEGIN)}\n(.*?)\n{re.escape(MARKER_END)}", canonical_text, re.DOTALL)
    if not m:
        sys.exit(f"ERROR: {MARKER_BEGIN} / {MARKER_END} markers not found in {CANONICAL_FILES['0.1']}")
    block_lines = m.group(1).splitlines()

    managed = {"This version", "Latest version", "Previous version"}
    passthrough = []
    for line in block_lines:
        bm = BULLET_RE.match(line)
        if bm and bm.group(1) in managed:
            continue  # canonical only ever defines "This version"; drop it, we rebuild it below
        passthrough.append(line)

    new_lines = [
        f"- **This version:** `{this_version_url}`",
        f"- **Latest version:** `{latest_url}`",
    ]
    if previous_url:
        new_lines.append(f"- **Previous version:** `{previous_url}`")
    new_lines.extend(passthrough)

    new_block = MARKER_BEGIN + "\n" + "\n".join(new_lines) + "\n" + MARKER_END
    start, end = m.span()
    return canonical_text[:start] + new_block + canonical_text[end:]


def banner(source: str) -> str:
    return (
        "<!--\n"
        "  GENERATED FILE — do not edit directly.\n"
        f"  Source: {source}\n"
        "  Regenerate: blygger-org/sync_spec.py (see docs/spec-publishing-plan.md)\n"
        "-->\n\n"
    )


def footer(sha: str) -> str:
    return f"\n\n---\n\n*Published from [{GITHUB_REPO}@{sha}]({GITHUB_URL}/commit/{sha}).*\n"


def render_spec_page(version: str, this_version_url: str, latest_url: str, previous_url: str | None) -> str:
    canonical_path = CANONICAL_FILES[version]
    if not canonical_path.is_file():
        sys.exit(f"ERROR: canonical spec not found at {canonical_path} (is blygger-spec checked out as a sibling of this repo?)")

    if spec_repo_is_dirty():
        print(f"WARNING: {SPEC_REPO} has uncommitted changes — publishing from a dirty tree.", file=sys.stderr)

    text = canonical_path.read_text("utf-8")
    text = rewrite_links_block(text, this_version_url, latest_url, previous_url)
    sha = spec_repo_sha()
    return banner("blygger-spec/docs/protocol-v0.1.md") + text.rstrip("\n") + footer(sha)


def sync_latest(version: str) -> None:
    latest_url = f"{SITE_ORIGIN}/spec/{version}/"
    snapshots = existing_snapshots(version)
    previous_url = f"{SITE_ORIGIN}/spec/{version}/{snapshots[-1]}/" if snapshots else None

    out_dir = CONTENT_SPEC / version
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.md"
    out_path.write_text(render_spec_page(version, latest_url, latest_url, previous_url), "utf-8")
    print(f"  wrote {out_path.relative_to(ROOT)}")


def cut_snapshot(version: str) -> None:
    if spec_repo_is_dirty():
        sys.exit(f"ERROR: {SPEC_REPO} has uncommitted changes — a snapshot must correspond to a pushed commit. Commit/push first.")
    if not spec_repo_head_is_pushed():
        sys.exit(f"ERROR: {SPEC_REPO}'s HEAD isn't pushed (or has no upstream) — a snapshot must correspond to a pushed commit. Push first.")

    date = datetime.now(timezone.utc).date().isoformat()
    snapshot_dir = CONTENT_SPEC / version / date
    if snapshot_dir.exists():
        sys.exit(f"ERROR: {snapshot_dir.relative_to(ROOT)} already exists — snapshots are immutable, refusing to overwrite.")

    snapshots = existing_snapshots(version)
    previous_url = f"{SITE_ORIGIN}/spec/{version}/{snapshots[-1]}/" if snapshots else None
    this_version_url = f"{SITE_ORIGIN}/spec/{version}/{date}/"
    latest_url = f"{SITE_ORIGIN}/spec/{version}/"

    sha = spec_repo_sha()
    tag = f"spec/{version}/{date}"
    existing_tag_sha = None
    try:
        existing_tag_sha = run("git", "rev-list", "-n", "1", tag, cwd=SPEC_REPO)
    except subprocess.CalledProcessError:
        pass
    head_full_sha = run("git", "rev-parse", "HEAD", cwd=SPEC_REPO)

    if existing_tag_sha and existing_tag_sha != head_full_sha:
        sys.exit(f"ERROR: tag {tag} already exists on a different commit ({existing_tag_sha[:7]} != {head_full_sha[:7]}).")
    elif existing_tag_sha:
        print(f"  tag {tag} already exists at HEAD — no-op.")
    else:
        run("git", "tag", tag, cwd=SPEC_REPO)
        run("git", "push", "origin", tag, cwd=SPEC_REPO)
        print(f"  created + pushed tag {tag}")

    snapshot_dir.mkdir(parents=True, exist_ok=True)
    (snapshot_dir / "index.md").write_text(render_spec_page(version, this_version_url, latest_url, previous_url), "utf-8")
    print(f"  wrote {(snapshot_dir / 'index.md').relative_to(ROOT)}")

    sync_latest(version)  # latest's Previous-version link now points at this snapshot


def build_spec_index() -> None:
    lines = [
        banner("derived from content/spec/ + blygger-spec tags").rstrip("\n"),
        "",
        "# Blygger Protocol — Specification Index",
        "",
        f"Source: [{GITHUB_REPO}]({GITHUB_URL})",
        "",
        "| Version | Status | Latest revision |",
        "|---|---|---|",
    ]
    for version, status in SPEC_VERSIONS.items():
        lines.append(f"| {version} | {status} | [/spec/{version}/](/spec/{version}/) |")

    for version in SPEC_VERSIONS:
        snapshots = existing_snapshots(version)  # ascending
        if not snapshots:
            continue
        lines.append("")
        lines.append(f"## {version} snapshots")
        lines.append("")
        for i, date in enumerate(reversed(snapshots)):  # newest first for display
            url = f"/spec/{version}/{date}/"
            row = f"- [{date}]({url})"
            older_idx = len(snapshots) - 1 - i - 1
            if older_idx >= 0:
                older = snapshots[older_idx]
                compare = f"{GITHUB_URL}/compare/spec/{version}/{older}...spec/{version}/{date}"
                row += f" — [diff since {older}]({compare})"
            lines.append(row)

    lines.append("")
    lines.append("## Reference implementation")
    lines.append("")
    try:
        ref_tags = run("git", "tag", "-l", "ref-v*", cwd=SPEC_REPO).splitlines()
    except subprocess.CalledProcessError:
        ref_tags = []
    if ref_tags:
        lines.append(f"Tagged releases: [{GITHUB_REPO}/releases]({GITHUB_URL}/releases/latest)")
    else:
        lines.append(
            "No reference-implementation release has been tagged yet "
            f"(will link to [{GITHUB_REPO}/releases]({GITHUB_URL}/releases) once `ref-v0.1.0` is cut)."
        )

    CONTENT_SPEC.mkdir(parents=True, exist_ok=True)
    out_path = CONTENT_SPEC / "index.md"
    out_path.write_text("\n".join(lines) + "\n", "utf-8")
    print(f"  wrote {out_path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", nargs="?", default="latest", choices=["latest", "snapshot"])
    parser.add_argument("--version", default="0.1", choices=list(SPEC_VERSIONS))
    args = parser.parse_args()

    if not SPEC_REPO.is_dir():
        sys.exit(f"ERROR: {SPEC_REPO.resolve()} not found — blygger-spec must be checked out as a sibling of blygger-org.")

    if args.mode == "snapshot":
        cut_snapshot(args.version)
    else:
        sync_latest(args.version)

    build_spec_index()


if __name__ == "__main__":
    main()
