#!/usr/bin/env python3
"""Capture a lightweight pre- or post-filter context inventory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def size_at(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    return sum(
        item.stat().st_size
        for item in path.rglob("*")
        if item.is_file() and ".git" not in item.parts
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--text", action="append", default=[])
    parser.add_argument("--image-pages", type=int, default=0)
    parser.add_argument("--output")
    args = parser.parse_args()

    if args.image_pages < 0:
        parser.error("--image-pages must be non-negative")
    paths = [Path(value) for value in args.text]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        parser.error(f"missing path(s): {', '.join(missing)}")

    text_bytes = sum(size_at(path) for path in paths)
    result = {
        "version": "1.0",
        "label": args.label,
        "text_bytes": text_bytes,
        "estimated_text_tokens": (text_bytes + 3) // 4,
        "image_pages": args.image_pages,
        "estimator": "ceil(total bytes / 4); image pages reported separately",
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
