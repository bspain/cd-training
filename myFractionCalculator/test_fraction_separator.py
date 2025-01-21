import sys
import os
import pytest
import re
from fraction_separator import FractionSeparator

# Add the directory containing myFractionCalculator to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_separate_fraction_into_numerator_and_denominator():
    separator = FractionSeparator()
    assert separator.separate("1/2") == (1, 2)
    assert separator.separate("03/4") == (3, 4)
    assert separator.separate("50/80") == (50, 80)

def test_should_generate_denominator_for_whole_numbers():
    separator = FractionSeparator()
    assert separator.separate("2") == (2, 1)
    assert separator.separate("10") == (10, 1)
    assert separator.separate("01") == (1, 1)

def test_should_return_error_if_whole_number_is_not_an_integer():
    separator = FractionSeparator()
    with pytest.raises(ValueError, match=re.escape("All fraction components (whole number, numerator, or denominator) must be an integer.")):
        separator.separate("2.5")

def test_should_return_error_if_numerator_is_not_an_integer():
    separator = FractionSeparator()
    with pytest.raises(ValueError, match=re.escape("All fraction components (whole number, numerator, or denominator) must be an integer.")):
        separator.separate("1.5/2")

def test_should_return_error_if_denominator_is_not_an_integer():
    separator = FractionSeparator()
    with pytest.raises(ValueError, match=re.escape("All fraction components (whole number, numerator, or denominator) must be an integer.")):
        separator.separate("1/2.5")