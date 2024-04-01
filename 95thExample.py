import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

numSamp =10

mu_x1, sigma_x1 = 0, 5 # mean and standard deviation
mu_y1, sigma_y1 = 0, 0.0000001

x1 = np.random.normal(mu_x1, sigma_x1, numSamp)
y1 = np.random.normal(mu_y1, sigma_y1, numSamp)
absX = [abs(ele) for ele in x1]

# Plot Limits
limGr = 10
xLimits = (-1*0,limGr)
yLimits = (-1*2,2)

fig, axs = plt.subplots(1,1)

print(absX)
# plotting
axs.set_title("X Error plot")
axs.axvline(c='grey', lw=1.5)
axs.axhline(c='grey', lw=1.5)
axs.scatter(absX, y1, color ="red", s=10)

axs.grid()
axs.set_aspect('equal', 'box')
axs.set(xlim=xLimits, ylim=yLimits)
plt.show()
# Write your code here :-)
