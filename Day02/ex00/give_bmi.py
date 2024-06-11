import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Take 2 lists of integers or floats in input and returns a list
    of BMI values.
    """
    array_height = np.array(height)
    array_weight = np.array(weight)
    array_bmi = array_weight / (array_height ** 2)
    return array_bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Accepts a list of integers or floats and an integer
    representing a limit as parameters.
    It returns a list of booleans (True if above the limit).
    """
    bmi_array = np.array(bmi)
    limit_array = np.array(limit)
    result_array = bmi_array > limit_array
    return result_array.tolist()

def check_float_or_int(lst: list) -> bool:
    """
    Accepts a list and it returns a boolean
    (True if all the members are int or float).
    """
    len = len (lst)
    i = 0
    while i < len:
        if type(lst[i]) is not int and type(lst[i]) is not float:
            return False
    return True

def same_length(lst1: list, lst2: list, lst3: list) -> bool:
    """
    Accepts a three lists and it returns a boolean
    (True if the two lists have the size).
    """
    len1 = len (lst1)
    len2 = len(lst2)
    len3 = len(lst3)

    if len1 == len2 and len1 == len3:
            return True
    return False

def input_cehck(lst1: list, lst2: list, lst3: list) -> bool:
    """
    Total input check
    """
    if same_length(lst1, lst2, lst3) == False:
         return False
    if check_float_or_int(lst1) == False:
         return False
    if check_float_or_int(lst2) == False:
         return False
    if check_float_or_int(lst3) == False:
         return False
    return (True)


def main(height, weight, limit):
    """
    Handles error cases if the lists are not the same size,
    are not int or float and make bmi and apply limit.
    """
    if input_cehck(height, weight, limit):
        bmi = give_bmi(height, weight)
        result = apply_limit(bmi, limit)
    else:
        raise AssertionError("Inputs do not match the requirements")


if __name__ == "__main__":
    main()
