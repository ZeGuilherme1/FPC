import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return np.cos(x) * np.cos(y)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.linspace(-2 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='jet', edgecolor='k')
colorbar = fig.colorbar(surf, ax=ax, shrink = 0.5, aspect = 10)
colorbar.set_label('f(x, y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

ax.view_init(elev = 30, azim = 45)
plt.title('Superfície 3D: f(x, y) = cos(x) * cos(y)')
plt.show()
