import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 + 0.5 * np.sin(2*x)**3

def g(x):
    return 3 + 0.5 * np.cos(3*x)**5

intervalo = np.linspace(0, 2 * np.pi, 1000)

y_fx = f(intervalo)
y_gx = g(intervalo)



plt.plot(intervalo, y_fx, label="f(x) = 1 + 1/2*sin^3(2x)")
plt.plot(intervalo, y_gx, label="g(x) = 3 + 1/2*cos^5(3x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico das funções f(x) e g(x)')
plt.legend()
plt.grid(True)
plt.show()