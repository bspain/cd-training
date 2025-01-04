import sys
import os
from string_calc import StringCalc

# Add the directory containing myapp.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_should_return_zero_for_empty_string():
    assert StringCalc().add("") == 0

def test_should_return_number_for_single_number():
    assert StringCalc().add("1") == 1
    assert StringCalc().add("2") == 2
    assert StringCalc().add("3") == 3
    assert StringCalc().add("4") == 4
    assert StringCalc().add("5") == 5

def test_should_return_sum_for_two_numbers():
    assert StringCalc().add("1,2") == 3
    assert StringCalc().add("2,3") == 5
    assert StringCalc().add("3,4") == 7
    assert StringCalc().add("4,5") == 9
    assert StringCalc().add("5,6") == 11

def test_should_return_sum_for_multiple_numbers():
    assert StringCalc().add("1,2,3") == 6
    assert StringCalc().add("2,3,4") == 9
    assert StringCalc().add("3,4,5") == 12
    assert StringCalc().add("4,5,6") == 15
    assert StringCalc().add("5,6,7") == 18

def test_should_return_sum_for_new_line_delimiter():
    assert StringCalc().add("1\n2,3") == 6
    assert StringCalc().add("2\n3,4") == 9
    assert StringCalc().add("3\n4,5") == 12
    assert StringCalc().add("4\n5,6") == 15
    assert StringCalc().add("5\n6,7") == 18

def test_should_return_sum_for_custom_delimiter():
    assert StringCalc().add("//;\n1;2") == 3
    assert StringCalc().add("//`\n5`6") == 11

    # Stuff that is a regex special character
    #  In true TDD fashion: the test should not care about the implementation details.
    # These are valuable tests, but they should not be written assuming the implementation is regex based.
    assert StringCalc().add("//+\n2+3") == 5
    assert StringCalc().add("//.\n3.4") == 7
    assert StringCalc().add("//*\n4*5") == 9
    assert StringCalc().add("//[\n5[6") == 11
