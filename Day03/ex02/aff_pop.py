from load_csv import load
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np


def replace_Mk(item):
    if 'M' in item:
        item = item.replace('M', '')
        result = float(item) * 1_000_000
    elif 'k' in item:
        item = item.replace('k', '')
        result = float(item) * 1_000
    return result


def create_float_array(array):
    lst1 = array.tolist()
    new_lst1 = []
    for item in lst1:
        new_lst1.append(replace_Mk(item))
    array = np.array(new_lst1)
    return array


def find_max_y_value(pop1, pop2):
    max2 = np.max(pop2)
    max1 = np.max(pop1)
    max = max2
    if max1 > max2:
        max = max1
    n = ((int(max) // 20_000_000) + 1) * 20_000_000
    return n


def plot(dataset: pd.DataFrame, country1: str, country2: str):
    try:
        data1 = dataset[dataset['country'] == country1]
        pop1 = create_float_array(data1.values.ravel()[1:])
        data2 = dataset[dataset['country'] == country2]
        pop2 = create_float_array(data2.values.ravel()[1:])
        n = find_max_y_value(pop1, pop2)
        years = data1.columns[1:].values
        plt.plot(years, pop1)
        plt.plot(years, pop2)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(years[::40])
        y_ticks = range(0, int(n), 20_000_000)
        y_labels = [f"{tick // 1_000_000}M" for tick in y_ticks]
        plt.yticks(y_ticks, y_labels)
        plt.legend([country1, country2], loc='lower right')
        plt.show()
    except Exception as e:
        print(e)


def main():
    """
    Run load and plot.
    """
    args = sys.argv
    if len(args) == 4:
        path = sys.argv[1]
        country1 = sys.argv[2]
        country2 = sys.argv[3]
        data_set = load(path)
        plot(data_set, country1, country2)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
