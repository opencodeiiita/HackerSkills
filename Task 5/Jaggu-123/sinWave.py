# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 10:57:32 2019

@author: Manish Jagnani
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.01)
y = 2 * np.sin(x * np.pi /4)
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('2sin(x*pi/4)')
plt.show()