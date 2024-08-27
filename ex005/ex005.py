import numpy as np
import matplotlib.pyplot as plt
a_min, a_max = 1, 4.0
n_iteracoes = 1000      
ultimo_n = 100
x0 = 0.5

a_valores = np.linspace(a_min, a_max, 10000)
plt.figure(figsize=(10, 7))

for a in a_valores:
    x = x0
    
    for i in range(n_iteracoes):
        x = a * x * (1 - x)
    x_vals = []
    
    for i in range(ultimo_n):
        x = a * x * (1 - x)
        x_vals.append(x)

    plt.plot([a] * ultimo_n, x_vals, ',k', alpha=0.1)  
plt.title('Diagrama de Bifurcação')
plt.xlabel('Valor de a')
plt.ylabel('Valores de x')
plt.show()

# Eu tentei fuçar muito pra entender a parte matemática e tudo que eu entendi foi que esse diagrama é uma das bases da teoria do Caos
# e também que aparentemente ele é usado pra descrever a reprodução de coelhos (?)
# espero que o professor realmente não queira que expliquemos a parte matemática além do código
