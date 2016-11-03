import math

def initHill(maxX, dx):
    res = []
    curX = -maxX
    while curX <= maxX:
        res.append(math.exp(- (curX * curX)))
        curX += dx
    return res


def ChehAlgo(maxX, dx, maxT, dt, u, kapa, initAlgo):
    init = initHill(maxX, dx)
    answer = []
    answer.append(init)
    answer.append(init)
    curT = dt * 2
    l = len(init)
    while (curT <= maxT):
        curRes = [0] * len(init)
        #         print(len(answer), len(answer[-1]))
        #         print(len(curRes))
        curRes[0] = answer[-1][0]
        curRes[-1] = answer[-1][-1]
        for i in range(1, l - 1):
            A = answer[-2][i]
            B = - u * dt / dx * (answer[-1][i + 1] - answer[-1][i - 1])
            C = kapa * 2 * dt / (dx * dx) * (answer[-1][i - 1] - 2 * answer[-1][i] + answer[-1][i + 1])
            curRes[i] = A + B + C

        answer.append(curRes)
        curT += dt
    return answer


def ExplicitRightAlgo(maxX, dx, maxT, dt, u, kapa, initAlgo):
    init = initAlgo(maxX, dx)
    answer = []
    answer.append(init)
    answer.append(init)
    curT = dt * 2
    l = len(init)
    while (curT <= maxT):
        curRes = [0] * len(init)
        curRes[0] = answer[-1][0]
        curRes[-1] = answer[-1][-1]
        for i in range(1, l - 1):
            A = answer[-1][i]
            B = - u * dt / dx * (answer[-1][i + 1] - answer[-1][i])
            C = kapa * dt / (dx * dx) * (answer[-1][i - 1] - 2 * answer[-1][i] + answer[-1][i + 1])
            curRes[i] = A + B + C

        answer.append(curRes)
        curT += dt
    return answer


def ExplicitLeftAlgo(maxX, dx, maxT, dt, u, kapa, initAlgo):
    init = initAlgo(maxX, dx)
    answer = []
    answer.append(init)
    answer.append(init)
    curT = dt * 2
    l = len(init)
    while (curT <= maxT):
        curRes = [0] * len(init)
        curRes[0] = answer[-1][0]
        curRes[-1] = answer[-1][-1]
        for i in range(1, l - 1):
            A = answer[-1][i]
            B = - u * dt / dx * (answer[-1][i] - answer[-1][i - 1])
            C = kapa * dt / (dx * dx) * (answer[-1][i - 1] - 2 * answer[-1][i] + answer[-1][i + 1])
            curRes[i] = A + B + C

        answer.append(curRes)
        curT += dt
    return answer