import numpy as np

# Definindo o sistema de equações
A = np.array([[3, -1, -1],
              [-1, 3, -1],
              [-1, -1, 3]])

b = np.array([1, 2, 3])

# Chute inicial para as variáveis x, y e z
x = np.zeros_like(b, dtype=float)

# Definir o número máximo de iterações e a tolerância para convergência
max_iterations = 100
tolerance = 1e-10

# Função que implementa o método iterativo de Jacobi
def jacobi(A, b, x0, max_iterations, tolerance):
    # Obter o tamanho do vetor b (ou seja, o número de equações)
    n = len(b)
    
    # Criar uma cópia do chute inicial
    x = x0.copy()
    
    # Iterar até o número máximo de iterações permitido
    for iteration in range(max_iterations):
        # Inicializar um novo vetor para armazenar os valores de x calculados na iteração atual
        x_new = np.zeros_like(x)
        
        # Loop para calcular cada variável x[i] na iteração atual
        for i in range(n):
            # Calcular a soma dos produtos A[i][j] * x[j] para todos os j ≠ i
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x[j]
            
            # Atualizar x_new[i] usando a fórmula do método de Jacobi
            x_new[i] = (b[i] - soma) / A[i][i]
        
        # Verificar se os valores de x na iteração atual estão próximos dos valores anteriores (convergência)
        convergiu = True
        for i in range(n):
            if abs(x_new[i] - x[i]) > tolerance:
                convergiu = False
                break
        
        # Se todos os valores convergiram dentro da tolerância, retornar o resultado
        if convergiu:
            print(f"Convergência atingida após {iteration+1} iterações.")
            return x_new
        
        # Atualizar x para a próxima iteração
        x = x_new

    # Caso o número máximo de iterações seja atingido, informar ao usuário
    print("Número máximo de iterações atingido.")
    return x

# Executar o método de Jacobi
solution = jacobi(A, b, x, max_iterations, tolerance)
print("Solução aproximada:", solution)
