class FtFilter:
    def __init__(self, function, iterable):
        self.function = function
        self.iterable = iterable

    def __iter__(self):
        if self.function is not None:
            return (i for i in self.iterable if self.function(i))
        else:
            return (i for i in self.iterable if i)

    def __repr__(self):
        return f"<ft_filter object at {id(self)}>"


def is_even(num):
        return num % 2 == 0

def main():
    """
    Test the FtFilter class.
    """
    
    made = FtFilter(is_even, [0, 1, -2, 3, 4, 5])
    print(made)
    for x in made:
        print(x)
    print(type(made))
    orginal = filter(is_even, [0, 1, -2, 3, 4, 5])
    print(orginal)
    for x in orginal:
        print(x)
    print(type(orginal))

if __name__ == "__main__":
    main()