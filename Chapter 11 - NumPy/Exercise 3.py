import numpy as np
import matplotlib.pyplot as plt


def main():
    with open('Files_Chapter_11/Temperatures.txt') as file:
        days = []
        temperature = []
        line = file.readline()

        while line:
            record = line.split(',')
            days.append(int(record[0]))
            temperature.append(int(record[1]))
            line = file.readline()

        ypoints = np.array(temperature)
        xpoints = np.array(days)
        xs = range(len(xpoints))

        # plotting x en y
        # plt.plot(xpoints, ypoints)
        plt.plot(xs, ypoints)
        # change x-as
        plt.xticks(xs, xpoints)
        # naming title, y-as and x-as
        plt.title('Temperature measurements')
        plt.ylabel('Temperature')
        plt.xlabel('Days')
        # showing plot
        plt.show()


if __name__ == '__main__':
    main()
