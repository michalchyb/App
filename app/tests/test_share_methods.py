import unittest
from datetime import datetime

from project.market.shares import Share

class TestShareMethods(unittest.TestCase):

    def test_validate_money_valid(self):
        self.assertEqual(Share.validate_money("10.50"), 10.50)
        self.assertEqual(Share.validate_money("100.0"), 100.0)
        self.assertEqual(Share.validate_money("50"), 50.0)

    def test_validate_money_invalid(self):
        with self.assertRaises(ValueError):
            Share.validate_money("0")
        with self.assertRaises(ValueError):
            Share.validate_money("-10")
        with self.assertRaises(ValueError):
            Share.validate_money("abc")
        with self.assertRaises(ValueError):
            Share.validate_money("$50")

    def test_convert_to_date_valid(self):
        self.assertEqual(Share.convert_to_date("2024-08-19"), datetime(2024, 8, 19).date())
        self.assertEqual(Share.convert_to_date("19.08.2024"), datetime(2024, 8, 19).date())
        self.assertEqual(Share.convert_to_date(datetime(2024, 8, 19)), datetime(2024, 8, 19).date())

    def test_convert_to_date_invalid(self):
        with self.assertRaises(ValueError):
            Share.convert_to_date("19/08/2024")
        with self.assertRaises(ValueError):
            Share.convert_to_date("abc")

if __name__ == '__main__':
    unittest.main()