import numpy as np
import matplotlib.pyplot as plt

def iteracao_jacobi(x, y):
    x_novo = (1 / 3) * (2 + y)
    y_novo = (1 / 4) * (1 + 2 * x)
    return x_novo, y_novo

def convergencia_jacobi(epsilons, max_iter=1000):
    erros_finais = []
    for epsilon in epsilons:
        x, y = 0, 0
        iter_count = 0
        while iter_count < max_iter:
            x_novo, y_novo = iteracao_jacobi(x, y)
            if abs(x_novo - x) < epsilon and abs(y_novo - y) < epsilon:
                break
            x, y = x_novo, y_novo
            iter_count += 1
        erro_final = max(abs(x_novo - x), abs(y_novo - y))
        erros_finais.append(erro_final)
    return erros_finais

epsilons = [10**-2, 10**-3, 10**-4, 10**-5, 10**-6, 10**-7, 10**-8]
erros = convergencia_jacobi(epsilons)

plt.figure(figsize=(10, 6))
plt.plot(epsilons, erros, marker='o', linestyle='-', color='r')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Epsilon (Erro)")
plt.ylabel("Erro Final")
plt.title("Erro Final em Função de Epsilon para o Método de Jacobi")
plt.grid(True)
plt.show()
