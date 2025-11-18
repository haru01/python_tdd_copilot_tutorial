def fizzbuzz(number):
    """Return Fizz/Buzz/FizzBuzz or the number as a string.

    Contract:
    - input must be an int, otherwise TypeError is raised.
    - returns "FizzBuzz" if number is divisible by 15 (including 0).
    - returns "Fizz" if divisible by 3.
    - returns "Buzz" if divisible by 5.
    - otherwise returns str(number).
    """
    if not isinstance(number, int):
        raise TypeError("number must be an int")

    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
