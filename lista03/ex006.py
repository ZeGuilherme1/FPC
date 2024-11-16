import numpy as np
import matplotlib.pyplot as plt

# Função dada f(x) = x * e^(-x^2) - 0.1
def f(x):
    return x * np.exp(-x**2) - 0.1

# Derivada de f(x)
def df(x):
    return np.exp(-x**2) * (1 - 2 * x**2)

# Método de Newton
def metodo_newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_novo = x - f(x) / df(x)
        if abs(x_novo - x) < tol:
            return x_novo, i + 1  # Retorna a raiz e o número de iterações
        x = x_novo
    raise ValueError("O método de Newton não convergiu.")

# Plotando a função no intervalo [-1, 2]
x_vals = np.linspace(-1, 2, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfico da função f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()

# Escolha dos pontos iniciais próximos das raízes no intervalo [0, 2]
x0_1 = 0.1  # Próximo da primeira raiz
x0_2 = 1.5  # Próximo da segunda raiz

# Calculando as raízes usando o Método de Newton
raiz_1, iteracoes_1 = metodo_newton(f, df, x0_1)
raiz_2, iteracoes_2 = metodo_newton(f, df, x0_2)

print(f"Primeira raiz: {raiz_1:.6f} encontrada em {iteracoes_1} iterações.")
print(f"Segunda raiz: {raiz_2:.6f} encontrada em {iteracoes_2} iterações.")
