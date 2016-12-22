import numpy as np

K = 1.6 * (10 ** 6)
E = 8 * 10 ** 4
R = 8.314
alpha = 1
Q = 7 * 10 ** 5
T0 = 293
Tm = 773
C = 1980
ro = 830
lam = 0.13
D = 8 * 10 ** (-12)
maxTime = 1000
Tm = T0 + Q * 1.0 / C

H = 0.03
totalTime = 500

cntH = 300
cntTime = 50000


def myEqual(a, b):
    if abs(a - b) > 10 ** -9:
        print ("A != B ", a, b)
        assert False

myEqual(cntTime * 10 ** -2, totalTime)
myEqual(cntH * 10 ** -4, H)


# dz = 10 ** -4
# dt = 10 ** -2
# dz <= 0.000166
# h >> 1.66666

