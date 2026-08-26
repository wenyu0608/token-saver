---
name: repomix
description: Build a compressed, token-efficient map of a repository with Repomix before analyzing or changing an unfamiliar codebase. Invoke explicitly with $repomix when repository-wide context is useful; do not use for a known single-file task.
---

# Repomix

Use Repomix as a discovery layer, not as the source to edit.

## Workflow

1. Resolve the repository root and the narrowest useful scope from the user's request. Prefer a relevant directory such as `src/` over the entire repository when possible.
2. Confirm `repomix` is available. If it is missing, report that fact and give the install command; do not silently substitute a network-based runner.
3. Create a temporary directory with `mktemp -d`. Run Repomix from the repository root with `--compress` and an explicit output path inside that temporary directory. Respect existing ignore files and add `--include` or `--ignore` only when the task provides a clear boundary.
4. Read the compressed output to identify entry points, dependencies, and the smallest set of relevant original files. If the output is still very large, narrow the scope before reading it in full.
5. Continue the user's task using original source files. Never edit, commit, or treat the Repomix output as authoritative source code.

## Token discipline

- Do not repeatedly regenerate the map unless repository contents or task scope changed materially.
- Do not paste the complete map into the user-facing response.
- Prefer repository selection before compression: excluding irrelevant files saves more tokens than compressing them.
- For a task already confined to one or two known files, say that Repomix would add overhead and work from those files directly.
- Report the chosen scope and the relevant files found in one compact line.

## Safety

Repomix output can contain source code and secrets that were not ignored. Keep generated output local and temporary. Do not upload or transmit it to another service beyond the model interaction already authorized by the current Codex task.
