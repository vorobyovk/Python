import numpy as np

# Матриця коефіцієнтів
A = np.array([
    [1, 1, 1],
    [1, -1, 0],
    [1, 0, -1]
])

# Матриця констант
B = np.array([1328, -120, 100])

# Розв'язання системи лінійних рівнянь
solution = np.linalg.solve(A, B)
print(solution)