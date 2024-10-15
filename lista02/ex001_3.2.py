# OK

import numpy as np
import matplotlib.pyplot as plt

M1 = 1000
M2 = 10000

N = 10**4

def movimentacao(n_passos, m_simulacoes):
    dist_quadratica = np.zeros(n_passos)

    for i in range(m_simulacoes):
        x, y, z = 0, 0, 0
        for k in range(n_passos):
            direcao = np.random.randint(1, 7)
            if direcao == 1:
                y += 1
            elif direcao == 2:
                y -= 1
            elif direcao == 3:
                x -= 1
            elif direcao == 4:
                x += 1
            elif direcao == 5:
                x += 1
            elif direcao == 6:
                x -= 1
            dist_quadratica[k] += x**2 + y**2 + z**2 
    dist_quadratica /= m_simulacoes
    return dist_quadratica

dist_1000 = movimentacao(N, M1)
dist_10000 = movimentacao(N, M2)

plt.plot(dist_1000, label=f'M = {M1}')
plt.plot(dist_10000, label=f'M = {M2}')
plt.title('Distância quadrática média percorrida')
plt.xlabel('Número de passos')
plt.ylabel('Distância quadrática média')
plt.legend()
plt.grid(True)
plt.show()