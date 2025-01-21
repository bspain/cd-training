import sys
import os
import pytest
import re
from fraction_primes import FractionPrimes

# Add the directory containing myFractionCalculator to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_return_only_one_and_itself_for_prime_numbers():
    assert FractionPrimes().getPrimes(1) == [1]
    assert FractionPrimes().getPrimes(2) == [1, 2]
    assert FractionPrimes().getPrimes(3) == [1, 3]
    assert FractionPrimes().getPrimes(5) == [1, 5]

def test_should_return_empty_list_for_numbers_less_than_one():
    assert FractionPrimes().getPrimes(0) == []
    assert FractionPrimes().getPrimes(-1) == []

def test_should_return_list_of_primes_for_non_prime_numbers():
    assert FractionPrimes().getPrimes(4) == [1, 2]
    assert FractionPrimes().getPrimes(6) == [1, 2, 3]
    assert FractionPrimes().getPrimes(8) == [1, 2]
    assert FractionPrimes().getPrimes(9) == [1, 3]