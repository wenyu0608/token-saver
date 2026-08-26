# Changelog

## v0.3.2-alpha.5 - 2026-08-26

### Changed

- Repositioned the marketplace listing around saving AI tokens without losing critical context.
- Added a high-contrast wallet logo, composer icon, brand color, and public website link.
- Tightened starter prompts to the three most useful first-run workflows.

## v0.3.2-alpha.4 - 2026-08-26

### Changed

- Removed synthetic token-reduction percentages from public examples.
- Public receipts now use reproducible measurements or explicit placeholders.

## v0.3.2-alpha.3 - 2026-08-26

### Added

- `Full Fidelity` mode for exhaustive debugging, verification, audits, and high-risk correctness work.
- Automatic escalation gates for cross-boundary bugs, inconclusive filtered evidence, causal ordering or environment details, and explicit complete-review requests.
- Coverage-aware receipts that only attribute savings to navigation, deduplication, and presentation while preserving complete evidence.

### Changed

- Fidelity requirements now override token reduction in the umbrella router.

## v0.3.2-alpha.2 - 2026-08-26

### Added

- Pre-filter candidate capture for text bytes, estimated text tokens, and visual page counts.
- Mixed-content receipts that report text-token and image-page reductions independently.
- Regression tests for baseline manifests and observed-only fallback behavior.

### Changed

- Heavy workflows now capture the candidate scope before filtering whenever it is locally observable.
- Receipts no longer attempt to merge image pages into an invented text-token total.

## v0.3.2-alpha.1 - 2026-08-26

First public alpha shaped by real user feedback.

### Included

- One umbrella `$token-saver` router plus Repomix, Diff Context, Errors Only, Docs Slice, Session Handoff, and Token Audit workflows.
- Progressive loading: short questions take a silent Fast Pass; heavy tasks load only the selected optimizer and measurement rules.
- Exact, estimated, and observed-only receipts with explicit measurement provenance.
- A pinned Repomix wrapper that avoids global installation and isolates its npm cache in plugin data.
- A measured DreamZero paper-and-code case study showing a candidate-context reduction from 379,765 to 57,098 tokens.

### User-feedback fix

The original umbrella workflow could load about 1,230 tokens of routing and receipt instructions for a one-line question. The Fast Pass entry now costs about 241 estimated tokens and skips child references, reducing fixed overhead by roughly 80%. Its user-facing response stays clean and only reminds the user that simple tasks do not need Token Saver.

### Known limitations

- Git marketplace installations do not update live; users must refresh the marketplace and reinstall the plugin.
- Receipt accuracy depends on available artifacts because coding-agent harnesses do not always expose the final serialized model input.
- The Repomix fallback requires Node.js/npm for its first approved, pinned download.
- Windows and Linux clean-install coverage is still limited during alpha.

### Install

```bash
codex plugin marketplace add wenyu0608/token-saver --ref main
codex plugin add token-saver@token-saver
```

### Update

```bash
codex plugin marketplace upgrade token-saver
codex plugin add token-saver@token-saver
```
