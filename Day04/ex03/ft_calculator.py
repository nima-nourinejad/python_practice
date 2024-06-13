class calculator:
    def __init__(self, list) -> None:
        self.list = list

    def __add__(self, object) -> None:
        result = []
        for item in self.list:
            result.append(item + object)
        self.list = result
        print(result)

    def __mul__(self, object) -> None:
        result = []
        for item in self.list:
            result.append(item * object)
        self.list = result
        print(result)

    def __sub__(self, object) -> None:
        result = []
        for item in self.list:
            result.append(item - object)
        self.list = result
        print(result)

    def __truediv__(self, object) -> None:
        result = []
        for item in self.list:
            result.append(item / object)
        self.list = result
        print(result)
