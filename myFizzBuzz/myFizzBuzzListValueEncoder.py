import sys
import os

from myFizzBuzz import fizzbuzz
from myListValueEncoder import ValueEncoderInterface


# Add the directory containing myFizzBuzz to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class FizzBuzzValueEncoder(ValueEncoderInterface):
    def encode(self, value):
        return fizzbuzz(value)
