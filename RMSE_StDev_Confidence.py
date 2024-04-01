import matplotlib.pyplot as plt
import numpy as np

itter8 = 1000000
grphx = ([])
grphx.clear()
xStDev = ([])
xStDev.clear()
xRmse = ([])
xRmse.clear()

numSamp = 30

mu_x, sigma_x = 0, 1 # mean and standard deviation

# For Histogram graph
numBins = 51
histDensity = True
histOrientation = 'vertical'  # 'vertical' or 'horizontal'
xMin = -4  # adding limits to keep histogram range consistent
xMax = 4

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

for i in range(itter8):
    x = np.random.normal(mu_x, sigma_x, numSamp)
    grphx.insert(i, x[0])
    xStDev.insert(i,np.std(x))
    xRmse.insert(i,rmse(x,0))

# plotting
plt.title("Itterations = " + ascii(itter8) + " numSamps= " + ascii(numSamp))
plt.hist(grphx,bins = numBins, color='gray',  density = True, orientation = histOrientation)
plt.hist(xStDev,  bins = numBins, color='Red',  density = True , orientation = histOrientation)
plt.hist(xRmse,  bins = numBins, color='Blue',  density = True , orientation = histOrientation)


plt.xlim(xMin, xMax)
plt.show()
