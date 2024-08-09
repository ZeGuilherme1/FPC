# Bibliotecas utilizadas
import numpy as np
import time
from matplotlib import pyplot as plt

# Função para gerar e valores aleatórios em cada vetor utilizando a função "np.random.rand" do numpy
# e também calcular os vetores com base nos valores setados na lista "dimensoes"
def calcular_vetor(n): 
    a = np.random.rand(n)
    b = np.random.rand(n)
    alpha = np.random.rand()
    beta = np.random.rand()

    start_time = time.time()
    c = alpha * a + beta * b
    end_time = time.time()
    exec_time = end_time - start_time

    return c, exec_time

# Cria uma lista com cada dimensão utilizada e uma para os resultados a serem armazenados
dimensoes = [10**5, 10**6, 10**7, 10**8] 
resultados = []

# Aplicada a função de calcular o vetor para cada valor em dimensoes
for n in dimensoes:
    c, tempo = calcular_vetor(n)
    resultados.append((n, c, tempo))
    print(f"Dimensão: {n}, Tempo de execução: {tempo:.6f} segundos")

# Armazena o tempo de execução
tempos_execucao = [resultado[2] for resultado in resultados]

# Comandos do numpy para plotar os gráficos
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(dimensoes, tempos_execucao, marker='o')
plt.title('Tempo de Execução vs Dimensão (Escala Linear)')
plt.xlabel('Dimensão n')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.loglog(dimensoes, tempos_execucao, marker='o')
plt.title('Tempo de Execução vs Dimensão (Escala Log-Log)')
plt.xlabel('Dimensão n')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)

plt.tight_layout()
plt.show()
