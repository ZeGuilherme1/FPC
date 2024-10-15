# OK

import numpy as np
import matplotlib.pyplot as plt 

# N == qntd de tentativas e M == qntd de dados
def jogar_dados(N, M):
    resultados = np.sum(np.random.randint(1, 7, (N, M)), axis=1)        # Gerando valores de 1-6 e somando eles com np.sum
    return resultados


# Plotagem do gráfico
# bins == definine o limite dos intervalos, nesse caso M*6+1 == M*6 por conta do in range ser sempre indexado a partir do 0
# sendo M a quantidade de dados;
# counts == array que armazena a contagem de quantos valores dentro de resultados caem dentro de cada intervalo definido em bins
# ou seja um array com a contagem de quantas vezes cada valor se repete quando os dados são jogados

def plot_histograma(N, M):
    resultados = jogar_dados(N, M)
    counts, bins = np.histogram(resultados, bins=range(M, M*6+1))
    plt.stairs(counts, bins) # counts == array que armazena a contagem de quantos valores dentro de resultados caem dentro de cada intervalo definido em bins
    plt.title(f'Histograma da soma para {N} jogadas e {M} dados')
    plt.xlabel('Soma dos valores dos dados')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()


# Array com os valores
valores_N = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7]
valores_M = [2, 4, 8]

# For para aplicar a função da plotagem nos valores que estão dentro do array
for M in valores_M:
    for N in valores_N:
        plot_histograma(N, M)
