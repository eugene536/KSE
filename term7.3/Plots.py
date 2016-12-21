import matplotlib.pyplot as plt

fig = plt.figure()

def createAx(x):
    global fig
    return fig.add_subplot(x)

plot_x = createAx(211)
plot_t = createAx(212)

def drawPlots(ax, xs, fs):
    ax.cla()
    ax.plot(fs, xs)


def showPlots():
    plt.show()

