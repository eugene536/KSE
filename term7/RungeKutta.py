import numpy as np
from Constants import *
from Constants import h

def rungeKuttaStep(p, h, r):
    k1 = calcDer(p, r)
    k2 = calcDer(p + k1 * h / 2, r)
    k3 = calcDer(p + k2 * h / 2, r)
    k4 = calcDer(p + k3 * h, r)

    p = p + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return p


def rungeKutta(x0, y0, z0, r):
    p = np.array([x0, y0, z0])
    tmr = 0
    history=[]
    ITER = round(MAX_T / h)
    for i in range(0, ITER):
        history.append(p.tolist() + [tmr])
        p = rungeKuttaStep(p, h, r)
        tmr = tmr + h
    return history





