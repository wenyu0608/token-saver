# Token Receipt

Use one of three measurement levels:

| Level | Requirement | Wording |
| --- | --- | --- |
| `exact` | Both baseline and optimized payload were tokenized with the target model's tokenizer, or the harness exposed equivalent counts | `净节省 8,633 input tokens（66.4%）` |
| `estimated` | Both payloads are available but only a documented approximation is possible | `估算净节省约 8.6K input tokens` |
| `unavailable` | No comparable baseline exists | `净节省：暂不可测（缺少同任务的未优化基线）` |

Calculate:

```text
gross_saved = baseline_input - optimized_input
net_saved = gross_saved - optimizer_overhead
saved_percent = net_saved / baseline_input * 100
```

The baseline is a locally constructed payload representing the context that the same task would have sent without Token Saver. It is not a second paid model call. Keep the task, model, system instructions, conversation state, and requested evidence constant; vary only the selected/filtering step.

Preferred compact footer:

```text
Token Saver｜方法：diff-context + errors-only｜净节省：8,633 input tokens（exact）
```

When unavailable, say why in the same line. Mention cost separately when cached-token and model-pricing data are available; token reduction and bill reduction are not interchangeable.
