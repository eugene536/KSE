# coding=utf-8
import matplotlib.pyplot as plt

from tkinter import *
from algo import *
from Constants import *

import time

import Plots
from Plots import *

sys.setrecursionlimit(3500)

root = Tk()

graph_x = []
graph_T = []
xs = []

cur_t = 0

btn1 = Button(root, text="Start")
btn1.grid(row=1, column=2)

lastUpdate = 0


def currentAlgorithm_(*_, **__):
    global graph_x
    global xs
    graph_x = [
        [10, 20, 14, 16, 18],
        [10, 20, 14, 16, 18],
        [10, 20, 14, 16, 18]
    ]
    # print(graph_x)

    xs = [1, 2, 3, 4, 5]
    return graph_x

def draw():
    tm = scl_time.get()

    xs = list(drange(0, H, 0.5))
    graph_x = list(map(lambda x: getX(tm, x), xs))
    print("xs:", xs)
    print("graph_x:", graph_x)
    drawPlots(plot_x, graph_x, xs)

    graph_T = list(map(lambda x: getT(tm, x), xs))

    print("xs_t:", xs)
    print("graph_t:", graph_T)
    drawPlots(plot_t, graph_T, xs)

    showPlots()

def makeWork():
    def work(*_):
        global lastUpdate

        nlast = int(round(time.time() * 1000))
        if (nlast - lastUpdate < 200): return
        lastUpdate = nlast

        draw()

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

def createEntry(text, default = "0"):
    global cur_row
    lbl = Label(root, text=text)
    lbl.grid(row=cur_row, column=1)
    # scl = Scale(root, from_=l, to=r, resolution=resolution, length=1000, orient=HORIZONTAL)
    entry = Entry(root, width=124)
    entry.grid(row=cur_row, column=2)
    entry.insert(0, default)
    cur_row += 1
    return entry


maxT = 100

# scl_kappa = createScroll("æ")
# scl_dtime = createScroll("Δt")
# scl_d = createScroll("D", 10 ** 6, 10 ** 8, 5 * 10 ** 5)
def e_f(k):
    return "%.1e" % k

resolution_time = totalTime / cntTime

scl_time = createScroll("t", 0, totalTime , resolution_time, False)
ent_d = createEntry("D", e_f(D))
ent_k = createEntry("K", e_f(K))
ent_alpha = createEntry("alpha [0.5, 3]", e_f(0.5))
scl_unused = createScroll("")


def drange(start, stop, step):
    r = start
    while r <= stop:
        yield r
        r += step


def start(*_):
    global graph_x
    global xs
    print("start")
    # createFigure()
    d = float(ent_d.get())
    k = float(ent_k.get())
    alpha_ = float(ent_alpha.get())

    calc(Tm, T0, H, cntH, totalTime, cntTime, ro, C, d, lam, Q, k, R, E, alpha_)
    draw()
    # graph_x = currentAlgorithm_()


def change_time(*_):
    print("CHANGE TIME")
    Plots.drawPlots(graph_x[int(scl_time.get())], xs)


btn1.config(command=start)

calc(Tm, T0, H, cntH, totalTime, cntTime, ro, C, D, lam, Q, K, R, E, alpha)
root.mainloop()
