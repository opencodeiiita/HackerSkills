import matplotlib.pyplot as plt # For ploting
import numpy as np # to work with numerical data efficiently

fs = 100 # sample rate 
f = 2 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [ np.sin(2*np.pi*f * (i/fs)) for i in x]


# showing the exact location of the smaples
plt.stem(x,y, 'r', )
plt.plot(x,y)