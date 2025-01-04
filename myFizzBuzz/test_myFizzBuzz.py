import sys
import os
from myFizzBuzz import global_function

# Add the directory containing myapp.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Example usage of global_function
if __name__ == "__main__":
    result = global_function()
    # First value is 1
    assert result[0] == "1"

    # Second value is 2
    assert result[1] == "2"

    # Third value is Fizz
    assert result[2] == "Fizz"

    # Fourth value is 4
    assert result[3] == "4"

    # Sixth value is Fizz
    assert result[5] == "Fizz"


    # Fifth value is Buzz
    assert result[4] == "Buzz"

    # 15th value is FizzBuzz
    assert result[14] == "FizzBuzz"

    # 30th value is FizzBuzz
    assert result[29] == "FizzBuzz"

    # 45th value is FizzBuzz
    assert result[44] == "FizzBuzz"

    # 90th value is FizzBuzz
    assert result[89] == "FizzBuzz"

    # 99th value is Fizz
    assert result[98] == "Fizz"

    # Last value is Buzz
    assert result[-1] == "Buzz"

    print("All tests passed!")