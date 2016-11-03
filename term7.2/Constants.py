import numpy as np

MAX_T = 30
sigma = 10
b = 8.0 / 3

h = 0.01

def dx(x, y, z, r):
    return -sigma * x + sigma * y

def dy(x, y, z, r):
    return -x * z + r * x - y

def dz(x, y, z, r):
    return x * y - b * z

def calcDer(point, r):
    x, y, z = point
    return np.array([sigma * (y - x), -x * z + r * x - y, x * y - b*z])


