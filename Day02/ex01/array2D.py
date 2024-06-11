import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """
    array_family = np.array(family)
    array_result = array_family[start:end]
    print(array_result.shape)
    return array_result.tolist()


def is_list(lst) -> bool:
    """
    Rreturns a boolean
    (True if the input is a list).
    """
    if type(lst) is list:
            return True
    return False

def main(family: list, start: int, end: int):
    """
    Handles error cases and slice the the family list.
    """
    if is_list(family) == True:
        result = slice_me(family, start, end)
    else:
        raise AssertionError("Inputs do not match the requirements")


if __name__ == "__main__":
    main()
