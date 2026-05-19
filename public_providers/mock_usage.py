"""Load a local sample snapshot for the desktop demo."""

from __future__ import annotations

import json

from app_paths import get_sample_data_dir
from .base import ProviderAdapter, ProviderSnapshot


class MockUsageProvider(ProviderAdapter):
    def load(self) -> ProviderSnapshot:
        sample_path = get_sample_data_dir() / "current_state.json"
        with open(sample_path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return ProviderSnapshot(payload=payload)
