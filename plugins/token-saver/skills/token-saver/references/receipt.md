# Token Receipt

Use one of three measurement levels internally:

| Level | Requirement | Wording |
| --- | --- | --- |
| `exact` | Both baseline and optimized payload were tokenized with the target model's tokenizer, or the harness exposed equivalent counts | `净节省 8,633 input tokens（66.4%）` |
| `estimated` | Both payloads are available but only a documented approximation is possible | `估算净节省约 8.6K input tokens` |
| `observed-only` | No comparable baseline exists | Report observable volume and explain that no pre-filter inventory was captured |

Calculate:

```text
gross_saved = baseline_input - optimized_input
net_saved = gross_saved - optimizer_overhead
saved_percent = net_saved / baseline_input * 100
```

The baseline is a locally constructed payload representing the context that the same task would have sent without Token Saver. It is not a second paid model call. Keep the task, model, system instructions, conversation state, and requested evidence constant; vary only the selected/filtering step.

Capture the baseline **before** filtering. Prefer lightweight manifests created by
`scripts/capture_candidate.py`; they record text bytes, estimated text tokens, and image/page counts
without copying the candidate content into the conversation. Pass the two manifests to
`scripts/estimate_receipt.py --baseline-manifest ... --optimized-manifest ...`.

For mixed text and visual inputs, never convert image pages into text tokens or combine them into
one invented number. Report the dimensions separately:

```text
Token Saver 账单｜文本候选约 X → Y tokens｜图表 A → B 页
```

Replace placeholders only with values captured from the current task. Public documentation and
marketing examples must use reproducible measurements or retain placeholders; never invent a
plausible-looking percentage.

In `Full Fidelity`, savings may only be attributed to navigation, indexes, deduplication, or
presentation. Never count preserved or fully inspected evidence as removed. Use wording such as:

```text
Token Saver 账单｜完整证据已保留｜导航上下文约 X → Y tokens
```

If no separable navigation baseline exists, say `完整证据已保留｜本轮不主张 token 节省`.

Use exactly one of the following final-line forms. Do not invent variants.

Exact comparable measurement:

```text
Token Saver 账单｜候选上下文 X → Y input tokens｜净节省 Z（P%）
```

Estimated comparable measurement:

```text
Token Saver 账单｜候选上下文约 X → Y tokens｜估算净节省约 Z（P%）
```

Observed-only measurement when no comparable baseline exists:

```text
Token Saver 账单｜已处理约 Y tokens｜未记录可比基线，不估算节省
```

Comparable measurement with zero or negative net savings:

```text
Token Saver 账单｜已处理约 Y tokens｜未产生可报告的净节省
```

Full Fidelity without a separable navigation baseline:

```text
Token Saver 账单｜完整证据已保留｜本轮不主张 token 节省
```

Do not display `unavailable`, `可归因节省 0`, a negative number, or a marketing estimate. Fast Pass
uses no receipt at all. Use `scripts/estimate_receipt.py` when baseline and optimized local artifacts
or manifests are available. Mention cost separately when cached-token and model-pricing data are
available; token reduction and bill reduction are not interchangeable.
