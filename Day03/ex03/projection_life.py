from load_csv import load
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np


def plot(dataset1: pd.DataFrame, dataset2: pd.DataFrame, year: str):
    try:
        life = dataset1[year]
        income = dataset2[year]
        plt.scatter(np.array(income), np.array(life), marker='o')
        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectency")
        plt.xscale('log')
        x_ticks = [300, 1000, 10000]
        x_labels = ['300', '1k', '10k']
        plt.xticks(x_ticks, x_labels)
        plt.show()
    except Exception as e:
        print(e)


def main():
    """
    Run load and plot.
    """
    args = sys.argv
    if len(args) == 4:
        path1 = sys.argv[1]
        path2 = sys.argv[2]
        year = sys.argv[3]
        data_set1 = load(path1)
        data_set2 = load(path2)
        plot(data_set1, data_set2, year)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
