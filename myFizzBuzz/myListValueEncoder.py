import sys
import os
from abc import ABC, abstractmethod

# Add the directory containing myFizzBuzz to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ValueEncoderInterface(ABC):
    @abstractmethod
    def encode(self, value) -> str:
        pass

def encodeListOfValues(values: list, encoder: ValueEncoderInterface) -> str:
    if not isinstance(values, list):
        raise ValueError("values must be a list")
    if not isinstance(encoder, ValueEncoderInterface):
        raise ValueError("encoder must be a ValueEncoderInterface")
    return ", ".join([encoder.encode(value) for value in values])


