import matplotlib.pyplot as plt
import numpy as np

numSamp = 20
mu_x, sigma_x = 0, 1 # mean and standard deviation

# ---- Start Histogram parameters ----
numBins = 2
histDensity = True
histOrientation = 'horizontal'  # 'vertical' or 'horizontal'
xMin = -4  # adding limits to keep histogram range consistent
xMax =  4
# ---- End Histogram parameters ----

x=np.random.normal(mu_x, sigma_x, numSamp)
#y=np.random.rand(numSamp)

# ---- Plotting ----
plt.title("Histogram:  Bins = " + ascii(numBins) + ", Samples = " + ascii(numSamp))
#plt.hist(y, bins = numBins, color='Red',  density = True, orientation = histOrientation)
plt.hist(x, bins = numBins, color='gray', density = True, orientation = histOrientation)

plt.xlim(xMin, xMax)
plt.show()
