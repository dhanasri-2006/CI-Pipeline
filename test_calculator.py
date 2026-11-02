import unittest
from calculator import add, multiply


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)


if __name__ == "__main__":
    unittest.main()
