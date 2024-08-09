import numpy as np
import time

def calcular_vetor(n):
    a = np.random.rand(n)
    b = np.random.rand(n)
    alpha = np.random.rand()
    beta = np.random.rand()

    start_time = time.time()
    c = alpha * a + beta * b
    end_time = time.time()
    exec_time = end_time - start_time

    return c, a, b, alpha, beta, exec_time      

n = float(input("Insira a dimensão dos vetores (use notação científica como 1e5 para 10^5): "))
n = int(n)
c, a, b, alpha, beta, exec_time = calcular_vetor(n)

print("\nVetor A: ", a)
print("Vetor B:", b)
print("\nEscalar Alpha:", alpha)
print("Escalar Beta:", beta)
print("\nO resultado do vetor C é:", c) 

print("\nO tempo de execução foi de:", exec_time, "segundos")
