import math


tableX = []
tableT = []
tableW = []
dz = 0
dt = 0

def getX(t, z):
    return tableX[t][z]

def getT(t, z):
    return tableT[t][z]


def getW(x, T):
    return tableW[x][T]


def initT(cntH, Tm, T0):
    res = [Tm]
    for i in range(1, cntH):
        res.append(T0)
    return res


def initX(cntH):
    res = [0]
    for i in range(1, cntH):
        res.append(1)
    return res


def getSpeed(x, T, K, alf, R, E):
    return -K * (x ** alf)  * math.exp(-E / (R * T))

def calc(Tm, T0, H, cntH, totalTime, cntTime, ro, C, D, lambd, Q, K, R, E, alf):
    global dz, dt
    tableX.append(initX(cntH))
    tableT.append(initT(cntH, Tm, T0))
    for n in range(1, totalTime):
        tableX.append([0] * cntH)
        tableT.append([0] * cntH)


    dz = H * 1.0 / cntH
    dt = totalTime / cntTime

    for n in range(0, totalTime - 1):
        for k in range(1, cntH - 1):
            tableX[n + 1][k] = dt * (D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz + getSpeed(tableX[n][k], tableT[n][k], alf, R, E)) + tableX[n][k]
            tableT[n + 1][k] = dt * (lambd / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q / C * getSpeed(tableX[n][k], tableT[n][k], alf, R, E)) + tableT[n][k]
        tableX[n + 1][0] = 0
        tableX[n + 1][cntH - 1] = 0
        tableT[n + 1][0] = Tm
        tableT[n + 1][cntH - 1] =





