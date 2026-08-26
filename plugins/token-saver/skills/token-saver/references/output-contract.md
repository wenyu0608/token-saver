# Output Contract

Treat the first and last nonblank lines as a strict interface. Do not improvise synonyms, labels,
emoji, punctuation, or extra status lines.

## Fast Pass

- Do not add a Token Saver opening line.
- Do not add a Token Saver receipt.
- Make the final nonblank line exactly:

```text
提示：这是简单任务，下次无需启用 Token Saver。
```

Never expose optimizer overhead or negative savings on Fast Pass.

## Focused route

Make the first nonblank line exactly this shape:

```text
⚡ Token Saver｜<Method>[ + <Method>]：<short action>
```

Allowed method labels are `Repomix`, `Diff Context`, `Errors Only`, `Docs Slice`,
`Session Handoff`, and `Token Audit`. Show at most two. Keep the action concrete and under
24 Chinese characters or 80 ASCII characters. Do not write `匹配到`, `本次已启用`, savings,
or percentages in the opening.

## Full Fidelity route

Make the first nonblank line exactly:

```text
🔍 Token Saver｜Full Fidelity：保留完整证据，仅压缩导航与重复内容
```

## Final line

For every routed task, emit exactly one receipt as the final nonblank line. Copy one applicable
form from `receipt.md`; do not put any content after it. Never print `unavailable`.

Before sending, check all four invariants:

1. Fast Pass has no branded opening and no receipt.
2. A routed response has exactly one approved opening.
3. A routed response has exactly one receipt, on the last nonblank line.
4. Every number in the receipt comes from the current task's captured artifacts.
