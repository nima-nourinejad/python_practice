def callLimit(limit: int):
    """A decorator factory: a specific type of higher order function which the inner function receives a function as input"""
    count = 0

    def callLimiter(function):
        nonlocal count

        def limit_function(*args, **kwds):
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print(f"<function {function} at {hex(id(function))}\
call too many times")
        return limit_function
    return callLimiter
