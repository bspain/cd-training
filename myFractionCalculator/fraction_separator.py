class FractionSeparator:
    def separate(self, fraction):
        value_error_message = "All fraction components (whole number, numerator, or denominator) must be an integer."
        if "/" not in fraction:
            if not fraction.isdigit():
                raise ValueError(value_error_message)
            return int(fraction), 1
        else:
            numerator, denominator = fraction.split("/")
            if not numerator.isdigit():
                raise ValueError(value_error_message)
            if not denominator.isdigit():
                raise ValueError(value_error_message)
            return int(numerator), int(denominator)
