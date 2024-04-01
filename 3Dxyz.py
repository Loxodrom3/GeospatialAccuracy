import matplotlib.pyplot as plt
import numpy as np

xMin = 1  # adding limits to keep histogram range consistent
xMax = -3
yMin = 1  # adding limits to keep histogram range consistent
yMax = 3
zMin = -6  # adding limits to keep histogram range consistent
zMax = 1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
ax.scatter(-2.277,1.901,-4.969, marker='o')
ax.scatter(-2.668,2.626,-3.987, marker='o')
ax.scatter(-2.696,2.331,-4.795, marker='o')
ax.scatter(-2.541,2.15,-5.559, marker='o')
ax.scatter(-2.427,2.124,-4.237, marker='o')
ax.scatter(-2.717,2.054,-3.773, marker='o')
ax.scatter(-2.892,2.285,-3.827, marker='o')
ax.scatter(-2.149,2.233,-4.016, marker='o')
ax.scatter(-2.529,2.59,-5.218, marker='o')
ax.scatter(-2.38,2.106,-4.505, marker='o')
ax.scatter(-2.525,2.318,-4.962, marker='o')
ax.scatter(-2.025,2.437,-4.434, marker='o')
ax.scatter(-2.056,2.326,-4.038, marker='o')
ax.scatter(-2.606,2.179,-3.181, marker='o')
ax.scatter(-3.098,2.226,-5.27, marker='o')
ax.scatter(-2.925,2.237,-5.503, marker='o')
ax.scatter(-2.803,2.245,-1.236, marker='o')
ax.scatter(-2.687,2.385,-5.16, marker='o')
ax.scatter(-3.209,2.18,-5.593, marker='o')
ax.scatter(-2.488,2.322,-4.851, marker='o')
ax.scatter(-2.145,2.314,-4.339, marker='o')
ax.scatter(-2.361,2.373,-4.42, marker='o')
ax.scatter(-2.515,2.341,-4.874, marker='o')
ax.scatter(-2.028,2.312,-4.656, marker='o')
ax.scatter(-3.391,2.323,-4.214, marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.xlim(xMin, xMax)
plt.ylim(yMin, yMax)
# plt.zlim(zMin, zMax)
plt.show()# Write your code here :-)
