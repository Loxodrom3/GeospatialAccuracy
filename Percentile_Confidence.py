import matplotlib.pyplot as plt
import numpy as np

itter8 = 1000000
numSamp = 20
mu_x, sigma_x = 0, 1 # mean and standard deviation

grphx = ([])
grphx.clear()
x10 = ([])   # Ten percentile
x10.clear()
x30 = ([])   # 30 percentile
x30.clear()
x50 = ([])   #
x50.clear()
x70 = ([])   #
x70.clear()
x90 = ([])   #
x90.clear()
x95 = ([])   #
x95.clear()
x99 = ([])   #
x99.clear()
x999 = ([])   # 99.9th percentile
x999.clear()
xStdev = ([])
xStdev.clear()
xRmse = ([])
xRmse.clear()


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
#    x10.insert(i,np.percentile(abs(x), 10))
#    x30.insert(i,np.percentile(abs(x), 30))
#    x50.insert(i,np.percentile(abs(x), 50))
    x70.insert(i,np.percentile(abs(x), 68.6))
#    x90.insert(i,np.percentile(abs(x), 90))
    x95.insert(i,np.percentile(abs(x), 95))
#    x99.insert(i,np.percentile(abs(x), 99))
#    x999.insert(i,np.percentile(abs(x), 99.9))

print(np.percentile(x70,5))
print(np.percentile(x70,95))
print(np.percentile(x95,5))
print(np.percentile(x95,95))

# plotting
plt.title("Itterations = " + ascii(itter8) + " numSamps= " + ascii(numSamp))
plt.hist(grphx,bins = numBins, color='gray',  density = True, orientation = histOrientation)
plt.hist(x10,  bins = numBins, color='Red',  density = True , orientation = histOrientation)
plt.hist(x30,  bins = numBins, color='Orange',  density = True , orientation = histOrientation)
plt.hist(x50,  bins = numBins, color='Yellow',  density = True, orientation = histOrientation)
plt.hist(x70,  bins = numBins, color='Green',  density = True, orientation = histOrientation)
plt.hist(x90,  bins = numBins, color='blue',  density = True, orientation = histOrientation)
plt.hist(x95,  bins = numBins, color='Indigo',  density = True, orientation = histOrientation)
# plt.hist(x99,  bins = numBins, color='violet',  density = True, orientation = histOrientation)
# plt.hist(x999,  bins = numBins, color='silver',  density = True, orientation = histOrientation)

plt.xlim(xMin, xMax)
plt.show()
