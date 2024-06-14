import numpy as np


def check_args(args) -> bool:
    """
    Check if all elements in args are either int or float.
    """
    if len(args) == 0:
        return False
    for item in args:
        if not isinstance(item, (int, float)):
            return False
    return True


def check_kwargs(item) -> bool:
    """
    Check if item in lst_kwargs is among the accepted keywords.
    """
    valid_keywords = {"mean", "median", "quartile", "var", "std"}
    if item not in valid_keywords:
        return False
    return True


def run(item, *args) -> float:
    """
    Run the specified statistical operation on the given arguments.
    """
    if item == "mean":
        return np.mean(args)
    elif item == "median":
        return np.median(args)
    elif item == "quartile":
        result = [np.quantile(args, 0.25), np.quantile(args, 0.75)]
        return result
    elif item == "var":
        return np.var(args)
    elif item == "std":
        return np.std(args)
    else:
        raise ValueError(f"Invalid operation: {item}")


def ft_statistics(*args, **kwargs) -> None:
    try:
        lst_kwargs = list(kwargs.values())
        if (check_args(args)):
            for item in lst_kwargs:
                if not check_kwargs(item):
                    print("ERROR")
                else:
                    result = run(item, *args)
                    print(f"{item} : {result}")
        else:
            print("ERROR")
    except Exception as e:
        print(e)
