import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0, 20, 0.2);
amplitude = np.sin(time)
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('time')
plot.ylabel('amplitude') 
plot.show()