from Constants import *

ITERATIONS = 5000


def solve(x0, y0, z0, r):
    print("Hello from Euler")
    ans = [[x0, y0, z0, 0]]

    dt = MAX_T * 1.0 / ITERATIONS
    t = 0
    for iteration in range(ITERATIONS):
        ans.append([x0, y0, z0, t])
        x1 = x0 + dt * dx(x0, y0, z0, r)
        y1 = y0 + dt * dy(x0, y0, z0, r)
        z1 = z0 + dt * dz(x0, y0, z0, r)
        t += dt
        x0, y0, z0 = x1, y1, z1

    # print "ended euler"
    return ans
