import unittest
from simple_calculator import SimpleCalculator()

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        result = SimpleCalculator().add(3, 5)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = SimpleCalculator().subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = SimpleCalculator().multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = SimpleCalculator().divide(8, 2)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        result = SimpleCalculator().divide(5, 0)
        self.assertIsNone(result)