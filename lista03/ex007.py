import numpy as np

print("Primeira parte do sétimo exercício: ")
print("-" * 50)
A1 = np.array([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])

# Inicializando um vetor inicial
x1 = np.array([1, 1, 1], dtype=float)

tolerance = 1e-6
max_iterations = 1000
lambda_novo = 0

# Método das potências para a matriz específica
for i in range(max_iterations):
    # Multiplicação da matriz A pelo vetor x
    x_novo = A1 @ x1
    
    # Normalização do vetor
    x_novo_norm = np.linalg.norm(x_novo)
    x_novo = x_novo / x_novo_norm
    
    # Aproximação do autovalor dominante
    lambda_novo = np.dot(x_novo, A1 @ x_novo)
    
    # Critério de parada
    if abs(lambda_novo - lambda_novo) < tolerance:
        break
    
    # Preparar para a próxima iteração
    x1 = x_novo
    lambda_novo = lambda_novo

print("Autovalor dominante aproximado para a matriz específica:", lambda_novo)
print("Autovetor dominante correspondente para a matriz específica:", x1)

print("-" * 50)
print("Segunda parte do sétimo exercício")

# Parâmetros para a matriz aleatória
n = 5  # Tamanho da matriz (pode ser ajustado conforme necessário)

# Gerando uma matriz diagonal com valores aleatórios entre 0 e 1
diagonal_values = np.random.rand(n)
A2 = np.diag(diagonal_values)

# Inicializando o vetor inicial
x2 = np.ones(n, dtype=float)
lambda_novo = 0

# Método das potências para a matriz aleatória
for i in range(max_iterations):
    # Multiplicação da matriz A pelo vetor x
    x_novo = A2 @ x2
    
    # Normalização do vetor
    x_novo_norm = np.linalg.norm(x_novo)
    x_novo = x_novo / x_novo_norm
    
    # Aproximação do autovalor dominante
    lambda_novo = np.dot(x_novo, A2 @ x_novo)
    
    # Critério de parada
    if abs(lambda_novo - lambda_novo) < tolerance:
        break
    
    # Preparar para a próxima iteração
    x2 = x_novo
    lambda_novo = lambda_novo

print("Valores na diagonal de A:", diagonal_values)
print("Autovalor dominante aproximado para a matriz aleatória:", lambda_novo)
print("Autovetor dominante correspondente para a matriz aleatória:", x2)
