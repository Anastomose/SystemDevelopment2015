import unittest

import calculator_functions as calc

class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        self.x = 2
        self.y = 3

    def test_add(self):
        self.assertEqual(calc.add(self.x, self.y), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(self.y, self.x), 1)

    def test_floater(self):
        self.assertEqual(calc.add(0.5, 0.5), 1)


if __name__ == "__main__":
    unittest.main()
