import unittest

from state_manager import default_state


class StateManagerTests(unittest.TestCase):
    def test_default_state_shape(self):
        state = default_state()
        self.assertIn("title", state)
        self.assertIn("providers", state)
        self.assertEqual(state["source"], "sanitized_sample")
        self.assertEqual(state["providers"], [])


if __name__ == "__main__":
    unittest.main()
