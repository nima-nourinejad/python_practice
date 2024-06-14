def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function):
    """A higher order function: Takes one or more functions as arguments and/or Returns a function as its result"""
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        result = x
        for i in range(count):
            result = function(result)
        return result

    return inner
