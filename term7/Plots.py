import matplotlib.pyplot as plt

def drawPlots(points):
    xs = map(lambda point: point[0], points)
    ys = map(lambda point: point[1], points)
    zs = map(lambda point: point[2], points)
    ts = map(lambda point: point[3], points)

    #if (drawPlots.printed == 1):
    #    plt.clf()
    plt.clf()
    plt.plot(ts, xs)
    plt.plot(ts, ys)
    plt.plot(ts, zs)
    plt.show()

    #if (drawPlots.printed == 0):
    #    plt.show()
    #    drawPlots.printed = 1

#drawPlots.printed = 0
