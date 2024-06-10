

def all_thing_is_obj(object: any) -> int:
    di = {}
    if object:
        ty = str(type(object))
        cat = str(ty.split("'")[1])
        cat = cat.capitalize()
        if cat != "Str" and cat != "Int":
            print(f"{cat} : {ty}")
        elif cat != "Int":
            print(f"{object} is in the kitchen : {ty}")
        else:
            print(f"Type not found")

    return (42)