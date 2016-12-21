import matplotlib.pyplot as plt

def drawPlots(xs, fs):
    #if (drawPlots.printed == 1):
#    plt.clf()
    print("xs = ", xs)
    print("fs = ", fs)
    plt.clf()
    plt.plot(fs, xs)
    plt.show()

    #if (drawPlots.printed == 0):
    #    plt.show()
    #    drawPlots.printed = 1

#drawPlots.printed = 0
