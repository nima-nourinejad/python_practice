from load_csv import load
import pandas as pd
import sys
import matplotlib.pyplot as plt


def plot(dataset: pd.DataFrame, country: str):
    try:
        title_str = f"{country} Life expectency Projections"
        data = dataset[dataset['country'] == country]
        years = data.columns[1:].values
        life = data.values.ravel()[1:]
        plt.plot(years, life)
        plt.title(title_str)
        plt.xlabel("Year")
        plt.ylabel("Life expectency")
        plt.xticks(years[::40])
        plt.show()
    except Exception as e:
        print(e)


def main():
    """
    Run load and plot.
    """
    args = sys.argv
    if len(args) == 3:
        path = sys.argv[1]
        country = sys.argv[2]
        data_set = load(path)
        plot(data_set, country)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
