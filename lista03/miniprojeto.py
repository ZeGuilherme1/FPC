import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

L =  1.0
g = 9.8
T = 2.0

def rho1(x):
    return 1.0

def rho2(x):
    return 0.5 * (1+np.exp(-100 * (x - 0.5) ** 2))

def calcular_massas(N, rho):
    l0 =  L / N
    massas = np.zeros(N+1)

    for i in range(1, N):
        xi_esquerda = (i - 1) * 10
        xi_direita = i * l0
        massas[i], tmp = quad(rho, xi_esquerda, xi_direita)
    massas[0], tmp = quad(rho, 0, l0/2)
    massas[N], tmp = quad(rho, L-l0/2, L)

    return massas


def iteracao_jacobi(N, massas, f, num_iter = 1000, tol = 1e-6):
    l0 = L / N
    y = np.zeros(N+1)
    y_novo = np.zeros_like(y)
    for tmp in range(num_iter):
        for i in range(1, N):
            y_novo[i] = (massas[i] * g + f[i] + T *(y[i-1] + y[i+1])) / (2 * T)

        if(np.linalg.norm(y_novo - y)) < tol:
            break
        y = np.copy(y_novo)
    return y

def iteracao_gauss_seidel(N, massas, f, num_iter=1000, tol=1e-6):
    l0 = L / N
    y = np.zeros(N+1)
    for tmp in range(num_iter):
        y_velho = np.copy(y)
        for i in range(1, N):
            y[i] = (massas[i] * g + f[i] + T * (y[i-1] + y[i+1])) / (2 * T)
        if np.linalg.norm(y - y_velho) < tol:
            break
    return y

def plotar_forma_equilibrio(N, y, titulo):
    x = np.linspace(0, L, N+1)
    plt.plot(x, y, marker='o')
    plt.title(titulo)
    plt.xlabel('Comprimento da corda (m)')
    plt.ylabel('Deslocamento (m)')
    plt.grid(True)
    plt.show()

valores_n = [10, 20, 40, 80]

for N in valores_n:
    massas1 = calcular_massas(N, rho1)
    massas2 = calcular_massas(N, rho2)
    
    f = np.zeros(N+1)

    y_jacobi_rho1 = iteracao_jacobi(N, massas1, f)
    y_gauss_rho1 = iteracao_gauss_seidel(N, massas1, f)
    
    y_jacobi_rho2 = iteracao_jacobi(N, massas2, f)
    y_gauss_rho2 = iteracao_gauss_seidel(N, massas2, f)
    
    
    plotar_forma_equilibrio(N, y_jacobi_rho1, f'Jacobi N={N}, rho=1')
    plotar_forma_equilibrio(N, y_gauss_rho1, f'Gauss-Seidel N={N}, rho=1')
    
    plotar_forma_equilibrio(N, y_jacobi_rho2, f'Jacobi N={N}, rho variável')
    plotar_forma_equilibrio(N, y_gauss_rho2, f'Gauss-Seidel N={N}, rho variável')

N = 80
massas = calcular_massas(N, rho1)
f = np.zeros(N+1)
f[39] = 5.0  
y_jacobi_forca = iteracao_jacobi(N, massas, f)
y_gauss_forca = iteracao_gauss_seidel(N, massas, f)

plotar_forma_equilibrio(N, y_jacobi_forca, 'Jacobi com força em i=39')
plotar_forma_equilibrio(N, y_gauss_forca, 'Gauss-Seidel com força em i=39')

