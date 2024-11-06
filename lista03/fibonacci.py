import numpy as np 

 # fibonacci de forma recursiva
j = int(input("insira um valor para calcular fibonacci: "))
resultados = []

def fibor(j):
        if(j == 0):
            return 0
        if(j == 1):
            return 1
        return fibor(j-1) + fibor(j - 2)

for k in range (j):
    resultados.append(fibor(k+1))

print(f"Os valores da sequência de Fibonacci para N = {j} são: ", resultados)


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
