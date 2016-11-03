

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def drawPlots(points):
    xs = map(lambda point: point[0], points)
    ys = map(lambda point: point[1], points)
    zs = map(lambda point: point[2], points)
    # ts = map(lambda point: point[3], points)

    ax = plt.axes(projection='3d')
    ax.plot(xs, ys, zs, '-b')
    plt.show()
