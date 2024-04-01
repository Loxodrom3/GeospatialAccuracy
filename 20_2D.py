import matplotlib.pyplot as plt
import numpy as np

numSamp = 1000
mu_x, sigma_x = 0, 1 # mean and standard deviation
mu_y, sigma_y = 0, 1 # mean and standard deviation

x=np.random.normal(mu_x, sigma_x, numSamp)
y=np.random.normal(mu_y, sigma_y, numSamp)

# ---- Start Plot parameters ----
xMin = -4.5  # adding limits to keep histogram range consistent
xMax =  4.5
yMin = -4.5
yMax =  4.5
# ---- End Plot parameters ----

# ---- Plotting ----
plt.title("Title " + "Samples = " + ascii(numSamp))
plt.axvline(0,yMin,yMax,color='gray', lw=1.5)
plt.axhline(0,xMin,xMax,color='gray', lw=1.5)

plt.scatter(x, y, color = 'Green', s=2)

plt.xlim(xMin, xMax)
plt.ylim(yMin, yMax)
plt.show()
