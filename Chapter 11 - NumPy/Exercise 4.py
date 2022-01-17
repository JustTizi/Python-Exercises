import numpy as np
import matplotlib.pyplot as plt


def main():
    # labels + colors
    activities = ['Cricket', 'Football', 'Hockey', 'Formula1']
    slices = [15, 30, 45, 10]
    colors = ['r', 'y', 'g', 'b']

    font = {
        'color': 'green'
    }

    # plotting the pie chart
    # labels = labels outside
    # colors = afkorting van de colors (r = red, y = yellow...)
    # startangle = starting point for rotating
    # explode = ruimte tussen pie slices
    # radius = straal
    # autopct = na comma
    plt.pie(slices, labels=activities, colors=colors,
            startangle=0, explode=(0, 0, 0, 0),
            radius=1.2, autopct='%1.1f%%')
    plt.title('Sports', fontdict=font)
    plt.show()


if __name__ == '__main__':
    main()
