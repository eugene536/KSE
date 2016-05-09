%pylab inline

import pylab
import numby as np

x = np.linspace(0, 20, 1000)
y = np.sin(x)

pylab.plot(x, y)
#import pylab
#import sys

#x = [0, 1, 2]
#y = [0, 1, 4]

#pylab.plot(x, y)
#sys.stdout.write("where is my plot?..\n")
