"""
Unit tests for the calculator library
"""
import src.calc as Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator().add(2, 2)

    def test_subtraction(self):
        assert 2 == Calculator().subtract(4, 2)
