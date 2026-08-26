# Token Receipt

Use one of three measurement levels internally:

| Level | Requirement | Wording |
| --- | --- | --- |
| `exact` | Both baseline and optimized payload were tokenized with the target model's tokenizer, or the harness exposed equivalent counts | `净节省 8,633 input tokens（66.4%）` |
| `estimated` | Both payloads are available but only a documented approximation is possible | `估算净节省约 8.6K input tokens` |
| `observed-only` | No comparable baseline exists | Report observable volume and a conservative attributable saving |

Calculate:

```text
gross_saved = baseline_input - optimized_input
net_saved = gross_saved - optimizer_overhead
saved_percent = net_saved / baseline_input * 100
```

The baseline is a locally constructed payload representing the context that the same task would have sent without Token Saver. It is not a second paid model call. Keep the task, model, system instructions, conversation state, and requested evidence constant; vary only the selected/filtering step.

Preferred compact footer:

```text
Token Saver 账单｜估算省下 8,633 tokens（66.4%）
```

When there is no baseline, do not display `unavailable`. Use the most informative honest form:

```text
Token Saver 账单｜已处理约 1.2K tokens｜可归因节省 0（未记录压缩前候选内容）
Token Saver 账单｜轻量任务，额外压缩≈0 tokens
```

`0` is a conservative attributable value, not a claim that the workflow had no indirect benefit. Use `scripts/estimate_receipt.py` when baseline and optimized local artifacts are available. Mention cost separately when cached-token and model-pricing data are available; token reduction and bill reduction are not interchangeable.
