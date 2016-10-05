# coding=utf-8
import matplotlib.pyplot as plt

from Tkinter import *
import Euler
import Plots

root = Tk()

btn1 = Button(root, text="явный Эйлер")
btn1.grid(row = 1, column = 1)
btn2 = Button(root, text="неявный Эйлер")
btn2.grid(row = 1, column = 2)
btn3 = Button(root, text="рунге-кутт")
btn3.grid(row = 1, column = 3)
btn4 = Button(root, text="адамс")
btn4.grid(row = 1, column = 4)

lbl1 = Label(root, text="x0")
lbl1.grid(row = 2, column = 1)
scl1 = Scale(root, from_=0, to=30, resolution=0.1)
scl1.set(1)
scl1.grid(row = 2, column = 2)


lbl2 = Label(root, text="y0")
lbl2.grid(row = 3, column = 1)
scl2 = Scale(root, from_=0, to=30, resolution=0.1)
scl2.set(2)
scl2.grid(row = 3, column = 2)

lbl3 = Label(root, text="z0")
lbl3.grid(row = 4, column = 1)
scl3 = Scale(root, from_=0, to=30, resolution=0.1)
scl3.set(3)
scl3.grid(row = 4, column = 2)

lbl4 = Label(root, text="r")
lbl4.grid(row = 5, column = 1)
scl4 = Scale(root, from_=0, to=30, resolution=0.1)
scl4.set(4)
scl4.grid(row = 5, column = 2)

def getStartPoint():
    print "getting start point"
    return scl1.get(), scl2.get(), scl3.get(), scl4.get()

def makeWork(algorithm):
    def work():
        Plots.drawPlots(algorithm(scl1.get(), scl2.get(), scl3.get(), scl4.get()))
    return work


btn1.config(command=makeWork(Euler.solve))

root.mainloop()
