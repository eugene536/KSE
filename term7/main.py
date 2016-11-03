# coding=utf-8
import matplotlib.pyplot as plt

from Tkinter import *



import time

import Euler
import ImplicitEuler
import Plots
import Adams
import Plots3d
import RungeKutta

sys.setrecursionlimit(3500)

root = Tk()


btn1 = Button(root, text="Эйлера явный")
btn1.grid(row = 1, column = 1)
btn2 = Button(root, text="Эйлера неявный")
btn2.grid(row = 1, column = 2)
btn3 = Button(root, text="Pунге-Kутты")
btn3.grid(row = 1, column = 3)
btn4 = Button(root, text="Aдамса")
btn4.grid(row = 1, column = 4)

btnSwitch = Button(root, text="Переключатель")
btnSwitch.grid(row = 5, column = 4)

lbl1 = Label(root, text="x0")
lbl1.grid(row = 2, column = 1)
scl1 = Scale(root, from_=0, to=30, resolution=0.1, length=1000, orient=HORIZONTAL)
scl1.set(1)
scl1.grid(row = 2, column = 2)

lbl2 = Label(root, text="y0")
lbl2.grid(row = 3, column = 1)
scl2 = Scale(root, from_=0, to=30, resolution=0.1, length=1000, orient=HORIZONTAL)
scl2.set(2)
scl2.grid(row = 3, column = 2)

lbl3 = Label(root, text="z0")
lbl3.grid(row = 4, column = 1)
scl3 = Scale(root, from_=0, to=30, resolution=0.1, length=1000, orient=HORIZONTAL)
scl3.set(3)
scl3.grid(row = 4, column = 2)

lbl4 = Label(root, text="r")
lbl4.grid(row = 5, column = 1)
scl4 = Scale(root, from_=0, to=30, resolution=0.1, length=1000, orient=HORIZONTAL)
scl4.set(4)
scl4.grid(row = 5, column = 2)

def getStartPoint():
    print "getting start point"
    return scl1.get(), scl2.get(), scl3.get(), scl4.get()

lastUpdate = 0

plotsType=0


def makeWork(algorithm):
    def work(*_):
        # print("in Work!!")
        global lastUpdate
        nlast = int(round(time.time() * 1000))
        if (nlast - lastUpdate < 200): return
        lastUpdate = nlast
        print ("x y z r: ", scl1.get(), scl2.get(), scl3.get(), scl4.get())
        if plotsType == 0:
            Plots.drawPlots(algorithm(scl1.get(), scl2.get(), scl3.get(), scl4.get()))
        else:
            Plots3d.drawPlots(algorithm(scl1.get(), scl2.get(), scl3.get(), scl4.get()))


    return work

currentAlgorithm = Euler.solve

def makeCurrentAlgorithm(algorithm):
    def work(*_):
        print("HEEEELLOO")
        global currentAlgorithm
        print("change")
        currentAlgorithm = algorithm
        makeWork(algorithm)()
    return work

def test():
    print("test want adams work")

def switcher():
    global plotsType
    plotsType = 1 - plotsType

    makeWork(currentAlgorithm)()

btn1.config(command=makeCurrentAlgorithm(Euler.solve))
btn2.config(command=makeCurrentAlgorithm(ImplicitEuler.solve))
btn3.config(command=makeCurrentAlgorithm(RungeKutta.rungeKutta))
btn4.config(command=makeCurrentAlgorithm(Adams.adams))
btnSwitch.config(command=switcher)


# btn4.config(command=test)

scl1.config(command=makeWork(currentAlgorithm))
scl2.config(command=makeWork(currentAlgorithm))
scl3.config(command=makeWork(currentAlgorithm))
scl4.config(command=makeWork(currentAlgorithm))


# print(time.clock())
# print(int(round(time.time() * 1000)))
# time.sleep(3)
# print(time.clock())
# print(int(round(time.time() * 1000)))





root.mainloop()
