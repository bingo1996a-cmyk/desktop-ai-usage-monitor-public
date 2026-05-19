# Architecture Notes

## Overview

This repository is intentionally small. It demonstrates a safe public split between:

1. a desktop presentation layer
2. a local persistence layer
3. a provider abstraction layer
4. sanitized evidence and sample payloads

## Layers

### UI Layer

- `main.py`
- `floating_widget.py`

Responsibilities:

- start the desktop app
- render the current usage snapshot
- let the user reload sanitized sample data

### Formatting Layer

- `widget_formatters.py`

Responsibilities:

- format percentages
- format balances
- format token counts
- format timestamps for display

### Persistence Layer

- `state_manager.py`
- `app_paths.py`

Responsibilities:

- define a stable local state shape
- load and save local JSON safely
- keep runtime state inside a local data directory

### Provider Layer

- `public_providers/base.py`
- `public_providers/mock_usage.py`

Responsibilities:

- define a small provider interface
- load sanitized local sample data

This public layer is intentionally auth-free.

### Evidence Layer

- `sample_data/`
- `evidence/`

Responsibilities:

- provide non-sensitive example inputs
- provide a human-readable explanation of the included monthly summary

## Public vs Private Boundary

This public repo should contain:

- UI structure
- local persistence
- provider contracts
- sanitized examples
- testable pure helpers

This public repo should not contain:

- raw provider credentials
- raw session cookies
- account identifiers
- raw usage exports
- provider-specific scraping or login recovery logic

## Why This Pattern Matters

For many local AI workflows, the hard part is not drawing a widget. The hard part is preserving a clean separation between:

- portable engineering patterns that are safe to publish
- private adapters that should remain local

This repository is designed to keep that split obvious.
