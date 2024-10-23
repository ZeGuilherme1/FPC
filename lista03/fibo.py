import numpy as np 

"""fibonacci de forma recursiva
j = int(input("insira um valor para calcular fibonacci: "))

def fibor(j):
    if(j == 0):
        return 0
    if(j == 1):
        return 1
    return fibor(j-1) + fibor(j - 2)
print(fibor(j))"""

# Fibonacci implementado de maneira não recursiva, iterando!
def fibo(x):
    if (x == 0):
        return 0
    if (x == 1):
        return 1

    a, b = 0, 1
    for n in range(2, x+1):
        a, b = b, a + b
    
    return b
print(fibo(9))


# Segunda parte do primeiro exercício
def phi(x):
    return 1 / np.sqrt(x)

def iteracao(x0, iteracao_max=10):
    x_k = x0
    for k in range(1, iteracao_max + 1):
        xk_plus1 = phi(x_k)
        print(f"Iteração {k}: x_{k} = {x_k}, x_k+1 = {xk_plus1}")
        x_k = xk_plus1

x0 = 0.75
iteracao(x0)
print(1/np.sqrt(0.75))
