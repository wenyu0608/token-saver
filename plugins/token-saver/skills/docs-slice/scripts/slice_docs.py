#!/usr/bin/env python3
"""Return bounded sections from local Markdown or text documentation."""

from __future__ import annotations

import argparse
from pathlib import Path


EXTENSIONS = {".md", ".mdx", ".txt", ".rst"}


def files_at(path: Path):
    if path.is_file():
        yield path
        return
    for item in sorted(path.rglob("*")):
        if item.is_file() and item.suffix.lower() in EXTENSIONS and ".git" not in item.parts:
            yield item


def sections(path: Path):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    starts = [i for i, line in enumerate(lines) if line.lstrip().startswith("#")]
    if not starts:
        for start in range(0, len(lines), 40):
            yield start + 1, "(text block)", lines[start:start + 40]
        return
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        yield start + 1, lines[start].strip(), lines[start:min(end, start + 80)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--query", action="append", required=True)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--max-chars", type=int, default=5000)
    args = parser.parse_args()

    root = Path(args.path).resolve()
    terms = [term.casefold() for term in args.query if term.strip()]
    ranked = []
    for path in files_at(root):
        for line, heading, body in sections(path):
            text = "\n".join(body)
            folded = text.casefold()
            score = sum(folded.count(term) for term in terms)
            if score:
                ranked.append((score, str(path), line, heading, text))
    ranked.sort(key=lambda item: (-item[0], item[1], item[2]))

    used = 0
    for score, path, line, heading, text in ranked[:max(1, args.limit)]:
        remaining = args.max_chars - used
        if remaining <= 0:
            break
        text = text[:remaining]
        print(f"\n--- {path}:{line} | score={score} | {heading} ---")
        print(text)
        used += len(text)
    if not ranked:
        print("no matching documentation sections")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
