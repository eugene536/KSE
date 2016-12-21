# coding=utf-8
import matplotlib.pyplot as plt

from Tkinter import *
from vanya import *


import time

import Plots
import Plots3d


sys.setrecursionlimit(3500)

root = Tk()


graph = []
xs = []

cur_t = 0

btn1 = Button(root, text="Start")
btn1.grid(row = 1, column = 1)
btn_left = Button(root, text="Left explicit")
btn_left.grid(row = 1, column = 2)
btn_right = Button(root, text="Right explicit")
btn_right.grid(row = 1, column = 3)
btn_chech = Button(root, text="Чехарда")
btn_chech.grid(row = 1, column = 4)
btn_left_i = Button(root, text="Left implicit")
btn_left_i.grid(row = 1, column = 5)
btn_right_i = Button(root, text="Right implicit")
btn_right_i.grid(row = 1, column = 6)

btnSwitch = Button(root, text="Переключатель")
btnSwitch.grid(row = 5, column = 4)


#def getStartPoint():
#    print "getting start point"
#    return scl1.get(), scl2.get(), scl3.get(), scl4.get()

lastUpdate = 0
def currentAlgorithm_(*_):
    global graph
    graph = [
        [(-5, 10), (-4, 20), (0, 10), (3, 15), (6, -10)],
        [(-5, 12), (-4, 30), (5, 10), (5.5, 15), (6, -10)],
        [(-5, 14), (-4, 40), (3, 10), (7, 13), (9, -10)]
    ]
    return

currentAlgorithm = ExplicitRightAlgo

def makeWork():
    def work(*_):
        global lastUpdate
        nlast = int(round(time.time() * 1000))
        if (nlast - lastUpdate < 200): return
        lastUpdate = nlast
        print "working"
        #currentAlgorithm()
        #Plots.drawPlots(currentAlgorithm(scl1.get(), scl2.get(), scl3.get(), scl4.get(), scl5.get()))
        start()
        Plots.drawPlots(graph[int(scl_time.get())], xs)
        return

    return work

cur_row = 2
def createScroll(text, l=0, r=2, resolution=None):
    if resolution == None:
        resolution = (r - l) / 50.0
    global cur_row
    lbl = Label(root, text=text)
    lbl.grid(row=cur_row, column=1)
    scl = Scale(root, from_=l, to=r, resolution=resolution, length=1000, orient=HORIZONTAL)
    scl.set((l + r) / 2)
    scl.grid(row=cur_row, column=2)
    scl.config(command=makeWork())
    cur_row += 1
    return scl

maxT = 100

scl_kappa = createScroll("æ")
scl_dtime = createScroll("Δt")
scl_dx = createScroll("Δx")
scl_u = createScroll("u")
scl_x = createScroll("x", 0, 100)
scl_time = createScroll("t", 0, maxT, 1)

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
    global graph
    global xs
    #Plots.drawPlots(graph[0])
    maxX = scl_x.get()
    dx = scl_dx.get()
    graph = currentAlgorithm(kapa=scl_kappa.get(), dt=scl_dtime.get(), dx=dx, maxT=maxT, u=scl_u.get(), maxX=maxX, initAlgo=initHill)
    xs = list(drange(-maxX, maxX, dx))
    print("xs=", xs)
    print("xs=", len(xs))
    print("graph[0] = ", graph[0])
    print("graph[0] = ", len(graph[0]))
    #plt.show()

# start()

def change_time(*_):
    print("CHANGE TIME")
    Plots.drawPlots(graph[int(scl_time.get())], xs)

btn1.config(command=start)

btn_left.config(command=makeCurrentAlgorithm(ExplicitLeftAlgo))
btn_right.config(command=makeCurrentAlgorithm(ExplicitRightAlgo))
btn_chech.config(command=makeCurrentAlgorithm(ChehAlgo))
btn_left_i.config(command=makeCurrentAlgorithm(ImplicitLeftAlgo))
btn_right_i.config(command=makeCurrentAlgorithm(ImplicitRightAlgo))


# btn4.config(command=test)
#scl_time.config(command=change_time)
#scl2.config(command=makeWork())
#scl3.config(command=makeWork())
#scl4.config(command=makeWork())


# print(time.clock())
# print(int(round(time.time() * 1000)))
# time.sleep(3)
# print(time.clock())
# print(int(round(time.time() * 1000)))





root.mainloop()
