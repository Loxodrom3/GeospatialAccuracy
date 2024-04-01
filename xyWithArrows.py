import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import matplotlib.lines as lines

# Plot text
plotTitle = "Arrow Graph" # Overview Title
plotTitleCU = "Close up of final" # Title for the close up graph
xLabel    = "X Axis"
yLabel    = "Y Axis"
xLimits = (-20,20)
yLimits = (-20,20)

# Generate Random data sets for x1,y1 and x2,y2
numSamp = 25
mu_x1, sigma_x1 = -4, 4 # mean and standard deviation
mu_y1, sigma_y1 = 3, 6
mu_x2, sigma_x2 = 0, 1 # mean and standard deviation
mu_y2, sigma_y2 = 0, 1

# Set up Random values
mu_x, sigma_x = 0, 6 # mean and standard deviation
mu_y, sigma_y = -2, 22
x  = np.random.normal(mu_x, sigma_x, numSamp)
y  = np.random.normal(mu_y, sigma_y, numSamp)

x1 = np.random.normal(mu_x1, sigma_x1, numSamp)
y1 = np.random.normal(mu_y1, sigma_y1, numSamp)
x2 = np.random.normal(mu_x2, sigma_x2, numSamp)
y2 = np.random.normal(mu_y2, sigma_y2, numSamp)

# plotting info
fig = plt.figure()

plt.title(plotTitle)
plt.xlabel(xLabel)
plt.ylabel(yLabel)

# Scatter Plot
plt.scatter(x1, y1, color ="red", s=1)
plt.scatter(x2, y2, color ="green", s=1)


# Draw arrows
# for i in range(len(x1)):
#     plt.arrow(x1[i], y1[i], (x2[i]-x1[i]), (y2[i]-y1[i]),color = "blue",
#     head_width=0.7, lw=0.2, shape="full", length_includes_head=True )

plt.xlim(xLimits)
plt.ylim(yLimits)
plt.show()

