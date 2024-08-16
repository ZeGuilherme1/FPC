import numpy as np
import time
import matplotlib.pyplot as plt

def mat_mul(A, B):
    num_linhas_A, num_col_A = len(A), len(A[0])
    num_linhas_B, num_col_B = len(B), len(B[0])

    assert num_col_A == num_linhas_B
                    
    C = []
    for linha in range(num_linhas_A):
        C.append([])
        for col in range(num_col_B):
            C[linha].append(0)
            for k in range(num_col_A):
                C[linha][col] += A[linha][k] * B[k][col]
    return C

def generate_sizes(start, end, step):
    return np.arange(start, end + 1, step)

# Gerar tamanhos de matrizes de 1000 até 5000 com passo de 1000
sizes = generate_sizes(1000, 5000, 1000)

tempo_for = []
tempo_multiplicacao = []

for size in sizes:
    A = np.random.rand(size, size).tolist()
    B = np.random.rand(size, size).tolist()

    # Medindo o tempo usando o for
    start_time_for = time.time()
    C = mat_mul(A, B)
    end_time_for = time.time()
    total_time_for = end_time_for - start_time_for
    tempo_for.append(total_time_for)

    # Medindo o tempo usando o operador @
    A_np = np.array(A)
    B_np = np.array(B)

    start_time = time.time()
    C_op = A_np @ B_np
    end_time = time.time()
    total_time = end_time - start_time
    tempo_multiplicacao.append(total_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, tempo_for, label="For loops")
plt.plot(sizes, tempo_multiplicacao, label="NumPy matmul (@)")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Dimensão da Matriz (n x n)")
plt.ylabel("Tempo de Cálculo (segundos)")
plt.title("Tempo de Cálculo da Multiplicação de Matrizes")
plt.legend()
plt.grid(True)
plt.show()
