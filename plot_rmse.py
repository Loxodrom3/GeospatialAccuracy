#
import matplotlib.pyplot as plt
import numpy as np

muX = 0   # average error (bias)
muY = 0
sigma = 1 # RMSE (spread)
numSamp = 5

x = np.random.normal(muX, sigma, numSamp)
y = np.random.normal(muY, sigma, numSamp)

ptX = ( 2001.1,  2012.2,  2006.3,  2001.4,  2011.5)
ptY = (10509.1, 10511.2, 10504.3, 10499.4, 10500.5)

obsX = ptX + x
obsY = ptY + y
dX = obsX - ptX
dY = obsY - ptY

# Plot Limits
ptXSpread = max(ptX) - min(ptX)
ptYSpread = max(ptY) - min(ptY)
limPct = 0.5
xLim1 = (min(ptX)-(ptXSpread*limPct), max(ptX)+(ptXSpread*limPct))
yLim1 = (min(ptY)-(ptYSpread*limPct), max(ptY)+(ptYSpread*limPct))

limGr = 8
xLim2 = (-1*limGr,limGr)
yLim2 = (-1*limGr,limGr)


fig, (ax1, ax2) = plt.subplots(1,2)

# plotting
# axs.set_title("Line graph")
ax1.scatter( ptX,  ptY, color ="red", marker = "^")
ax1.scatter(obsX, obsY, color ="blue", marker = "+")
ax1.set(xlim=xLim1, ylim=yLim1)
ax1.grid()
ax1.set_aspect('equal', 'box')

ax2.scatter(0, 0, color ="red", marker = "^")
ax2.scatter(dX, dY, color ="blue", marker = "+")
ax2.set(xlim=xLim2, ylim=yLim2)
ax2.axvline(c='grey', lw=1.5)
ax2.axhline(c='grey', lw=1.5)
ax2.grid()
ax2.set_aspect('equal', 'box')

plt.show()

