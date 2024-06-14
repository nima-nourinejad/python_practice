def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        nonlocal count

        def limit_function(*args, **kwds):
            nonlocal count
            nonlocal function
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print(f"<function {function} at {hex(id(function))}\
                      call too many times")
        return limit_function
    return callLimiter
