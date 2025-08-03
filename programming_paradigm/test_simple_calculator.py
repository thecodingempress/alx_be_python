import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance for testing."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(self.calculator.divide(8, 2), 4)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.divide(5, 0))