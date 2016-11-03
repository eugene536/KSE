import numpy as np
from Constants import *
from RungeKutta import rungeKuttaStep
from Constants import h


def adams(x0, y0, z0, r):
    print("Hello from Adams")
    p = np.array([x0, y0, z0])
    ITER = int(round(MAX_T / h))
    tmr = 0
    history=[]
    for i in range(0, ITER):
        history.append(p.tolist() + [tmr])
        if i < 3:
            p = rungeKuttaStep(p, h, r)
        else:
            p0 = np.array(history[-4][:3])
            p1 = np.array(history[-3][:3])
            p2 = np.array(history[-2][:3])
            p3 = np.array(history[-1][:3])
            p4 = p
            f0 = calcDer(p0, r)
            f1 = calcDer(p1, r)
            f2 = calcDer(p2, r)
            f3 = calcDer(p3, r)
            f4 = calcDer(p4, r)

            p = p4 + h * (1901 / 720 * f4 - 1387 / 360 * f3 + 109 /30 * f2 - 637/360 * f1 + 251/720 * f0)

        tmr = tmr + h

    return history






