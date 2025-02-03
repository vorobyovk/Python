import numpy as np

# Матриця коефіцієнтів
a = np.matrix(
    [
        [1, 1, 1],
        [0.05, 0.07, 0],
        [0.05, 0, 0.06],
    ]
)

# Матриця констант
b = np.transpose(np.matrix((50000, 2250, 1400)))

# Розв'язання системи лінійних рівнянь
x = np.linalg.solve(a, b)

print(x)
