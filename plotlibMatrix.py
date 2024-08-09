# Bibliotecas utilizadas
import numpy as np
import time
from matplotlib import pyplot as plt

# Cria as listas com as dimensões que serão utilizadas, bem como as listas para armazenarmos os tempos
dimensoes = [1000, 2000, 3000, 4000 ]

tempos_m2 = []
tempos_m3 = []
tempos_m4 = []

# Utiliza o loop for do python para gerar uma matriz aleatória com base em cada dimensão setada na 
# primeira lista e aplica cada exponenciação em cada matriz
for dim in dimensoes:
    array = np.random.randint(10, size=(dim, dim))

    start_time = time.time()
    np.linalg.matrix_power(array, 2)
    end_time = time.time()
    tempos_m2.append(end_time - start_time)
    
    start_time = time.time()
    np.linalg.matrix_power(array, 3)
    end_time = time.time()
    tempos_m3.append(end_time - start_time)
    
    start_time = time.time()
    np.linalg.matrix_power(array, 4)
    end_time = time.time()                                      
    tempos_m4.append(end_time - start_time)


# Códigos da matplotlib

# Observação: "plt.loglog" irá plotar o gráfico em LogLog, para plotar o gráfico como função linear
# é preciso trocar para os comandos para "plt.plot", você pode fazer 2 blocos diferentes para plotar
# 2 gráficos de uma só vez mas eu tô com preguiça

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.loglog(dimensoes, tempos_m2, label='m=2', marker='o')
plt.loglog(dimensoes, tempos_m3, label='m=3', marker='o')
plt.loglog(dimensoes, tempos_m4, label='m=4', marker='o')
plt.xlabel('Dimensão da Matriz (n)')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escala Linear')
plt.legend()
plt.grid(True)      
plt.tight_layout()
plt.show()
