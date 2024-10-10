import numpy as np
import matplotlib.pyplot as plt
import math

def funcao(N):
    return math.sqrt(1 - N**2) 

def soma_riemann(N):
    delta_x = 1/N
    soma = 0

    for i in range(N):
        x_i = i * delta_x
        soma += funcao(x_i) * delta_x

    return soma * 4

valores_N = [10, 100, 1000, 10000, 100000]
resultados = []

for N in valores_N:
    pi_aproximado = soma_riemann(N)
    erro = abs(math.pi - pi_aproximado)
    resultados.append((N, pi_aproximado, erro))

for N, pi_aproximado, erro in resultados:
    print(f'N = {N}, pi_aproximado = {pi_aproximado:.6f}, erro = {erro:.6f}')