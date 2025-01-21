from sympy import primefactors

class FractionPrimes:
    def getPrimes(self, n):
        if n < 1:
            return []
        elif n == 1:
            return [1]
        else:
            return [1] + primefactors(n)