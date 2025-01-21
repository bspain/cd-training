import sys
import os
from fraction_calculator import FractionCalculator

# Add the directory containing myFractionCalculator to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_add_two_fractions():
    calculator = FractionCalculator()
    assert calculator.add("1/2", "1/2") == "1"
    assert calculator.add("1/4", "1/4") == "1/2"
    assert calculator.add("1/4", "3/4") == "1"
    assert calculator.add("1/2", "1/4") == "3/4"
    assert calculator.add("1/2", "1/3") == "5/6"
    assert calculator.add("1/2", "1") == "3/2"
    assert calculator.add("1/2", "2") == "5/2"
    assert calculator.add("1", "1") == "2"
    assert calculator.add("1", "2") == "3"
    assert calculator.add("2", "2") == "4"

    assert calculator.add("5/8", "5/10") == "9/8"
    assert calculator.add("5/8", "3/4") == "11/8"
