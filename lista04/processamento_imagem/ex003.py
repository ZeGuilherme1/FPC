import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread('/home/zegui/FPC/lista04/processamento_imagem/stinkbug.png')
height, width, tmp = img.shape

def suavizar(matriz, height, width, iteracoes):
    for n in range(iteracoes):
        matriz_suavizada = np.copy(matriz)
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                 matriz_suavizada[i][j] = ((matriz[i][j] + matriz[i+1][j] + matriz[i-1][j] + matriz[i][j+1] + matriz[i][j-1]) / 5)
        matriz = np.copy(matriz_suavizada)
    return matriz


img_suavizada = suavizar(img, height, width, iteracoes = 10)

plt.title("Original")
plt.imshow(img)
plt.show()

plt.title("Suavizada")
plt.imshow(img_suavizada)
plt.show()


