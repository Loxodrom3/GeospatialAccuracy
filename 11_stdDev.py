import matplotlib.pyplot as plt
import numpy as np

numSamp = 1000
mu_x, sigma_x = 0, 1 # mean and standard deviation
mu_y, sigma_y = 0, 2 # mean and standard deviation

# ---- Generate data ----
x=np.random.normal(mu_x, sigma_x, numSamp)
y=np.random.normal(mu_y, sigma_y, numSamp)

# ---- Print ----
print(np.mean(x))
print(np.std(x))
print("\n")
print(np.mean(y))
print(np.std(y))

# ---- Starts Histogram parameters ----
numBins = 51
histDensity = True
histOrientation = 'vertical'  # 'vertical' or 'horizontal'
xMin = -8  # adding limits to keep histogram range consistent
xMax = 8
# ---- End Histogram parameters ----

# ---- Plotting ----
plt.title("Histogram:  Bins = " + ascii(numBins) + ", Samples = " + ascii(numSamp))
plt.hist(x, bins = numBins, color='gray', density = True, orientation = histOrientation)
plt.hist(y, bins = numBins, color='Red',  density = True, orientation = histOrientation)


plt.xlim(xMin, xMax)
plt.show()

# StDEV is the deviation from the average of the sample
# increasing the mu_x does not change stdev.
# in other words, bias does not impact StDEV.   Return to RMSE.
# RMSE is calculated from the difference from the observed and 'actual'.  A bias will change the rmse.
