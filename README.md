# Desktop AI Usage Monitor

A local desktop demo for monitoring AI usage metrics on a workstation.

This repository presents a compact desktop pattern for:

- AI usage visibility
- cost awareness
- local observability
- lightweight metric display

## Why This Repo Exists

Many AI-heavy local workflows need a small, always-on surface for answering questions like:

- How much usage have I accumulated this month?
- How expensive is the current workflow?
- Are cached inputs dominating the token profile?
- Can I review these metrics without opening a larger dashboard?

This repo demonstrates one answer: a local desktop widget backed by repository sample data and a generic provider abstraction.

## What This Repo Shows

- A local-only desktop widget built with `PySide6`
- A generic provider model for AI usage metrics
- Local JSON state persistence with atomic writes
- Pure formatting helpers and lightweight tests
- An example monthly usage summary
- A modular structure that can be extended with more providers or views

## Repo Layout

```text
main.py                        App entry point
floating_widget.py             Simple desktop widget
state_manager.py               Local JSON persistence
widget_formatters.py           Display formatting helpers
app_paths.py                   Local path helpers
public_providers/              Provider abstractions
sample_data/                   Local demo payloads
evidence/                      Human-readable monthly summary notes
tests/                         Lightweight regression tests
ARCHITECTURE.md                Architecture notes
SECURITY.md                    Runtime notes
```

## Sample Evidence Included

This repo includes a monthly usage summary for `2026-05`:

- active days: `18`
- request count: `23,939`
- output tokens: `21,795,595`
- input cache hit tokens: `2,980,890,496`
- input cache miss tokens: `80,871,022`
- cache hit ratio: `97.36%`
- monthly cost: `312.8643 CNY`

See [evidence/deepseek_usage_summary_2026_05.md](./evidence/deepseek_usage_summary_2026_05.md).

## Run Locally

```bash
pip install -r requirements.txt
python main.py
```

The default demo reads local sample files from the repository. It does not call any external API.

## Current Demo Surface

The demo currently renders a local widget with:

- monthly cost
- request count
- output tokens
- cache hit tokens
- cache hit ratio
- active days

All values come from sample files under [sample_data](./sample_data/).

## Extending This Repo

Natural next steps for this project include:

- additional provider adapters
- historical storage and trend views
- richer widgets or charts
- alerting and threshold summaries

See [ARCHITECTURE.md](./ARCHITECTURE.md) and [SECURITY.md](./SECURITY.md).

## Runtime Notes

- local-only desktop app
- no listening ports
- no embedded service credentials in the demo
- no external API calls in the default demo configuration

## License

This repository is released under the MIT License. See [LICENSE](./LICENSE).
