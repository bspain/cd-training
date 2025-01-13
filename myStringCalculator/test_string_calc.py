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

def test_should_throw_a_ValueError_exception_for_negative_number():
    try:
        StringCalc().add("-1,2")
        assert False
    except ValueError as e:
        assert str(e) == "Negatives not allowed: -1"
        
def test_should_throw_exception_for_negative_numbers_with_message_containing_all_negative_values():
    try:
        StringCalc().add("-1,-3")
        assert False
    except ValueError as e:
        assert str(e) == "Negatives not allowed: -1, -3"

# Added in response to the new requirement that the last values used in the calculation should be returned for display purposes.
# Nice that, in python, this meants seemless switching between class and instance methods.
def test_should_return_all_values_used_in_last_calulation():
    c = StringCalc()
    assert c.add("1,2") == 3
    assert c.getLastValues() == ["1", "2"]

    assert c.add("3,4") == 7
    assert c.getLastValues() == ["3", "4"]

# These tests are examples of testing the specific implementation details by calling interal private methods.
# In TDD, these types of tests are not recommended because they are coupled to the implementation.
# I believe there is value in these tests, but they should somehow be denoted as (optional) such that if/when the code is refactored, these tests should be considered disposable.
def test_get_split_values_should_use_default_delimiter():
    assert StringCalc()._get_split_values("1,2,3") == ["1", "2", "3"]
    assert StringCalc()._get_split_values("2\n3\n4") == ["2", "3", "4"]
    assert StringCalc()._get_split_values("3\n4,5") == ["3", "4", "5"]

def test_get_split_values_should_use_custom_delimiter():
    assert StringCalc()._get_split_values("//;\n1;2") == ["1", "2"]
    assert StringCalc()._get_split_values("//`\n5`6") == ["5", "6"]
    assert StringCalc()._get_split_values("//+\n2+3") == ["2", "3"]
    assert StringCalc()._get_split_values("//.\n3.4") == ["3", "4"]
    assert StringCalc()._get_split_values("//*\n4*5") == ["4", "5"]
    assert StringCalc()._get_split_values("//[\n5[6") == ["5", "6"]