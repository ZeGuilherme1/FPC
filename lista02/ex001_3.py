# OK

import numpy as np
import matplotlib.pyplot as plt

passos = [10**3, 10**4, 10**5, 10**6]

def movimentacao(passos):
    x, y = 0, 0
    pos_x = [x]
    pos_y = [y]

    for i in range(passos):
        direcao = np.random.randint(1, 5)

        if direcao == 1:
            y+=1
        elif direcao == 2:
            y-=1
        elif direcao == 3:
            x-=1
        elif direcao == 4:
            x+=1
        pos_x.append(x)
        pos_y.append(y)

    return pos_x, pos_y

for n_passos in passos:
    pos_x, pos_y = movimentacao(n_passos)

    plt.figure(figsize=(8, 8))
    plt.plot(pos_x, pos_y, label=f"{n_passos} passos")
    plt.title(f"Caminhada Aleatória - {n_passos} passos")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

        