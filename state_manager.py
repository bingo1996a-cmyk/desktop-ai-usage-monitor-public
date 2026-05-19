"""Local JSON state persistence with atomic writes."""

from __future__ import annotations

import json
from typing import Any, Dict

from app_paths import get_data_dir

STATE_FILE = get_data_dir() / "state.json"


def default_state() -> Dict[str, Any]:
    return {
        "title": "Desktop AI Usage Monitor",
        "source": "demo_sample",
        "providers": [],
        "last_loaded_at": None,
    }


def load_state() -> Dict[str, Any]:
    if not STATE_FILE.exists():
        return default_state()
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return default_state()

    merged = default_state()
    if isinstance(data, dict):
        merged.update(data)
    return merged


def save_state(state: Dict[str, Any]) -> None:
    tmp_path = STATE_FILE.with_suffix(".tmp")
    with open(tmp_path, "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2, ensure_ascii=False)
    tmp_path.replace(STATE_FILE)
