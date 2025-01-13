from myStringCalculator.display_interface import DisplayInterface
from myStringCalculator.calculator_interface import CalculatorInterface

class StringCalcDisplay:
    def __init__(self, display: DisplayInterface, calculator: CalculatorInterface):
        self.calculator = calculator
        self.display = display

    def add(self, input: str) -> None:
        result = self.calculator.add(input)
        lastValues = self.calculator.getLastValues()
        if len(lastValues) == 0:
            return
        
        operands = ' + '.join(self.calculator.getLastValues())
        self.display.display(f"{operands} = {result}")
