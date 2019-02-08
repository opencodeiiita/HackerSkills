import matplotlib.pyplot as mpl
import numpy as np



x = np.arange(0, 15, 0.0001)  
y = 2 * np.sin(np.pi *x /4)

mpl.title('Plotting Sine Wave using python')
mpl.xlabel('Time')
mpl.ylabel('Amplitude : y = 2sin(x*pi/4)')
mpl.plot(x, y)
mpl.savefig('sine wave')
mpl.show()
