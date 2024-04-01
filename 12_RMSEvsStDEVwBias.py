import matplotlib.pyplot as plt
import numpy as np
import math

numSamp = 10000
bias = 0
mu_x, sigma_x = bias, 1 # mean and standard deviation # sample for RMSE
mu_y, sigma_y = bias, 1 # mean and standard deviation # sample for StDEVd

# ---- Generate data ----
x=np.random.normal(mu_x, sigma_x, numSamp)
y=np.random.normal(mu_y, sigma_y, numSamp)
# MSE = np.square(np.subtract(y_actual,y_predicted)).mean()
# RMSE = math.sqrt(MSE)
MSEx  = np.square(x).mean()
RMSEx = math.sqrt(MSEx)
MSEy  = np.square(y).mean()
RMSEy = math.sqrt(MSEy)

print('RMSEx:  ', RMSEx)
print('StDEVx: ', np.std(x))
print('RMSEy:  ', RMSEy)
print('StDEVy: ', np.std(y))


# ---- Start Histogram parameters ----
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

# size of numSamp to get smooth histogram
# increase bias to show that stdev stays the same, and RMSE changes with bias
# change mu_y to show the effect of spreding out the histogram
