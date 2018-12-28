# import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
# from pylab import *
import matplotlib.pyplot as plt
import numpy as np
# sns.set_style("whitegrid", {'axes.grid': False})

fig = plt.figure(figsize=(6, 6))

ax = Axes3D(fig)  # Method 1
# ax = fig.add_subplot(111, projection='3d') # Method 2

x = np.random.uniform(1, 20, size=20)
y = np.random.uniform(1, 100, size=20)
z = np.random.uniform(1, 100, size=20)

ax.scatter(x, y, z, c=x, marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
