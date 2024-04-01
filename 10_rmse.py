import matplotlib.pyplot as plt
import numpy as np
import math

numSamp = 20
mu_x, sigma_x = 2, 3 # mean and standard deviation
mu_y, sigma_y = 0, 2 # mean and standard deviation

# ---- Generate data ----
x=np.random.normal(mu_x, sigma_x, numSamp)
y=np.random.normal(mu_y, sigma_y, numSamp)
# MSE = np.square(np.subtract(y_actual,y_predicted)).mean()
# RMSE = math.sqrt(MSE)
MSEx  = np.square(x).mean()
RMSEx = math.sqrt(MSEx)

MSEy  = np.square(y).mean()
RMSEy = math.sqrt(MSEy)

print(MSEx)
print('RMSEx: ', RMSEx)
print('/n')
print(MSEy)
print('RMSEy: ', RMSEy)


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
# plt.hist(y, bins = numBins, color='Red',  density = True, orientation = histOrientation)


plt.xlim(xMin, xMax)
plt.show()


# increase numSamp to get smooth
# change mu_y
# discuss actual minus predicted
