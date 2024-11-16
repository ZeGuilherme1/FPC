# Matrizes dadas no exercício
A = [[3, -1, -1],
     [-1, 3, -1],
     [-1, -1, 3]]
b = [1, 2, 3]

# Iniciando x, y, z com uma aproximação inicial
x, y, z = 0, 0, 0

tolerance = 1e-6 
max_iterations = 100 

# Aplicando o método
for iteration in range(max_iterations):
    x_new = (1 - (-1)*y - (-1)*z) / 3
    y_new = (2 - (-1)*x - (-1)*z) / 3
    z_new = (3 - (-1)*x - (-1)*y) / 3

    # Verificando a convergência
    if abs(x_new - x) < tolerance and abs(y_new - y) < tolerance and abs(z_new - z) < tolerance:
        print(f"Convergiu na iteração {iteration + 1}")
        break

    # Atualizando as variáveis
    x, y, z = x_new, y_new, z_new

print(f"Solução aproximada: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")
