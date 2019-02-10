import numpy as np

import matplotlib.pyplot as plot


x_values       = np.arange(-10, 10, 0.1);

y_values  = 2*(np.sin(x_values*(np.pi/4)))

plot.plot(x_values, y_values)

plot.title('Sine wave')

plot.xlabel('x')

plot.ylabel('y = 2sin(x*pi/4)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

plot.show()

