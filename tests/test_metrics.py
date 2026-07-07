import unittest
from src.lead_tracker import safe_divide, percentage


class MetricsTestCase(unittest.TestCase):
    def test_safe_divide_returns_zero_for_zero_denominator(self):
        self.assertEqual(safe_divide(10, 0), 0.0)

    def test_safe_divide_regular_case(self):
        self.assertEqual(safe_divide(10, 2), 5)

    def test_percentage_format(self):
        self.assertEqual(percentage(0.1234), "12.34%")


if __name__ == "__main__":
    unittest.main()
