import numpy as np
import matplotlib.pyplot as plt


def main():
    with open('Files_Chapter_11/degrees_fahrenheit.txt') as file:
        days = []
        temperature_fahrenheit = []
        temperature_celsius = []
        line = file.readline()

        while line:
            record = line.split(';')
            days.append(int(record[0]))
            temperature_fahrenheit.append(float(record[1]))
            line = file.readline()

        print(temperature_fahrenheit)
        for fahrenheit in temperature_fahrenheit:
            temperature_celsius.append((fahrenheit - 32) * 5 / 9)

        ypoints = np.array(temperature_celsius)
        xpoints = np.array(days)

        # plotting x and y
        plt.plot(xpoints, ypoints)
        # naming stuff
        plt.title('Degrees Celsius')
        plt.ylabel('Temperatures')
        plt.xlabel('Datapoints')
        # show
        plt.show()


if __name__ == '__main__':
    main()
