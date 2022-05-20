import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import field as f


def B1(t):
    return np.array([0, 0, t/10])

def B2(t):
    return np.array([0, 0, 1])

def E(t):
    return np.array([0, 0, 0])

a=f.mov(-1, 1, np.array([0.1, 0.1, 0.1]), B1, E, 20, 'RK', 0.01)
b=f.mov(-1, 1, np.array([0.1, 0.1, 0.1]), B2, E, 20, 'RK', 0.01)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(a[0], a[1], a[2], label='B=t/10')
ax.plot(b[0], b[1], b[2], label='B=1')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

a=f.mov(-1, 1, np.array([0.1, 0.1, 0.1]), B1, E, 20, 'RK', 0.01)
b=f.mov(1, 1, np.array([0.1, 0.1, 0.1]), B1, E, 20, 'RK', 0.01)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(a[0], a[1], a[2], label='-e')
ax.plot(b[0], b[1], b[2], label='+e')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()