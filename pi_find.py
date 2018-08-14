from math import sqrt
from random import randint
import matplotlib.pyplot as plt
import numpy as np

# pi ~ 4A/B where A is the number of points in the circle
# and B is the number of points total

def pos_check(x,y): #Checks if point is inside circle
    r = 100
    if sqrt(x**2 + y**2) < r:
        return True
    else:
        return False

def pi_approx(accuracy):
    a = 0.0
    b = 0.0

    plt.ion()
    fig, ax = plt.subplots()
    plot = ax.scatter([], [])
    ax.set_xlim(0.0,100.0)
    ax.set_ylim(0.0,100.0)

    circle = plt.Circle((50,50), radius = 50, fill = False)

    ax.add_artist(circle)

    for i in range(1,accuracy):

        x = randint(0.0,100.0)
        y = randint(0.0,100.0)

        point  = (x,y)
        array = plot.get_offsets()

        array = np.append(array, point)
        plot.set_offsets(array)

        if pos_check(x, y):
            a+=1
        else:
            b+=1

        fig.canvas.draw()

        print (4*a)/(b+a)

pi_approx(500)
