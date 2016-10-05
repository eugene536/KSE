from Constants import *

ITERATIONS = 1000
MAX_T = 30

def solve(x0, y0, z0, r):
    print "started euler"
    ans = [[x0, y0, z0, 0]]

    dt = MAX_T * 1.0 / ITERATIONS
    t = 0
    for iteration in range(ITERATIONS):
        x1 = x0 + dt * dx(x0, y0, z0, r)
        y1 = y0 + dt * dy(x0, y0, z0, r)
        z1 = z0 + dt * dz(x0, y0, z0, r)

        x2 = x0 + dt * (dx(x0, y0, z0, r) + dx(x1, y1, z1, r)) / 2
        y2 = y0 + dt * (dy(x0, y0, z0, r) + dy(x1, y1, z1, r)) / 2
        z2 = z0 + dt * (dz(x0, y0, z0, r) + dz(x1, y1, z1, r)) / 2
        x1, y1, z1 = x2, y2, z2

        t += dt
        ans.append([x1, y1, z1, t])
        x0, y0, z0 = x1, y1, z1

    print "ended euler"
    return ans