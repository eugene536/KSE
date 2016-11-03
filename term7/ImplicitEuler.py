from Constants import *


def solve(x0, y0, z0, r):
    print("Hello from ImplicitEuler")

    ans = [[x0, y0, z0, 0]]


    ITER = int(round(MAX_T / h))
    t = 0
    for iteration in range(ITER):
        ans.append([x0, y0, z0, t])
        x1 = x0 + h * dx(x0, y0, z0, r)
        y1 = y0 + h * dy(x0, y0, z0, r)
        z1 = z0 + h * dz(x0, y0, z0, r)

        x2 = x0 + h * (dx(x0, y0, z0, r) + dx(x1, y1, z1, r)) / 2
        y2 = y0 + h * (dy(x0, y0, z0, r) + dy(x1, y1, z1, r)) / 2
        z2 = z0 + h * (dz(x0, y0, z0, r) + dz(x1, y1, z1, r)) / 2
        x1, y1, z1 = x2, y2, z2

        t += h
        x0, y0, z0 = x1, y1, z1

    return ans
