import numpy as np
#Emanuel Martins - 2022007043


n = int(input("Entre com a ordem da matriz de coeficientes do sistema.\n n = "))

print("Entre com os elementos da matriz de coeficientes do sistema.")
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i}][{j}] = "))


b = np.zeros(n)
print("Entre com os elementos dos termos independentes de cada equação.")
for i in range(n):
    b[i] = float(input(f"b[{i}] = "))
B = np.concatenate((A, np.expand_dims(b, axis=1)), axis=1)


print("\nMatriz expandida:")
print(B)

for k in range(n):
    max_index = np.argmax(np.abs(B[k:, k])) + k
    if B[max_index][k] == 0:
        raise ValueError("O sistema não tem solução única.")
    B[[k, max_index]] = B[[max_index, k]]

    for i in range(k+1, n):
        m = B[i][k] / B[k][k]
        B[i][k] = 0
        for j in range(k+1, n+1):
            B[i][j] = B[i][j] - m * B[k][j]

print("\nMatriz escalonada:")
print(B)

x = np.zeros(n)
x[n-1] = B[n-1][n] / B[n-1][n-1]
for i in range(n-2, -1, -1):
    S = 0
    for k in range(i+1, n):
        S = S + B[i][k] * x[k]
    x[i] = (B[i][n] - S) / B[i][i]

print("\nSolução:")
for i in range(n):
    print(f"x[{i}] = {x[i]}")
