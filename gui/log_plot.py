#!/usr/bin/env python

import matplotlib.pyplot as plt
import argparse
import sys
import re

parser = argparse.ArgumentParser()
parser.add_argument("--yName", help="Name of y axis", required=True, type=str)
parser.add_argument("--xName", help="Name of x axis", required=False, type=str, default="T (temperature)")
parser.add_argument("--plotName", help="Name of plot", required=False, type=str)

args = parser.parse_args()
plt.ylabel(args.yName)
plt.xlabel(args.xName)

plt.suptitle(args.plotName if args.plotName else args.yName, fontsize=14, fontweight='bold')

xs = map(float, sys.stdin.readline().split())
ys = map(float, sys.stdin.readline().split())
plt.plot(xs, ys)

#plt.savefig(args.yName + ".png")
plt.show()
