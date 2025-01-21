import math

from fraction_reducer import FractionReducer
from fraction_separator import FractionSeparator
 
class FractionCalculator:
    
    def add(self, fraction1, fraction2):
        
        numerator1, denominator1 = self.__separate(fraction1)
        numerator2, denominator2 = self.__separate(fraction2)

        numerator1, denominator1 = self.__reduce__fraction(numerator1, denominator1)
        numerator2, denominator2 = self.__reduce__fraction(numerator2, denominator2)

        lcm = math.lcm(denominator1, denominator2)

        numerator1 = numerator1 * (lcm // denominator1)
        numerator2 = numerator2 * (lcm // denominator2)

        numerator = numerator1 + numerator2
        denominator = lcm

        numerator, denominator = self.__reduce__fraction(numerator, denominator)

        if denominator == 1:
            return f"{numerator}"
        return f"{numerator}/{denominator}"

    
    def __separate(self, fraction):
        return FractionSeparator().separate(fraction)
    
    def __reduce__fraction(self, numerator, denominator):
        return FractionReducer().reduce(numerator, denominator)
