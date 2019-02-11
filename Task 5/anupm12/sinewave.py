import matplotlib.pyplot as plot
import numpy as npy
x = npy.arange(0,25,0.1)
y = 2 * npy.sin(npy.pi *x /4)

plot.title('PLot a sine wave')
plot.xlabel('Time')
plot.ylabel('2sin(x*pi/4)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.plot(x, y)
plot.show()