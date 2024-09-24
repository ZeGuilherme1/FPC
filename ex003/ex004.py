import numpy as np
import matplotlib as plt



def mapa_logistico(a, x0, N):
    x = np.zeros(N+1)
    x[0] = x0
    for n in range(1, N+1):
        x[n] = a * x[n-1] * (1 - x[n-1])
    return x

N = 5000
x0 = 0.1
valores_a = [1, 2, 3.8, 4]


plt.figure(figusize=(10, 6))

for a in valores_a:
    sequence = mapa_logistico(a, x0, N)
    mean = np.mean(sequence)
    variance = np.var(sequence)
    print(f"Para a = {a}: temos a média = {mean:.4f} e variância = {variance:.4f}")

plt.title('Mapa Logístico para diferentes valores de a', fontsize=14)
plt.xlabel('Iteração (n)', fontsize=12)
plt.ylabel('Valor de x', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True)

plot.show()
# Isso realmente tá certo (?)
