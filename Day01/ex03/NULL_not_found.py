def NULL_not_found(object: any) -> int:
    types = type(object)
    if object == None:
        print(f"Nothing: {object} {types}")
    elif object != object and type(object) is float:
        print(f"Cheese: {object} {types}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {types}")
    elif object == '' and type(object) is str:
        print(f"Empty: {object} {types}")
    elif object == False and type(object) is bool:
        print(f"Fake: {object} {types}")
    else:
        print(f"Type not Found")
        return 1
    return 0