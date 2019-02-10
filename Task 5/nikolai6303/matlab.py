import matplotlib.pyplot as plt
import numpy as np


Fs = 2
sample=20
x = np.arange(sample)
y = 2*np.sin(np.pi *1/4* x / Fs)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('2sin(x*pi/4)')
plt.show()