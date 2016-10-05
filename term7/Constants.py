sigma = 10
b = 8.0 / 3

def dx(x, y, z, r):
    return -sigma * x + sigma * y

def dy(x, y, z, r):
    return -x * z + r * x - y

def dz(x, y, z, r):
    return x * y - b * z