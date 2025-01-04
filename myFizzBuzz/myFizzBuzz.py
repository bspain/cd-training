def global_function():
    #return ["1", "2", "Fizz", "100"]

    result = []
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            continue

        if i % 3 == 0:
            result.append("Fizz")
            continue

        if i % 5 == 0:
            result.append("Buzz")
            continue

        result.append(str(i))
    return result