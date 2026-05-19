# Security Notes

## Redaction Policy

This repository is a public-safe extract. The following classes of data are intentionally excluded:

- API keys
- session cookies
- account identifiers
- raw billing rows
- raw browser state
- personal machine paths
- private handoff notes

## Included Evidence

The evidence in this repo is aggregated and sanitized. It is included only to demonstrate real-world usage scale without disclosing raw account records.

Included evidence may contain:

- aggregated request counts
- aggregated token counts
- aggregated monthly costs
- model-level summaries

Included evidence must not contain:

- raw user identifiers
- reconstructable credentials
- session material
- unredacted provider exports

## Local Runtime

The public demo is local-only:

- it opens no listening ports
- it ships no embedded credentials
- it loads sanitized sample data from disk
- it does not contact external APIs

## Adapting Privately

If you build on this repo for a private workflow:

- keep provider auth code outside the public repo
- keep raw exports outside the public repo
- keep private session logic outside the public repo
- publish only aggregated evidence
