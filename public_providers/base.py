"""Provider interface for usage snapshots."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ProviderSnapshot:
    payload: Dict[str, Any]


class ProviderAdapter:
    def load(self) -> ProviderSnapshot:
        raise NotImplementedError
