import sys
import os

from fraction_joiner import FractionJoiner

# Add the directory containing myFractionCalculator to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_fraction_joiner_should_join_numerator_and_denominator():
    joiner = FractionJoiner()
    assert joiner.join(1, 2) == "1/2"
    assert joiner.join(3, 4) == "3/4"
    assert joiner.join(50, 80) == "50/80"

def test_fraction_joiner_should_join_whole_number_and_numerator():
    joiner = FractionJoiner()
    assert joiner.join(2, 1) == "2"
    assert joiner.join(10, 1) == "10"
    assert joiner.join(1, 1) == "1"

