import sys
import os
import math
import pytest
import re
from fraction_reducer import FractionReducer

# Add the directory containing myFractionCalculator to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_verify_my_understanding_of_gcd():
    assert math.gcd(1, 1) == 1
    assert math.gcd(1, 2) == 1
    assert math.gcd(2, 4) == 2
    assert math.gcd(3, 4) == 1
    assert math.gcd(4, 6) == 2
    assert math.gcd(8, 6) == 2
    assert math.gcd(15, 20) == 5

def test_should_reduce_fraction_to_lowest_terms():
    reducer = FractionReducer()
    assert reducer.reduce(1, 1) == [1, 1]
    assert reducer.reduce(1, 2) == [1, 2]
    assert reducer.reduce(2, 4) == [1, 2]
    assert reducer.reduce(4, 6) == [2, 3]
    assert reducer.reduce(5, 10) == [1, 2]
    assert reducer.reduce(6, 9) == [2, 3]