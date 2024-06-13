class calculator:
    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        result = 0
        index = 0
        while index < len(V1):
            result += (float(V1[index]) * float(V2[index]))
            index += 1
        print(result)

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        result = []
        index = 0
        while index < len(V1):
            result.append(float(V1[index]) + float(V2[index]))
            index += 1
        print(result)

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        result = []
        index = 0
        while index < len(V1):
            result.append(float(V1[index]) - float(V2[index]))
            index += 1
        print(result)
