# coding=utf-8
import matplotlib.pyplot as plt

from tkinter import *
from vanya import *

import time

import Plots

sys.setrecursionlimit(3500)

root = Tk()

graph_x = []
graph_T = []
xs = []

cur_t = 0

btn1 = Button(root, text="Start")
btn1.grid(row=1, column=1)
btn_left = Button(root, text="Left explicit")
btn_left.grid(row=1, column=2)
btn_right = Button(root, text="Right explicit")
btn_right.grid(row=1, column=3)
btn_chech = Button(root, text="Чехарда")
btn_chech.grid(row=1, column=4)
btn_left_i = Button(root, text="Left implicit")
btn_left_i.grid(row=1, column=5)
btn_right_i = Button(root, text="Right implicit")
btn_right_i.grid(row=1, column=6)

# def getStartPoint():
#    print "getting start point"
#    return scl1.get(), scl2.get(), scl3.get(), scl4.get()

lastUpdate = 0


def currentAlgorithm_(*_, **__):
    global graph_x
    global xs
    graph_x = [
        [10, 20, 14, 16, 18],
        [10, 20, 14, 16, 18],
        [10, 20, 14, 16, 18]
    ]
    print(graph_x)

    xs = [1, 2, 3, 4, 5]
    return graph_x


currentAlgorithm = currentAlgorithm_


def makeWork():
    def work(*_):
        global lastUpdate
        nlast = int(round(time.time() * 1000))
        if (nlast - lastUpdate < 200): return
        lastUpdate = nlast
        print("working")
        # currentAlgorithm()
        # Plots.drawPlots(currentAlgorithm(scl1.get(), scl2.get(), scl3.get(), scl4.get(), scl5.get()))
        start()
        Plots.drawPlots(graph_x[int(scl_time.get())], xs)
        return

    return work


cur_row = 2


def createScroll(text, l=0, r=2, resolution=None, mid=True):
    if resolution == None:
        resolution = (r - l) / 50.0
    global cur_row
    lbl = Label(root, text=text)
    lbl.grid(row=cur_row, column=1)
    scl = Scale(root, from_=l, to=r, resolution=resolution, length=1000, orient=HORIZONTAL)
    if mid:
        scl.set((l + r) / 2)
    else:
        scl.set(0)
    scl.grid(row=cur_row, column=2)
    scl.config(command=makeWork())
    cur_row += 1
    return scl


maxT = 100

# scl_kappa = createScroll("æ")
# scl_dtime = createScroll("Δt")
# scl_dx = createScroll("Δx")
scl_alpha = createScroll("alpha", 0.5, 3, 0.5)
scl_time = createScroll("t", 0, 2, False)
scl_unused = createScroll("")


def makeCurrentAlgorithm(algorithm):
    def work(*_):
        print("HEEEELLOO")
        global currentAlgorithm
        print("change")
        currentAlgorithm = algorithm
        start()
        change_time()

    return work


def drange(start, stop, step):
    r = start
    while r <= stop:
        yield r
        r += step


def start(*_):
    print("HEEEELLOO")
    global graph_x
    global xs
    # Plots.drawPlots(graph[0])
    # maxX = scl_x.get()
    # dx = scl_dx.get()
    graph_x = currentAlgorithm()
    # xs = list(drange(-maxX, maxX, dx))
    print("xs=", xs)
    print("xs=", len(xs))
    print("graph[0] = ", graph_x[0])
    print("graph[0] = ", len(graph_x[0]))
    # plt.show()


# start()

def change_time(*_):
    print("CHANGE TIME")
    Plots.drawPlots(graph_x[int(scl_time.get())], xs)


btn1.config(command=start)

# btn_left.config(command=makeCurrentAlgorithm(ExplicitLeftAlgo))
# btn_right.config(command=makeCurrentAlgorithm(ExplicitRightAlgo))
# btn_chech.config(command=makeCurrentAlgorithm(ChehAlgo))
# btn_left_i.config(command=makeCurrentAlgorithm(ImplicitLeftAlgo))
# btn_right_i.config(command=makeCurrentAlgorithm(ImplicitRightAlgo))


# btn4.config(command=test)
# scl_time.config(command=change_time)
# scl2.config(command=makeWork())
# scl3.config(command=makeWork())
# scl4.config(command=makeWork())


# print(time.clock())
# print(int(round(time.time() * 1000)))
# time.sleep(3)
# print(time.clock())
# print(int(round(time.time() * 1000)))

root.mainloop()
