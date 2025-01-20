import sys
import os
from myFizzBuzz import fizzbuzz

# Add the directory containing myFizzBuzz to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_render_a_values_for_non_fizzbuzz_numbers():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(97) == "97"
    assert fizzbuzz(98) == "98"

def test_should_render_Fizz_for_values_of_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_should_render_Buzz_for_values_of_five():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"

def test_should_render_FizzBuzz_for_values_of_fifteen():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
