import matplotlib.pyplot as plt


def drawPlots(points):
    print("called")
    xs = map(lambda point: point[0], points)
    ys = map(lambda point: point[1], points)
    zs = map(lambda point: point[2], points)
    ts = map(lambda point: point[3], points)

    plt.plot(ts, xs)
    plt.plot(ts, ys)
    plt.plot(ts, zs)

    plt.show()