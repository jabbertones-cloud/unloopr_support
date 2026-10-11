#!/usr/bin/env python3
"""Regenerate llms-full.txt from the support repo docs. Run from the repo root."""
import pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "llms-full.txt"

SECTIONS = [
    ("# Unloopr Support — Full Documentation", None),
    ("## Product overview", "README.md"),
    ("## Agent instructions", "llms.txt"),
    ("## Getting started", "docs/getting-started.md"),
    ("## FAQ", "docs/faq/faq.md"),
    ("## Troubleshooting index", "docs/troubleshooting.md"),
    ("## Pricing", "docs/pricing.md"),
    ("## Security", "docs/security.md"),
    ("## Agent contract", "AGENTS.md"),
    ("## Problem ontology", "knowledge/problem-ontology.md"),
]

parts = []
for title, rel in SECTIONS:
    parts.append(title)
    parts.append("")
    if rel:
        p = ROOT / rel
        if p.exists():
            # Strip the file's own H1 to avoid duplication (keep body)
            lines = p.read_text().splitlines()
            body = "\n".join(lines[1:]) if lines and lines[0].startswith("# ") else "\n".join(lines)
            parts.append(body.strip())
        else:
            parts.append(f"_(missing: {rel})_")
    parts.append("")
    parts.append("---")
    parts.append("")

OUT.write_text("\n".join(parts))
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
