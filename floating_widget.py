"""Minimal local desktop widget for AI usage metrics."""

from __future__ import annotations

from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from public_providers import MockUsageProvider
from state_manager import load_state, save_state
from widget_formatters import clock_segments, format_metric_value, format_updated_at


class FloatingWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Desktop AI Usage Monitor")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setMinimumWidth(380)

        self._provider = MockUsageProvider()
        self._clock_label = QLabel()
        self._source_label = QLabel()
        self._rows: list[QLabel] = []

        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(10)

        self._clock_label.setStyleSheet("font-size: 18px; font-weight: 600;")
        self._source_label.setWordWrap(True)

        root.addWidget(self._clock_label)
        root.addWidget(self._source_label)

        for _ in range(6):
            row = QLabel("--")
            row.setWordWrap(True)
            row.setStyleSheet("padding: 6px; border: 1px solid #d0d7de; border-radius: 8px;")
            self._rows.append(row)
            root.addWidget(row)

        self._refresh_button = QPushButton("Reload Demo Sample")
        self._refresh_button.clicked.connect(self.reload_sample)
        root.addWidget(self._refresh_button)

        self._clock_timer = QTimer(self)
        self._clock_timer.timeout.connect(self._refresh_clock)
        self._clock_timer.start(1000)

        self.reload_sample()
        self._refresh_clock()

    def _refresh_clock(self) -> None:
        date_text, time_text, weekday = clock_segments(datetime.now())
        self._clock_label.setText(f"{date_text}  {time_text}  {weekday}")

    def reload_sample(self) -> None:
        snapshot = self._provider.load().payload
        snapshot["last_loaded_at"] = datetime.utcnow().isoformat()
        save_state(snapshot)
        self.render_state(load_state())

    def render_state(self, state: dict) -> None:
        source = state.get("source", "unknown")
        loaded_at = state.get("last_loaded_at", "--")
        self._source_label.setText(
            "Source: "
            f"{source}\nLast loaded: {str(loaded_at).replace('T', ' ')[:19]}\n"
            "This demo uses local sample data only."
        )

        providers = list(state.get("providers", []))
        for index, row in enumerate(self._rows):
            if index < len(providers):
                metric = providers[index]
                note = metric.get("note", "")
                note_line = f"\n{note}" if note else ""
                row.setText(
                    f"{metric.get('label', 'Metric')}: {format_metric_value(metric)}\n"
                    f"Updated: {format_updated_at(metric)}{note_line}"
                )
            else:
                row.setText("--")


def launch_app() -> int:
    app = QApplication.instance() or QApplication([])
    widget = FloatingWidget()
    widget.show()
    return app.exec()
