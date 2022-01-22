import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = list(np.linspace(-4, 4, 100))
Y = list(np.linspace(-4, 4, 100))
X, Y = np.meshgrid(X, Y)
Z = np.sin((X**2 + Y**2)/4)
# Z = (np.sin((X**2 + Y**2)/4)).tolist()
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()
