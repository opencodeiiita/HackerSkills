import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10,0.1)
y = 2*np.sin(np.pi * x / 4)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
