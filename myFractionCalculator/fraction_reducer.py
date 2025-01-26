import math

from fraction_separator import FractionSeparator
from fraction_joiner import FractionJoiner

class FractionReducer:
    def reduce(self, fraction):
        numerator, denominator = self._separate(fraction)
        numerator, denominator = self._reduce_separated_fraction(numerator, denominator)
        return self._join(numerator, denominator)
    
    def _separate(self, fraction):
        return FractionSeparator().separate(fraction)

    def _reduce_separated_fraction(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return [numerator // gcd, denominator // gcd]
    
    def _join(self, numerator, denominator):
        return FractionJoiner().join(numerator, denominator)
