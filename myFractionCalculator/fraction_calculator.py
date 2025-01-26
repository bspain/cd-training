import math

from fraction_separator import FractionSeparator
from fraction_reducer import FractionReducer
from fraction_joiner import FractionJoiner
 
class FractionCalculator:
    
    def add(self, fraction1, fraction2):
        
        # numerator1, denominator1 = self.__separate(fraction1)
        # numerator2, denominator2 = self.__separate(fraction2)

        numerator1, denominator1 = self.__reduce_and_separate_fraction(fraction1)
        numerator2, denominator2 = self.__reduce_and_separate_fraction(fraction2)

        lcm = math.lcm(denominator1, denominator2)

        numerator1 = numerator1 * (lcm // denominator1)
        numerator2 = numerator2 * (lcm // denominator2)

        numerator = numerator1 + numerator2
        denominator = lcm

        return self.__join_and_reduce_fraction(numerator, denominator)
    
    def __reduce_and_separate_fraction(self, fraction):
        reduced = FractionReducer().reduce(fraction)
        return FractionSeparator().separate(reduced)
    
    def __join_and_reduce_fraction(self, numerator, denominator):
        joined = FractionJoiner().join(numerator, denominator)
        return FractionReducer().reduce(joined)
