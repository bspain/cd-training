import sys
import os

from myFizzBuzzListValueEncoder import FizzBuzzValueEncoder
from myListValueEncoder import encodeListOfValues

# Add the directory containing myFizzBuzz to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_encode_values_for_non_fizzbuzz_numbers():
    encoder = FizzBuzzValueEncoder()
    assert encodeListOfValues([1], encoder) == "1"

def test_should_encode_values_for_fizzbuzz_numbers():
    encoder = FizzBuzzValueEncoder()
    assert encodeListOfValues([3], encoder) == "Fizz"
    assert encodeListOfValues([5], encoder) == "Buzz"
    assert encodeListOfValues([15], encoder) == "FizzBuzz"

def test_should_encode_values_for_multiple_fizzbuzz_numbers():
    encoder = FizzBuzzValueEncoder()
    assert encodeListOfValues([3, 5, 15], encoder) == "Fizz, Buzz, FizzBuzz"

def test_should_render_final_11_values_correctly_given_an_array_of_all_numbers_1_to_100():
    results = encodeListOfValues(list(range(1, 101)), FizzBuzzValueEncoder())
    tailEndOfResults = "FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz"
    assert results[-len(tailEndOfResults):] == tailEndOfResults
