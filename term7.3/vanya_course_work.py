import math

tableX = []
tableT = []
tableW = []
dz = 0
dt = 0
mxT = 0
mxH = 0

def getX(t, z):
    idT = int(t / dt)
    idZ = int(z / dz)
    idT = min(mxT - 1, idT)
    idZ = min(mxH - 1, idZ)
    return tableX[idT][idZ]

def getT(t, z):
    idT = int(t / dt)
    idZ = int(z / dz)
    idT = min(mxT - 1, idT)
    idZ = min(mxH - 1, idZ)
    return tableT[idT][idZ]

def getSpeed(x, T, K, alf, R, E):
    # return 0
    return -K * (x ** alf)  * math.exp(-E / (R * T))

gK = 0
gAlf = 0
gR = 0
gE = 0

def getW(x, T):
    return getSpeed(x, T, gK, gAlf, gR, gE)

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



def calc(Tm, T0, H, cntH, totalTime, cntTime, ro, C, D, lambd, Q, K, R, E, alf):
    global gAlf, gK, gR, gE
    global dz, dt
    global mxT, mxH
    gAlf = alf
    gK = K
    gR = R
    gE = E

    tableX.append(initX(cntH))
    tableT.append(initT(cntH, Tm, T0))
    for n in range(1, cntTime):
        tableX.append([0] * cntH)
        tableT.append([0] * cntH)

    dz = H * 1.0 / cntH
    dt = totalTime * 1.0 / cntTime
    mxT = totalTime
    mxH = cntH

    for n in range(0, totalTime - 1):
        for k in range(1, cntH - 1):
            tableX[n + 1][k] = dt * (D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz + getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableX[n][k]
            tableT[n + 1][k] = dt * (lambd / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableT[n][k]
        tableX[n + 1][0] = 0
        tableX[n + 1][cntH - 1] = 0
        tableT[n + 1][0] = Tm
        tableT[n + 1][cntH - 1] = T0

calc(300, 100, 10, 100, 10, 100, 10, 10, 10, 10, 10, 10, 10, 10, 10)

print("heelo")

