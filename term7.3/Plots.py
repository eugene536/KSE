import matplotlib.pyplot as plt

def createAx():
    f = plt.figure()
    return f.add_subplot(111)


def drawPlots(ax, xs, fs):
    ax.cla()
    ax.plot(fs, xs)


def showPlots():
    plt.show()

