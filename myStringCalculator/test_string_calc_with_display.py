import sys
import os
from myStringCalculator.string_calc import StringCalc
from myStringCalculator.string_calc_display import StringCalcDisplay
from myStringCalculator.display_interface import DisplayInterface

# Add the directory containing string_calc_with_display.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Display(DisplayInterface):
    def __init__(self):
        self.output = ""

    def display(self, message: str):
        self.output += message

    def clear(self):
        self.output = ""
    
    def get_display(self):
        return self.output

def test_should_display_nothing_for_empty_string():
    c = StringCalc()
    d = Display()
    sc = StringCalcDisplay(d, c)
    
    sc.add("")
    assert d.get_display() == ""

def test_should_display_operands_and_sum():
    c = StringCalc()
    d = Display()
    sc = StringCalcDisplay(d, c)
    
    sc.add("1,2")
    assert d.get_display() == "1 + 2 = 3"

def test_should_display_operands_and_sum_for_multiple_numbers():
    c = StringCalc()
    d = Display()
    sc = StringCalcDisplay(d, c)
    
    sc.add("//;\n1;2;3")
    assert d.get_display() == "1 + 2 + 3 = 6"
