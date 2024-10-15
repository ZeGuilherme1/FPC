# OK
import matplotlib.pyplot as plt
import numpy as np

def calcular(N):
    Nc = 0
    for i in range(N):
        x = -1.0 + 2.0 * np.random.rand()
        y = -1.0 + 2.0  * np.random.rand()
        if (x**2 + y**2 < 1.0):
            Nc += 1
    prob = Nc / N
    return 4 * prob

repeticoes = 4
Ns = np.array([10**3, 10**4, 10**5, 10**6, 10**7])

pi_medias = np.zeros(len(Ns))  
erros = np.zeros(len(Ns))      

def valores():
    for J, N in enumerate(Ns):  
        soma_resultados = 0
        for k in range(repeticoes):
            soma_resultados += calcular(N)
        media_resultados = soma_resultados / repeticoes
        pi_medias[J] = media_resultados  
        erros[J] = abs(np.pi - media_resultados)  
        print(f'N = {N}, Média de pi = {media_resultados:.6f}, Erro = {erros[J]:.6f}')


valores()


plt.figure(figsize=(10, 6))
plt.loglog(Ns, erros, marker='o', linestyle='-', color='b')
plt.xlabel('N (Número de pontos)')
plt.ylabel('Erro de pi - pi_MC|')
plt.title('Erro do cálculo de pi em função de N')
plt.grid(True, which="both", ls="--")
plt.show()  
