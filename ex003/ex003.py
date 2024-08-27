import numpy as np

def mapa_logistico(a, x0, N):
    x = np.zeros(N+1)
    x[0] = x0
    for n in range(1, N+1):
        x[n] = a * x[n-1] * (1 - x[n-1])
    return x

N = 5000
x0 = 0.1
a_values = [1, 2, 3.8, 4]

for a in a_values:
    sequence = mapa_logistico(a, x0, N)
    mean = np.mean(sequence)
    variance = np.var(sequence)
    print(f"Para a = {a}: média = {mean:.4f}, variância = {variance:.4f}")

# Isso realmente tá certo (?)
