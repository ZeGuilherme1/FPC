import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('/home/zegui/FPC/lista04/concrete.jpg')
matriz_recortada = img[:, :, 0]
plt.imshow(img)
plt.show()
height, width, tmp = img.shape

def recortar(matriz, height, width, height_inicial = 0, width_inicial = 0):
    matriz_cortada = np.zeros((height, width, matriz.shape[2]), dtype=matriz.dtype)
    for i in range(height):
        for j in range(width):
            matriz_cortada[i][j] = matriz[height_inicial + i][width_inicial + j]

    return matriz_cortada


matriz_recortada = recortar(img, 100, 200, 150, 150)
plt.imshow(matriz_recortada)
plt.show()

def agregados_count(matriz_recortada, limiar):
    matriz_recortada = matriz_recortada / np.max(matriz_recortada)

    img = (matriz_recortada > limiar) * 1.0

    cinza_escuro = np.sum(img == 0)
    cinza_claro = np.sum(img == 1)

    return cinza_escuro, cinza_claro

limiar = 0.5
cinza_escuro, cinza_claro = agregados_count(matriz_recortada, limiar)
proporcao =  cinza_escuro / (cinza_escuro + cinza_claro)
print("A proporção de pixeis escuros para claros é de:", proporcao)

