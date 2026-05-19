# Desktop AI Usage Monitor

A public-safe desktop demo for monitoring AI usage metrics on a local machine.

This repository is a cleaned public extract of a larger private desktop tool. It keeps the publishable architecture and removes private adapters, browser-session logic, personal paths, credentials, and raw account records.

The goal is not to publish a complete production monitor. The goal is to publish a safe, inspectable desktop pattern for:

- AI usage visibility
- cost awareness
- local observability
- clean separation between public architecture and private adapters

## Why This Repo Exists

Many AI-heavy local workflows need a small, always-on surface for answering questions like:

- How much usage have I accumulated this month?
- How expensive is the current workflow?
- Are cached inputs dominating the token profile?
- Can I keep provider-specific credentials and session logic out of the public codebase?

This repo demonstrates one answer: a local desktop widget backed by sanitized sample data and a public-safe provider abstraction.

## What This Public Version Shows

- A local-only desktop widget built with `PySide6`
- A generic provider model for AI usage metrics
- Local JSON state persistence with atomic writes
- Pure formatting helpers and lightweight tests
- Sanitized monthly evidence derived from real usage records
- A safe boundary between public demo code and private account adapters

## What Is Intentionally Not Included

- API keys, cookies, or login sessions
- Private provider adapters
- Raw account identifiers
- Raw billing CSV exports
- Personal notes, handoff docs, or local machine paths

## Repo Layout

```text
main.py                        App entry point
floating_widget.py             Simple desktop widget
state_manager.py               Local JSON persistence
widget_formatters.py           Display formatting helpers
app_paths.py                   Local path helpers
public_providers/              Public-safe provider abstractions
sample_data/                   Sanitized local sample payloads
evidence/                      Human-readable sanitized evidence summaries
tests/                         Lightweight regression tests
ARCHITECTURE.md                Public architecture notes
SECURITY.md                    Redaction and safety notes
```

## Sample Evidence Included

This repo includes a sanitized monthly usage summary for `2026-05`:

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

The public demo uses sanitized local sample data only. It does not call any external API.

## Current Demo Surface

The demo currently renders a local widget with:

- monthly cost
- request count
- output tokens
- cache hit tokens
- cache hit ratio
- active days

All values come from sanitized sample files under [sample_data](./sample_data/).

## Extending This Safely

If you want to adapt this pattern for a real private workflow, keep the split clear:

- public repo:
  - UI shell
  - formatting helpers
  - provider interface
  - sanitized evidence
- private repo:
  - account credentials
  - browser session handling
  - provider-specific auth logic
  - raw billing exports

See [ARCHITECTURE.md](./ARCHITECTURE.md) and [SECURITY.md](./SECURITY.md).

## Security Boundary

- local-only desktop app
- no listening ports
- no embedded credentials
- no raw personal usage exports
- no browser session scraping logic in the public repo

## License

This repository is released under the MIT License. See [LICENSE](./LICENSE).
