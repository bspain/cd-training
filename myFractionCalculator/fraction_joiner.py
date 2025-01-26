class FractionJoiner:
    def join(self, numerator, denominator):
        return f"{numerator}/{denominator}" if denominator != 1 else f"{numerator}"