# Tiziano Van der Waals r0889630 1ITF3

import numpy as np
import matplotlib.pyplot as plt


def main():
    with open("city_population.txt") as file:
        split_data = []
        group_sizes = []
        group_names = []
        sum = 0
        line = file.readline()
        line = file.readline()

        while line:
            record = line.split("#")
            group_names.append(record[0])
            group_sizes.append(int(record[1]))
            line = file.readline()

        for i in range(len(group_sizes)):
            sum += group_sizes[i]

        plt.pie(group_sizes, labels=group_names, autopct="%1.0f%%")
        plt.title(f"Population per city\nTotal population in cities: {sum}")
        donut = plt.Circle((0, 0), 0.7, color="white")
        p = plt.gcf()
        p.gca().add_artist(donut)
        plt.show()


if __name__ == "__main__":
    main()
