import numpy as np
import matplotlib.pyplot as plt

def phi(x):
    return 1 / np.sqrt(x)

def iteracao(x0, iteracao_max=10):
    valores_x = [x0] 
    for k in range(iteracao_max):
        xk_plus1 = phi(valores_x[-1])  
        valores_x.append(xk_plus1)  
    return valores_x

x0 = 0.75
iteracao_max = 10

valores_x = iteracao(x0, iteracao_max)

x = np.linspace(0.5, 1.2, 400)  
y = phi(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\phi(x) = 1/\sqrt{x}$', color='blue') 
plt.plot(x, x, label=r'$y = x$', color='black', linestyle='--')  

for k in range(len(valores_x) - 1):
    plt.plot([valores_x[k], valores_x[k]], [valores_x[k], valores_x[k+1]], color='red', linestyle='--')
    plt.plot([valores_x[k], valores_x[k+1]], [valores_x[k+1], valores_x[k+1]], color='red', linestyle='--')

plt.title(r'Iteração de Ponto Fixo para $\phi(x) = 1/\sqrt{x}$')
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.legend()
plt.grid()
plt.show()
