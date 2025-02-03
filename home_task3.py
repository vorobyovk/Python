import numpy as np

# Матриця коефіцієнтів
A = np.array([
    [3, 0, 3],
    [6, 1/4, 0],
    [1, 1/3, 1]
])

# Вектор правих частин
B = np.array([1, 1, 1])

# Розв'язання системи лінійних рівнянь
solution = np.linalg.solve(A, B)

# Знаходимо a^2, b^2, c^2
a2 = 1 / solution[0]
b2 = 1 / solution[1]
c2 = 1 / solution[2]

print(a2, b2, c2)
