#!/usr/bin/env python3
"""Create a conservative, byte-derived Token Saver receipt."""

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


def estimated_tokens(paths: list[Path]) -> int:
    return (sum(size_at(path) for path in paths) + 3) // 4


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", action="append", required=True)
    parser.add_argument("--baseline", action="append", default=[])
    parser.add_argument("--optimized", action="append", default=[])
    parser.add_argument("--overhead-tokens", type=int, default=0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    optimized = estimated_tokens([Path(value) for value in args.optimized])
    if not args.baseline:
        result = {
            "version": "1.0",
            "measurement": "observed-only",
            "methods": args.method,
            "observable_input_tokens": optimized,
            "attributable_saved_tokens": 0,
            "reason": "No comparable pre-filter baseline was captured.",
        }
    else:
        baseline = estimated_tokens([Path(value) for value in args.baseline])
        saved = baseline - optimized - args.overhead_tokens
        result = {
            "version": "1.0",
            "measurement": "estimated",
            "methods": args.method,
            "baseline_input_tokens": baseline,
            "optimized_input_tokens": optimized,
            "optimizer_overhead_tokens": args.overhead_tokens,
            "net_saved_tokens": saved,
            "saved_percent": round(saved / baseline * 100, 1) if baseline else 0,
            "reason": "Estimated with ceil(total UTF-8 bytes / 4).",
        }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["measurement"] == "observed-only":
        print(
            f"Token Saver 账单｜已处理约 {optimized:,} tokens｜"
            "可归因节省 0（未记录压缩前候选内容）"
        )
    else:
        print(
            f"Token Saver 账单｜估算省下 {result['net_saved_tokens']:,} tokens "
            f"({result['saved_percent']}%)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
