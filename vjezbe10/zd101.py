import field as f
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a=f.mov(-1, 1, np.array([0.1, 0.1, 0.1]), np.array([0, 0, 1]), np.array([0, 0, 0]), 20)
b=f.mov(1, 1, np.array([0.1, 0.1, 0.1]), np.array([0, 0, 1]), np.array([0, 0, 0]), 20)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(a[0], a[1], a[2])
ax.plot(b[0], b[1], b[2])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()