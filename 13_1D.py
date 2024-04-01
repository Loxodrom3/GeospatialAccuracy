import matplotlib.pyplot as plt
import numpy as np

numSamp = 10000
mu_x, sigma_x = 0, 1 # mean and standard deviation

# ---- Start Histogram parameters ----
numBins = 21
histDensity = True
histOrientation = 'vertical'  # 'vertical' or 'horizontal'
# histOrientation = 'horizontal'  # 'vertical' or 'horizontal'
xMin = -4  # adding limits to keep histogram range consistent
xMax =  4
x=np.random.normal(mu_x, sigma_x, numSamp)
# ---- End Histogram parameters ----

# ---- Plotting ----
plt.title("Histogram:  Bins = " + ascii(numBins) + ", Samples = " + ascii(numSamp))
plt.hist(x, bins = numBins, color='gray', density = True, orientation = histOrientation)

# plt.xlim(xMin, xMax)
plt.show()

# this has all been 1 Dimensional
# what do we measure that is 1D?
# Change histOrientation to show vertical plot
