# Security Notes

## Local Demo Mode

The default configuration in this repository is local-only:

- it opens no listening ports
- it stores runtime state in local files
- it loads repository sample data from disk
- it does not contact external APIs in demo mode

## Repository Data

The included monthly summary is used to render the desktop widget and document the metric shape shown in the demo.

It includes:

- aggregated request counts
- aggregated token counts
- aggregated monthly costs
- model-level summary fields

## Extending The Project

If you extend this repository with live service integrations:

- keep service configuration separate from the demo surface
- keep runtime secrets outside versioned project files
- prefer aggregated summary outputs for public examples
