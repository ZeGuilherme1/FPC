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
