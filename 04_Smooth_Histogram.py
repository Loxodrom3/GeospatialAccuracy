import matplotlib.pyplot as plt
import numpy as np

numSamp = 1000000
mu_x, sigma_x = 0, 1 # mean and standard deviation
mu_y, sigma_y = 3, 2 # mean and standard deviation

# ---- Start Histogram parameters ----
numBins = 51
histDensity = True
histOrientation = 'vertical'  # 'vertical' or 'horizontal'
xMin = -4  # adding limits to keep histogram range consistent
xMax =  8
x=np.random.normal(mu_x, sigma_x, numSamp)
y=np.random.normal(mu_y, sigma_y, numSamp)
# ---- End Histogram parameters ----

# ---- Plotting ----
plt.title("Histogram:  Bins = " + ascii(numBins) + ", Samples = " + ascii(numSamp))
plt.hist(x, bins = numBins, color='gray', density = True, orientation = histOrientation)
plt.hist(y, bins = numBins, color='Red',  density = True, orientation = histOrientation)

plt.xlim(xMin, xMax)
plt.show()
