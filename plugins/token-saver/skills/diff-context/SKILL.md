---
name: diff-context
description: Review or continue existing code changes using the Git diff, changed symbols, and minimal dependency context. Use for PR reviews, regressions, or work-in-progress changes; do not use for an unfamiliar repository with no relevant diff.
---

# Diff Context

Start from changed lines instead of scanning the repository.

1. Inspect `git status --short`, `git diff --stat`, and the relevant unstaged, staged, or branch diff. Preserve unrelated user changes.
2. Read each changed hunk with bounded context. Identify the containing symbol and direct imports or callers with `rg` before opening more files.
3. Expand to a full original file only when the hunk lacks a required invariant, type, or control-flow edge.
4. Review or modify only the files justified by that dependency trail. Do not treat absence from the diff as permission to ignore a required test.
5. Report one compact line containing the diff basis and files inspected.

Prefer `git diff --unified=20` for initial context. Avoid repository-wide searches until a concrete symbol or behavior requires them.
