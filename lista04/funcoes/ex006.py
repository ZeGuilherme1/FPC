import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.cos(x) * np.cos(y)

x = np.linspace(0, 2 * np.pi, 100) 
y = np.linspace(0, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

df_dx, df_dy = np.gradient(Z, x, y)

plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, levels=20, cmap='jet')
plt.colorbar(contour)
plt.title(r'Curvas de nível: $f(x, y) = \cos(x) \cos(y)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(figsize=(8, 6))
plt.quiver(X, Y, df_dx, df_dy, color='k', scale=50)
plt.title('Gradiente de $f(x, y)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, levels=20, cmap='jet')
plt.colorbar(contour)
plt.quiver(X, Y, df_dx, df_dy, color='k', scale=50)
plt.title(r'Curvas de nível e gradiente de $f(x, y)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
