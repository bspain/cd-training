import math

class FractionCommonDenominator:
    def calculate(self, denominator1, denominator2):
        if denominator1 == denominator2:
            return 1
        else:
            return math.lcm(denominator1, denominator2)