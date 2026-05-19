# Architecture Notes

## Overview

This repository is intentionally small. It demonstrates a safe public split between:

1. a desktop presentation layer
2. a local persistence layer
3. a provider abstraction layer
4. example monthly summary payloads

## Layers

### UI Layer

- `main.py`
- `floating_widget.py`

Responsibilities:

- start the desktop app
- render the current usage snapshot
- let the user reload the demo sample

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
- load local demo sample data

The default provider layer in this repository is file-based.

### Evidence Layer

- `sample_data/`
- `evidence/`

Responsibilities:

- provide non-sensitive example inputs
- provide a human-readable explanation of the included monthly summary

## Repository Focus

This repository focuses on:

- UI structure
- local persistence
- provider contracts
- example inputs
- testable pure helpers

## Extension Direction

Teams extending this pattern may add:

- provider adapters
- historical storage
- charts and trend views
- richer alerting logic

## Why This Pattern Matters

For many local AI workflows, the hard part is not drawing a widget. The hard part is preserving a clean separation between:

- a small always-on UI surface
- data loading and persistence logic
- reusable formatting helpers

This repository is designed to keep those boundaries obvious.
