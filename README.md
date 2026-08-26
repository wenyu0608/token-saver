# Token Saver

An umbrella router for reducing avoidable coding-agent context without hiding the evidence needed to do the work.

Token Saver selects a focused workflow for each task, explains the choice naturally, and ends with an honest `exact`, `estimated`, or `observed-only` token receipt.

## Skills

- `$token-saver` automatically routes the task and produces a token receipt.
- `$repomix` builds a compressed map before exploring an unfamiliar repository.
- `$token-audit` measures observable context overhead and ranks fixes.
- `$errors-only` captures full command output locally and returns bounded failures.
- `$diff-context` starts from changed lines and expands only along justified dependencies.
- `$session-handoff` replaces stale chat history with a verified continuation brief.
- `$docs-slice` retrieves bounded, relevant documentation sections.

The umbrella `$token-saver` skill supports automatic selection. The six specialist skills remain explicit so their instructions are not injected into unrelated prompts. The bundled Repomix wrapper uses a compatible local CLI when available or, after explicit approval, retrieves a pinned version with `npx`; no global install is required.

## Install

```bash
codex plugin marketplace add wenyu0608/token-saver --ref main
codex plugin add token-saver@token-saver
```

Restart Codex, then invoke a skill such as:

```text
$token-saver diagnose the failing test without dumping the full build log
```

## Real-world example: understand DreamZero

We asked Token Saver to connect the [DreamZero paper](https://arxiv.org/abs/2602.15922) to its [official implementation](https://github.com/dreamzero0/dreamzero):

```text
$token-saver Read the DreamZero paper and code. Explain how the World Action Model
jointly predicts video and robot actions, then point me to the key implementation files.
```

Token Saver routed the task through two methods:

```text
⚡ Token Saver｜Docs Slice + Repomix：只读架构章节，再画代码地图
```

The resulting explanation followed one evidence trail:

1. Paper pages 6–7 define a causal DiT conditioned on vision, language, and proprioception, trained with joint video-action flow matching.
2. `groot/vla/model/dreamzero/base_vla.py` dispatches joint video-action inference to the action head.
3. `action_head/wan_flow_matching_action_tf.py` coordinates joint denoising, action sampling, and persistent KV caches.
4. `modules/wan_video_dit_action_casual_chunk.py` inserts state/action tokens into the causal DiT and decodes video and action predictions separately.

### Measured context funnel

| Context candidate | Tokens |
| --- | ---: |
| Full repository, uncompressed | 337,054 |
| Full repository with `repomix --compress` | 177,239 |
| Task-focused compressed repository map | 54,855 |
| Full 36-page paper, estimated | 42,711 |
| Relevant paper pages 6–7, estimated | 2,243 |

```text
Token Saver 账单｜候选上下文 379,765 → 57,098｜估算省下 322,667 tokens（85.0%）
```

Repository figures are Repomix token counts from DreamZero commit `ab790c1`; the focused scope contains `groot/vla/model/dreamzero/**`, its model configuration, and `README.md`. PDF figures use `ceil(UTF-8 bytes / 4)`, so the combined receipt is labeled as an estimate. The optimized number is a context candidate, not a claim that every token was sent to a model.

## Design

Token Saver optimizes context before it reaches the model. It favors selection over lossy compression, keeps raw diagnostic output locally retrievable, and never edits user configuration without permission.

Status lines use a compact branded form such as `⚡ Token Saver｜Docs Slice：只读关键段落`. Receipts quantify exact or estimated attributable savings; small or unmeasured tasks report conservative observable values instead of `unavailable`.

See [the MVP contract](docs/MVP.md) for routing, measurement levels, and the baseline model.

## License

MIT
