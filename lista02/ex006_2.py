# Ok

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calcular(N):
    Nc = 0
    pontos_dentro = []
    pontos_fora = []

    for i in range(N):
        x = -1.0 + 2.0 * np.random.rand()
        y = -1.0 + 2.0 * np.random.rand()
        z = -1.0 + 2.0 * np.random.rand()

        if (x**2 + y**2 + z**2 < 1):
            Nc += 1
            pontos_dentro.append((x, y, z))
        else:
            pontos_fora.append((x, y, z))
    
    prob = Nc / N
    pi_estimado = prob * 6

    pontos_dentro = np.array(pontos_dentro)
    pontos_fora = np.array(pontos_fora)

    return pi_estimado, pontos_dentro, pontos_fora

def plotar_pontos(pontos_dentro, pontos_fora):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(pontos_dentro[:, 0], pontos_dentro[:, 1], pontos_dentro[:, 2], color='b', s=1)
    ax.scatter(pontos_fora[:, 0], pontos_fora[:, 1], pontos_fora[:, 2], color='r', s=1, alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Monte Carlo - Estimativa de Pi em 3D')

    plt.savefig('/home/zegui/projetos/FPC/teste.png')

N = 1000000
resultado, pontos_dentro, pontos_fora = calcular(N)
print(f"Estimativa de pi: {resultado}")
plotar_pontos(pontos_dentro, pontos_fora)
