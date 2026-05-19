import unittest
from datetime import datetime

from widget_formatters import clock_segments, format_large_number, format_metric_value


class WidgetFormatterTests(unittest.TestCase):
    def test_clock_segments(self):
        self.assertEqual(
            clock_segments(datetime(2026, 5, 20, 9, 8, 7)),
            ("2026-05-20", "09:08:07", "Wed"),
        )

    def test_large_number_formatting(self):
        self.assertEqual(format_large_number(23939), "23,939")
        self.assertEqual(format_large_number(21795595), "21.80M")
        self.assertEqual(format_large_number(2980890496), "2.98B")

    def test_metric_formatting(self):
        self.assertEqual(
            format_metric_value({"kind": "balance", "value": 312.8643, "unit": "CNY"}),
            "312.86 CNY",
        )
        self.assertEqual(
            format_metric_value({"kind": "percent", "value": 97.36}),
            "97.36%",
        )
        self.assertEqual(
            format_metric_value({"kind": "tokens", "value": 21795595, "unit": "tokens"}),
            "21.80M tokens",
        )


if __name__ == "__main__":
    unittest.main()
