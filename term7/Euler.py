from Constants import *



def solve(x0, y0, z0, r):
    print("Hello from Euler")
    ans = [[x0, y0, z0, 0]]
    dt = h;
    ITER = int(round(MAX_T / h))
    t = 0
    for iteration in range(ITER):
        ans.append([x0, y0, z0, t])
        x1 = x0 + dt * dx(x0, y0, z0, r)
        y1 = y0 + dt * dy(x0, y0, z0, r)
        z1 = z0 + dt * dz(x0, y0, z0, r)
        t += h
        x0, y0, z0 = x1, y1, z1

    # print "ended euler"
    return ans
