import pandas as pd
import sys


def load(path: str):
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as e:
        print(e)


def main(path: str):
    """
    Run load.
    """
    args = sys.argv
    if len(args) == 2:
        path = sys.argv[1]
        load(path)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
