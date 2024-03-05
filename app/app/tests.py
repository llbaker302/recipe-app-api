"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        result = calc.add(5, 6)

        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers together."""

        result = calc.subtract(10, 5)

        self.assertEqual(result, 5)