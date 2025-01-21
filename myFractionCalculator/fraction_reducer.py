import math

class FractionReducer:
    def reduce(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return [numerator // gcd, denominator // gcd]
