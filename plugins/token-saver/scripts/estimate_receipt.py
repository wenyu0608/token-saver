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


def load_manifest(path: str) -> dict[str, int]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    return {
        "text_tokens": int(value["estimated_text_tokens"]),
        "image_pages": int(value.get("image_pages", 0)),
    }


def percent(saved: int, baseline: int) -> float:
    return round(saved / baseline * 100, 1) if baseline else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", action="append", required=True)
    parser.add_argument("--baseline", action="append", default=[])
    parser.add_argument("--optimized", action="append", default=[])
    parser.add_argument("--baseline-manifest")
    parser.add_argument("--optimized-manifest")
    parser.add_argument("--overhead-tokens", type=int, default=0)
    parser.add_argument("--fidelity-mode", choices=("focused", "full"), default="focused")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if bool(args.baseline_manifest) != bool(args.optimized_manifest):
        parser.error("provide both --baseline-manifest and --optimized-manifest")

    if args.baseline_manifest:
        baseline_scope = load_manifest(args.baseline_manifest)
        optimized_scope = load_manifest(args.optimized_manifest)
        baseline = baseline_scope["text_tokens"]
        optimized = optimized_scope["text_tokens"]
        baseline_images = baseline_scope["image_pages"]
        optimized_images = optimized_scope["image_pages"]
    else:
        baseline = estimated_tokens([Path(value) for value in args.baseline])
        optimized = estimated_tokens([Path(value) for value in args.optimized])
        baseline_images = optimized_images = 0

    if not args.baseline and not args.baseline_manifest:
        result = {
            "version": "1.0",
            "measurement": "observed-only",
            "methods": args.method,
            "observable_input_tokens": optimized,
            "attributable_saved_tokens": 0,
            "reason": "No comparable pre-filter baseline was captured.",
            "fidelity_mode": args.fidelity_mode,
            "evidence_retained": args.fidelity_mode == "full",
        }
    else:
        saved = baseline - optimized - args.overhead_tokens
        image_pages_saved = baseline_images - optimized_images
        result = {
            "version": "1.1",
            "measurement": "estimated",
            "methods": args.method,
            "baseline_input_tokens": baseline,
            "optimized_input_tokens": optimized,
            "optimizer_overhead_tokens": args.overhead_tokens,
            "net_saved_tokens": saved,
            "saved_percent": percent(saved, baseline),
            "baseline_image_pages": baseline_images,
            "optimized_image_pages": optimized_images,
            "image_pages_saved": image_pages_saved,
            "image_pages_saved_percent": percent(image_pages_saved, baseline_images),
            "reason": "Text estimated with ceil(total bytes / 4); image pages reported separately.",
            "fidelity_mode": args.fidelity_mode,
            "evidence_retained": args.fidelity_mode == "full",
        }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["measurement"] == "observed-only":
        if args.fidelity_mode == "full":
            print("Token Saver 账单｜完整证据已保留｜本轮不主张 token 节省")
        else:
            print(
                f"Token Saver 账单｜已处理约 {optimized:,} tokens｜"
                "可归因节省 0（未记录压缩前候选内容）"
            )
    else:
        prefix = "Token Saver 账单｜"
        if args.fidelity_mode == "full":
            prefix += "完整证据已保留｜导航上下文约 "
        else:
            prefix += "文本候选约 "
        parts = [
            f"{prefix}{baseline:,} → {optimized:,} tokens "
            f"(↓{result['saved_percent']}%)"
        ]
        if baseline_images or optimized_images:
            parts.append(
                f"图表 {baseline_images:,} → {optimized_images:,} 页 "
                f"(↓{result['image_pages_saved_percent']}%)"
            )
        print("｜".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
