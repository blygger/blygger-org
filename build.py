#!/usr/bin/env python3
"""
build.py — render content/*.md into dist/ static HTML via templates/page.html.

Install once:
    /opt/homebrew/bin/python3 -m pip install markdown --break-system-packages

Usage:
    /opt/homebrew/bin/python3 build.py
"""

import re
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("markdown not installed.\nRun: /opt/homebrew/bin/python3 -m pip install markdown --break-system-packages")

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
TEMPLATE = (ROOT / "templates" / "page.html").read_text("utf-8")
EXTENSIONS = ["extra", "toc", "sane_lists"]


def flatten_h2(tokens):
    out = []
    for tok in tokens:
        if tok["level"] == 2:
            out.append(tok)
        out.extend(flatten_h2(tok["children"]))
    return out


def render_markdown(md_path: Path):
    md = markdown.Markdown(extensions=EXTENSIONS, extension_configs={"toc": {"permalink": False}})
    content_html = md.convert(md_path.read_text("utf-8"))
    return content_html, flatten_h2(md.toc_tokens)


def rail_items(tokens, numbered: bool) -> str:
    lines = []
    for i, tok in enumerate(tokens):
        name = tok["name"]
        if numbered:
            m = re.match(r"(\d+)\.\s*(.+)", name)
            idx, label = (m.group(1), m.group(2)) if m else (str(i + 1), name)
        else:
            idx, label = f"{i + 1:02d}", name
        lines.append(
            f'      <li><span class="idx">{idx}</span><a href="#{tok["id"]}">{label}</a></li>'
        )
    return "\n".join(lines)


def build_page(md_path: Path, out_path: Path, title: str, description: str,
                prompt: str, rail_label: str, numbered_rail: bool):
    content_html, tokens = render_markdown(md_path)
    page = (
        TEMPLATE
        .replace("{{TITLE}}", title)
        .replace("{{DESCRIPTION}}", description)
        .replace("{{PROMPT}}", prompt)
        .replace("{{RAIL_LABEL}}", rail_label)
        .replace("{{RAIL_ITEMS}}", rail_items(tokens, numbered_rail))
        .replace("{{CONTENT}}", content_html)
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page, "utf-8")
    print(f"  {md_path.relative_to(ROOT)}  ->  {out_path.relative_to(ROOT)}")


def first_heading(md_path: Path, fallback: str) -> str:
    for line in md_path.read_text("utf-8").splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def build_spec_pages():
    """Walk content/spec/ for every sync_spec.py-generated index.md — the
    index page itself, each version's latest revision, and any dated
    snapshots — and build each. Depth-driven since the tree shape is fixed
    (spec/, spec/{version}/, spec/{version}/{date}/), not content-driven."""
    spec_root = ROOT / "content" / "spec"
    if not spec_root.is_dir():
        return
    for md_path in sorted(spec_root.rglob("index.md")):
        parts = md_path.relative_to(spec_root).parent.parts
        if parts == (".",) or parts == ():
            parts = ()
        url_path = "spec/" + "/".join(parts)
        out_path = DIST / "spec" / Path(*parts) / "index.html" if parts else DIST / "spec" / "index.html"
        prompt = f"~/blygger.org/{url_path}" + ("" if url_path.endswith("/") else "/")

        if len(parts) == 0:
            title = first_heading(md_path, "Blygger Protocol — Specification Index")
            description = "Index of Blygger protocol spec versions and dated snapshots."
            rail_label, numbered_rail = "Versions", False
        elif len(parts) == 1:
            version = parts[0]
            title = first_heading(md_path, f"The Blygger Protocol — Version {version}")
            description = f"Normative specification of the Blygger protocol, version {version}."
            rail_label, numbered_rail = "Sections", True
        else:
            version, date = parts[0], parts[1]
            title = first_heading(md_path, f"The Blygger Protocol — Version {version} ({date} snapshot)")
            description = f"Blygger protocol version {version}, immutable snapshot from {date}."
            rail_label, numbered_rail = "Sections", True

        build_page(md_path, out_path, title=title, description=description,
                   prompt=prompt, rail_label=rail_label, numbered_rail=numbered_rail)


if __name__ == "__main__":
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    print("Building HTML...")
    build_page(
        ROOT / "content" / "overview.md",
        DIST / "index.html",
        title="Blygger — an AI-native, decentralized medium for writing in public",
        description="Blygger is a protocol for public writing: fragments, threads, "
                     "TK-transclusion, and versioning over static files and RSS.",
        prompt="~/blygger.org/blyg/",
        rail_label="On this page",
        numbered_rail=False,
    )
    build_spec_pages()

    shutil.copyfile(ROOT / "site.css", DIST / "site.css")
    print("  site.css  ->  dist/site.css")
    print("Done.")
