import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance for testing."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calculator.divide(8, 2)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        result = self.calculator.divide(5, 0)
        self.assertIsNone(result)