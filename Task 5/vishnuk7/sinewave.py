import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-20,20,0.2)
y = 2*np.sin(x * np.pi/4)
plt.plot(x, y)
plt.title('sine wave')
plt.xlabel('x-axis')
plt.ylabel('2sin(x*pi/4)')
plt.show()