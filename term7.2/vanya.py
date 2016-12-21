import math

def initHill(maxX, dx):
    res = []
    curX = -maxX
    while curX <= maxX:
        res.append(math.exp(- (curX * curX)))
        curX += dx
    return res


def ChehAlgo(maxX, dx, maxT, dt, u, kapa, initAlgo):
    from PIL import Image
    img = Image.open('test.txt')
    img.show()

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


def ImplicitRightAlgo(maxX, dx, maxT, dt, u, kapa, initAlgo):
    init = initAlgo(maxX, dx)
    answer = []
    answer.append(init)
    curT = dt
    l = len(init)
    while (curT <= maxT):
        print("curT", curT)
        #         curRes = [0] * len(init)
        #         curRes[0] = answer[-1][0]
        #         curRes[-1] = answer[-1][-1]

        matrix = [0] * l
        for i in range(0, l):
            matrix[i] = [0] * 4

        matrix[0][1] = 1
        matrix[0][3] = answer[-1][0]

        matrix[-1][1] = 1
        matrix[-1][3] = answer[-1][-1]
        for k in range(1, l - 1):
            D = answer[-1][k] / dt
            A = -kapa * dx / dx
            B = 1 / dt - u / dx + 2 * kapa / dx / dx
            C = u / dx - kapa / dx / dx
            matrix[k] = [A, B, C, D]
        # print(matrix)
        answer.append(solveTriangMatrix(matrix))
        curT += dt

    return answer


def ImplicitLeftAlgo(maxX, dx, maxT, dt, u, kapa, initAlgo):
    init = initAlgo(maxX, dx)
    answer = []
    answer.append(init)
    curT = dt
    l = len(init)
    while (curT <= maxT):
        print("curT", curT)
        #         curRes = [0] * len(init)
        #         curRes[0] = answer[-1][0]
        #         curRes[-1] = answer[-1][-1]

        matrix = [0] * l
        for i in range(0, l):
            matrix[i] = [0] * 4

        matrix[0][1] = 1
        matrix[0][3] = answer[-1][0]

        matrix[-1][1] = 1
        matrix[-1][3] = answer[-1][-1]
        for k in range(1, l - 1):
            D = answer[-1][k] / dt
            A = -kapa * dx / dx - u / dx
            B = 1 / dt + u / dx + 2 * kapa / dx / dx
            C = - kapa / dx / dx
            matrix[k] = [A, B, C, D]
        # print(matrix)
        answer.append(solveTriangMatrix(matrix))
        curT += dt

    return answer