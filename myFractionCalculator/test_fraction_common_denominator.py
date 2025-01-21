import sys
import os
import pytest
import re
from fraction_common_denominator import FractionCommonDenominator

# Add the directory containing myFractionCalculator to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_return_leastcommonmultiple_of_one_when_the_denominators_are_the_same():
    commonDenominator = FractionCommonDenominator()
    assert commonDenominator.calculate(1, 1) == 1
    assert commonDenominator.calculate(2, 2) == 1
    assert commonDenominator.calculate(15, 15) == 1

def test_should_return_the_correct_leastcommonmultiple():
    commonDenominator = FractionCommonDenominator()
    assert commonDenominator.calculate(2, 4) == 4
    assert commonDenominator.calculate(3, 4) == 12
    assert commonDenominator.calculate(2, 6) == 6
    assert commonDenominator.calculate(6, 8) == 24