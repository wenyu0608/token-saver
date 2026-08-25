#!/usr/bin/env python3
"""Estimate observable, file-backed context overhead without reading contents."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


NAMES = {"AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules", "hooks.json"}
SKIP = {".git", "node_modules", "vendor", "dist", "build", ".next", ".venv"}


def estimate_tokens(size: int) -> int:
    return (size + 3) // 4


def candidates(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP for part in path.parts):
            continue
        if path.is_file() and (path.name in NAMES or path.name == "SKILL.md"):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    rows = []
    for path in candidates(root):
        size = path.stat().st_size
        rows.append({
            "path": str(path.relative_to(root)),
            "bytes": size,
            "estimated_tokens": estimate_tokens(size),
        })
    rows.sort(key=lambda row: row["estimated_tokens"], reverse=True)

    result = {
        "root": str(root),
        "method": "ceil(file_bytes / 4); observable files only",
        "estimated_tokens": sum(row["estimated_tokens"] for row in rows),
        "files": rows,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"observable estimate: {result['estimated_tokens']} tokens")
        for row in rows[:20]:
            print(f"{row['estimated_tokens']:>8}  {row['path']}")
        if len(rows) > 20:
            print(f"... {len(rows) - 20} more files")
        print("not measured: hidden harness instructions, chat history, or tool results")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
