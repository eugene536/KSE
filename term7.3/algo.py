import math
import Constants as C

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
    print (idT, idZ)
    return tableX[idT][idZ]

def getT(t, z):
    idT = int(t / dt)
    idZ = int(z / dz)
    idT = min(mxT - 1, idT)
    idZ = min(mxH - 1, idZ)
    print (idT, idZ)
    return tableT[idT][idZ]

def getSpeed(x, T, K, alf, R, E):
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
        z = i * dz
        res.append(T0)
        # print (" z ", z)
        # res.append(T0 + (Tm - T0) / ( math.exp(z)))
    return res


def initX(cntH):
    res = [0]
    for i in range(1, cntH):
        res.append(1)
        # z = i * dz
        # res.append(1 - 1 / (math.exp(z)))
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

    dz = H * 1.0 / cntH
    dt = totalTime * 1.0 / cntTime

    tableX.append(initX(cntH))
    tableT.append(initT(cntH, Tm, T0))
    for n in range(1, cntTime):
        tableX.append([0] * cntH)
        tableT.append([0] * cntH)

    mxT = cntTime
    mxH = cntH
    for n in range(0, cntTime - 1):
        for k in range(1, cntH - 1):
            tableX[n + 1][k] = dt * (D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz + getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableX[n][k]
            tableT[n + 1][k] = dt * (lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableT[n][k]
            # tableX[n+1][k] = max(0.0, tableX[n+1][k])
            # print(dt, dz)
            # print (D)
            # print ("der ", (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]))
            # print (" cof " , D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz, getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E))
            # print ("x t", tableX[n + 1][k], tableT[n + 1][k])
            # print ("her")
            # print(dt)
            # print ((tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]))
            # print (dz)
            # print ("xxx ", tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1])
            # print("temp: ",  (lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz, Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)))
            # print("x t ", tableX[n][k], tableT[n][k])
            # print("speed: ", Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E))
            # print("res ", (lambd * 1.0 / (ro * C)), ((tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz), Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E))
            # print("gg", dt * (lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)))
            # return
        tableX[n + 1][0] = 0
        tableX[n + 1][cntH - 1] = tableX[n + 1][cntH - 2]
        tableT[n + 1][0] = Tm
        tableT[n + 1][cntH - 1] = tableT[n + 1][cntH - 2]


def solveTriangMatrix(data):
    n = len(data)
    for i in range(0, n - 1):
        assert (abs(data[i][0]) < 1e-5)
        cof = data[i + 1][0] / data[i][1]
        data[i + 1][0] -= data[i][1] * cof
        data[i + 1][1] -= data[i][2] * cof
        data[i + 1][3] -= data[i][3] * cof

    answer = [0] * n

    answer[-1] = data[-1][3] / data[-1][1]
    for i in range(n - 2, -1, -1):
        answer[i] = (data[i][3] - answer[i + 1] * data[i][2]) / data[i][1]

    return answer




def implicit(Tm, T0, H, cntH, totalTime, cntTime, ro, C, D, lambd, Q, K, R, E, alf):
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

    dz = H * 1.0 / cntH
    dt = totalTime * 1.0 / cntTime

    tableX.append(initX(cntH))
    tableT.append(initT(cntH, Tm, T0))
    for n in range(1, cntTime):
        tableX.append([0] * cntH)
        tableT.append([0] * cntH)

    mxT = cntTime
    mxH = cntH
    for n in range(0, cntTime - 1):
        data = []
        for k in range(0, cntH):
            data.append([0] * (cntH + 1))
        for k in range(1, cntH - 1):
            data[k][k] = 1.0 / dt + 2 * D / dz / dz
            data[k][k + 1] = -D / dz / dz
            data[k][k - 1] = -D / dz / dz
            data[k][cntH] = tableX[n][k] / dt + getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)

        data[0][0] = 1
        data[0][cntH] = 0
        data[cntH - 1][cntH - 1] = 1
        data[cntH - 1][cntH - 2] = -1
        tableX[n + 1] = solveTriangMatrix(data)
        # calc T

        data = []
        for k in range(0, cntH):
            data.append([0] * (cntH + 1))
        for k in range(1, cntH - 1):
            data[k][k] = 1.0 / dt + 2 * D / dz / dz
            data[k][k + 1] = -D / dz / dz
            data[k][k - 1] = -D / dz / dz
            data[k][cntH] = tableX[n][k] / dt + getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)

        data[0][0] = 1
        data[0][cntH] = Tm
        data[cntH - 1][cntH - 1] = 1
        data[cntH - 1][cntH - 2] = -1
        tableT[n + 1] = solveTriangMatrix(data)


        # tableX[n + 1][k] = dt * (D * (tableX[n][k - 1] - 2 * tableX[n][k] + tableX[n][k + 1]) / dz / dz +
        #     tableT[n + 1][k] = dt * (lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableT[n][k]
        # tableX[n + 1][0] = 0
        # tableX[n + 1][cntH - 1] = tableX[n + 1][cntH - 2]
        # tableT[n + 1][0] = Tm
        # tableT[n + 1][cntH - 1] = tableT[n + 1][cntH - 2]







#
# A = (2 * C.K * C.lam / (C.ro * C.Q * (C.Tm - C.T0)))
# B = (C.R * (C.Tm ** 2) / C.E) ** 2
# C = math.exp(-C.E / C.R / C.Tm);
# U = (A * B * C)  ** 0.5
# print("U = ", U)

if __name__ == "__main__" :
    calc(C.Tm, C.T0, C.H, C.cntH, C.totalTime, C.cntTime, C.ro, C.C, C.D, C.lam, C.Q, C.K, C.R, C.E, C.alpha)
    # print(getSpeed(1, Constants.T0, Constants.K, Constants.alpha, Constants.R, Constants.E))
    tt = 3.6
    print ("x ", getX(tt, 0.00010))
    print ("temp ", getT(tt, 0.00010))
    G = C.R * C.Tm / C.E

    print("heelo")
    #     tableT[n + 1][k] = dt * (lambd * 1.0 / (ro * C) * (tableT[n][k - 1] - 2 * tableT[n][k] + tableT[n][k + 1]) / dz / dz - Q * 1.0 / C * getSpeed(tableX[n][k], tableT[n][k], K, alf, R, E)) + tableT[n][k]

