import matplotlib.pyplot as plt
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--yName", help="Name of y axis", required=True, type=str)
parser.add_argument("--xName", help="Name of x axis", required=False, type=str, default="T (temperature)")

args = parser.parse_args()
plt.ylabel(args.yName)
plt.xlabel(args.xName)

xs = map(int, sys.stdin.readline().split())
ys = map(float, sys.stdin.readline().split())
plt.plot(xs, ys)

plt.show()