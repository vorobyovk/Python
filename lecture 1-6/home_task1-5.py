import numpy as np

def get_polynom(coords):
    # Кількість точок
    n = len(coords)

    # Матриця коефіцієнтів
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i, (x, y) in enumerate(coords):
        for j in range(n):
            A[i, j] = x ** j
        B[i] = y

    # Розв'язання системи лінійних рівнянь для знаходження коефіцієнтів
    coefficients = np.linalg.solve(A, B)

    return coefficients

# Приклад використання функції
coords = [(1, 12), (3, 54), (-1, 2)]
coefficients = get_polynom(coords)
print(coefficients)
