"""Pure formatting helpers for the desktop widget."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Mapping

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def clock_segments(now: datetime) -> tuple[str, str, str]:
    return now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), WEEKDAYS[now.weekday()]


def format_large_number(value: float | int | None) -> str:
    if value is None:
        return "--"
    numeric = float(value)
    if abs(numeric) >= 1_000_000_000:
        return f"{numeric / 1_000_000_000:.2f}B"
    if abs(numeric) >= 1_000_000:
        return f"{numeric / 1_000_000:.2f}M"
    if abs(numeric) >= 1_000:
        return f"{numeric:,.0f}"
    if numeric.is_integer():
        return f"{numeric:.0f}"
    return f"{numeric:.2f}"


def format_metric_value(metric: Mapping[str, Any]) -> str:
    if metric.get("last_error_type"):
        return f"[{metric['last_error_type']}]"

    value = metric.get("value")
    kind = metric.get("kind")
    unit = metric.get("unit") or ""

    if value is None:
        return "--"

    if kind == "balance":
        return f"{float(value):.2f} {unit or 'CNY'}"
    if kind == "percent":
        return f"{float(value):.2f}%"
    if kind in {"count", "tokens"}:
        suffix = f" {unit}" if unit else ""
        return f"{format_large_number(value)}{suffix}"
    if unit:
        return f"{format_large_number(value)} {unit}"
    return format_large_number(value)


def format_updated_at(metric: Mapping[str, Any]) -> str:
    updated_at = metric.get("updated_at")
    if not updated_at:
        return "--"
    return str(updated_at).replace("T", " ")[:19]
