import numpy as np

# Матриця коефіцієнтів
A = np.array([
    [1, 1, 1],
    [9, 3, 1],
    [1, -1, 1]
])

# Вектор правих частин
B = np.array([12, 54, 2])

# Розв'язання системи лінійних рівнянь
solution = np.linalg.solve(A, B)
print(solution)