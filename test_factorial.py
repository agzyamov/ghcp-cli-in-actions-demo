"""
Unit tests for the factorial module.

This test module provides comprehensive testing for the factorial function,
including normal cases, edge cases, and error handling.
"""

import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    """Test cases for the factorial function."""
    
    def test_factorial_zero(self):
        """Test that factorial of 0 is 1."""
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_one(self):
        """Test that factorial of 1 is 1."""
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_small_positive(self):
        """Test factorial of small positive integers."""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_larger_numbers(self):
        """Test factorial of larger positive integers."""
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(15), 1307674368000)
    
    def test_factorial_negative_raises_value_error(self):
        """Test that negative numbers raise ValueError."""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertIn("negative", str(context.exception).lower())
        
        with self.assertRaises(ValueError):
            factorial(-5)
        
        with self.assertRaises(ValueError):
            factorial(-100)
    
    def test_factorial_non_integer_raises_type_error(self):
        """Test that non-integer inputs raise TypeError."""
        with self.assertRaises(TypeError) as context:
            factorial(5.5)
        self.assertIn("integer", str(context.exception).lower())
        
        with self.assertRaises(TypeError):
            factorial("5")
        
        with self.assertRaises(TypeError):
            factorial([5])
        
        with self.assertRaises(TypeError):
            factorial(None)
    
    def test_factorial_boolean_accepted(self):
        """Test that boolean values work (since bool is subclass of int in Python)."""
        # In Python, bool is a subclass of int, so True=1 and False=0
        self.assertEqual(factorial(True), 1)
        self.assertEqual(factorial(False), 1)


if __name__ == '__main__':
    unittest.main()
