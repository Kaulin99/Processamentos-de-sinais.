import matplotlib.pyplot as plt

# Sinal original
x = [0, -2, -1, 0, 1, 2, 3, 0, 0]
n = list(range(len(x)))

# Transformações:

# 1. Deslocamento para a direita em 2 unidades: x[n - 2]
n_shifted = [i + 2 for i in n]  # Desloca o índice
x_shifted = x  # Os valores permanecem os mesmos

# 2. Reflexão temporal: x[-n]
n_reflected = [-i for i in n]
x_reflected = x

# 3. Compressão por 2: x[2n]
n_compressed = list(range(0, len(x)*2, 2))
x_compressed = []
for i in n:
    idx = 2 * i
    if idx < len(x):
        x_compressed.append(x[idx])
    else:
        break
n_compressed = list(range(len(x_compressed)))  # Ajusta o tamanho do eixo n

# Plotagem
plt.figure(figsize=(12, 8))

# Sinal original
plt.subplot(2, 2, 1)
plt.stem(n, x)
plt.title("Sinal Original x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)

# Deslocamento para a direita
plt.subplot(2, 2, 2)
plt.stem(n_shifted, x_shifted)
plt.title("Deslocamento: x[n - 2]")
plt.xlabel("n")
plt.ylabel("x[n - 2]")
plt.grid(True)

# Reflexão temporal
plt.subplot(2, 2, 3)
plt.stem(n_reflected, x_reflected)
plt.title("Reflexão Temporal: x[-n]")
plt.xlabel("n")
plt.ylabel("x[-n]")
plt.grid(True)

# Compressão por 2
plt.subplot(2, 2, 4)
plt.stem(n_compressed, x_compressed)
plt.title("Compressão por 2: x[2n]")
plt.xlabel("n")
plt.ylabel("x[2n]")
plt.grid(True)

plt.tight_layout()
plt.show()


