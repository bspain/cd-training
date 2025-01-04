import re

class StringCalc:
    def add(self, input: str) -> int:
        total = 0
        if input != "":
            split_token = r'[,\n]'

            # If the input string starts with '//'
            if input.startswith("//"):
                # Split the input string by '\n'
                tokens = input.split('\n')
                
                # Get the delimiter from the first token (escaping for any regex special characters)
                split_token = re.escape(tokens[0][2:])

                # Get the input string from the second token
                input = tokens[1]


            # Split the input string by the split token
            numbers = re.split(split_token, input)

            for number in numbers:
                total += int(number)
        return total    
    
    def contains_regex_tokens(self, input: str) -> bool:
        return input != re.escape(input)