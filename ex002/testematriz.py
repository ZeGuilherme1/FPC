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

# Dimensão da matriz
size = 1000

# Gerar matrizes aleatórias
A = np.random.rand(size, size).tolist()
B = np.random.rand(size, size).tolist()
    
# Medindo o tempo usando o for
start_time_for = time.time()
C = mat_mul(A, B)
end_time_for = time.time()
total_time_for = end_time_for - start_time_for

# Medindo o tempo usando o operador @
A_np = np.array(A)
B_np = np.array(B)

start_time = time.time()
C_op = A_np @ B_np
end_time = time.time()
total_time = end_time - start_time

# Exibindo os tempos
print(f"Tempo de cálculo usando loops: {total_time_for:.6f} segundos")
print(f"Tempo de cálculo usando NumPy matmul (@): {total_time:.6f} segundos")
