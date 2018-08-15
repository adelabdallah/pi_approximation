from math import sqrt
from random import randint
import matplotlib.pyplot as plt
import numpy

# pi ~ 4A/B where A is the number of points in the circle
# and B is the number of points total


def pos_check(x, y):
    # Checks if point is inside circle

    r = 100
    if sqrt(x**2 + y**2) < r:
        return True
    else:
        return False


def pi_approx(accuracy):
    a = float(0)
    b = float(0)

    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(0.0, 100.0)
    ax.set_ylim(0.0, 100.0)

    circle = plt.Circle((50, 50), radius=50, fill=False)

    ax.add_artist(circle)

    for i in range(1, accuracy):

        x = randint(0.0, 100.0)
        y = randint(0.0, 100.0)

        if pos_check(x, y):
            a += 1.0
        else:
            b += 1.0

        plt.scatter(x, y)

        fig.canvas.draw()

        numerator = float(4*a)
        denominator = float(b+a)

        print(numerator/denominator)


pi_approx(500)
