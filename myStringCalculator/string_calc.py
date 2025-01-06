import re

class StringCalc:
    def add(self, input: str) -> int:
        total = 0
        if input != "":
            numbers = self._get_split_values(input)

            for number in numbers:
                if int(number) < 0:
                    raise ValueError(f"Negatives not allowed: {', '.join([n for n in numbers if int(n) < 0])}")
                total += int(number)
        return total    
    
    def _get_split_values(self, input: str) -> list[str]:
        # If the input string starts with '//'
        split_token = r'[,\n]'
        if input.startswith("//"):
            # Split the input string by '\n'
            tokens = input.split('\n')
            
            # Get the delimiter from the first token (escaping for any regex special characters)
            split_token = re.escape(tokens[0][2:])

            # Get the input string from the second token
            input = tokens[1]

        # Split the input string by the split token
        return re.split(split_token, input)
