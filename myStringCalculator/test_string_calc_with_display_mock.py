import sys
import os
import unittest
from myStringCalculator.string_calc import StringCalc
from myStringCalculator.string_calc_display import StringCalcDisplay
from unittest.mock import MagicMock

# Add the directory containing string_calc_with_display.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_display_nothing_for_empty_string():
    c = StringCalc()
    d = MagicMock()
    sc = StringCalcDisplay(d, c)

    sc.add("")
    d.display.assert_not_called()

def test_should_display_operands_and_sum():
    c = StringCalc()
    d = MagicMock()
    sc = StringCalcDisplay(d, c)

    sc.add("1,2")
    d.display.assert_called_with("1 + 2 = 3")
