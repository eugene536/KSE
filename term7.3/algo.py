import math
import Constants

tableX = []
tableT = []
dz = 0
dt = 0
mxT = 0
mxH = 0

def getX(t, z):
    idT = int(t / dt)
    idZ = int(z / dz)
    idT = min(mxT - 1, idT)
    idZ = min(mxH - 1, idZ)
    # print (dt, dz)
    # print (idT, idZ)
    return tableX[idT][idZ]

def getT(t, z):
    idT = int(t / dt)
    idZ = int(z / dz)
    idT = min(mxT - 1, idT)
    idZ = min(mxH - 1, idZ)
    return tableT[idT][idZ]

def getSpeed(x, T, K, alf, R, E):
    # print("t: ", T)
    return -K * (x ** alf) * math.exp(-E / (R * T))

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
    global tableX, tableT
    gAlf = alf
    gK = K
    gR = R
    gE = E
    tableX = []
    tableT = []

    tableX.append(initX(cntH))
    tableT.append(initT(cntH, Tm, T0))
    for n in range(1, cntTime):
        tableX.append([0] * cntH)
        tableT.append([0] * cntH)

    dz = H * 1.0 / cntH
    dt = totalTime * 1.0 / cntTime
    mxT = cntTime
    mxH = cntH
    for n in range(0, cntTime - 1):
        for k in range(1, cntH - 1):
            tableX[n + 1][k] = dt * (D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz + getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableX[n][k]
            tableT[n + 1][k] = dt * (lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableT[n][k]

            tableX[n+1][k] = max(0.0, tableX[n+1][k])
            # print(dt, dz)
            # print (D)
            # print ("der ", (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]))
            #
            # print (" cof " , D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz, getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E))
            # print ("x t", tableX[n + 1][k], tableT[n + 1][k])
            # print ("her")
            # print(dt)

            # print ((tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]))
            # print("temp: ",  lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz,  - Q / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E))

            # return
        tableX[n + 1][0] = 0
        tableX[n + 1][cntH - 1] = tableX[n + 1][cntH - 2]
        tableT[n + 1][0] = Tm
        tableT[n + 1][cntH - 1] = tableT[n + 1][cntH - 2]



if __name__ == "__main__":
    calc(Constants.Tm, Constants.T0, Constants.H, Constants.cntH, Constants.totalTime, Constants.cntTime, Constants.ro, Constants.C, Constants.D, Constants.lam, Constants.Q, Constants.K, Constants.R, Constants.E, Constants.alpha)
    # print(getSpeed(1, Constants.T0, Constants.K, Constants.alpha, Constants.R, Constants.E))

    print ("x ", getX(10, 0.1))
    print ("temp ", getT(30, 0.1))

    print("heelo")

