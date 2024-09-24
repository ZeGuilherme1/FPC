def mapeamento_logistico_manual(a, N=5000, x0=0.1):
    
    x = [x0]
  
    for n in range(1, N):
        x_n = a * x[-1] * (1 - x[-1])
        x.append(x_n)
    
    # calcular a média usando a função sum do python
    media = sum(x) / N
    
    # variancia
    variancia = sum((xi - media) ** 2 for xi in x) / (N - 1)
    
    return media, variancia

# diferentes valores de A pedidos no exercício
for a in [1, 2, 3.8, 4]:
    media, variancia = mapeamento_logistico_manual(a)
    print(f'a={a}: média={media}, variância={variancia}')
