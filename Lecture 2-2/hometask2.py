import numpy as np

# a = np.array(
#     [[20, 3, 0],
#      [8, 28, 4],
#      [4, 12, 32]]
#     )
# b = np.array([775, 1012, 696])

# print(f"A = {a}")
# print(b)
# print(np.linalg.solve(a, b))

a = np.array(
     [[-1, 1, 2],
      [0, -1, -3],
      [4, -3, 2]]
     )
b = np.array([1, -4, 7])
print(f" result {np.linalg.solve(a, b)}")

# delta = round(np.linalg.det(a))
# a2 = np.array(
#      [[1, 1, 2],
#       [-4, -1, -3],
#       [7, -3, 2]]
#      )
# delta1 = round(np.linalg.det(a2))
# a3 = np.array(
#      [[-1, 1, 2],
#       [0, -4, -3],
#       [4, 7, 2]]
#      )
# delta2 = round(np.linalg.det(a3))
# a4 = np.array(
#      [[-1, 1, 1],
#       [0, -1, -4],
#       [4, -3, 7]]
#      )
# delta3 = round(np.linalg.det(a4))

# print(f"delta = {delta} delta1 = {delta1} delta2 = {delta2} delta3 = {delta3}")
# print(f"x1 = {delta1/delta} x2 = {delta2/delta} x3 = {delta3/delta}")

A = a  # Матриця коефіцієнтів A (ліва частина системи)
# Вектор вільних членів b (значення праворуч від знака рівності)
# Замініть ці значення на значення з вашої системи
# --- Розв'язання матричним методом ---

try:    
    A_inv = np.linalg.inv(A)    
    x = A_inv @ b    
    print(np.round(x, decimals=5))
    check = A @ x    
    if np.allclose(check, b):
        print("\nПеревірка успішна: A @ x наближено дорівнює b.")
    else:
        print("\nУвага: Перевірка показує розбіжність. Можливі проблеми з точністю обчислень або помилка.")
except np.linalg.LinAlgError:    
    print("\nПомилка: Матриця A є сингулярною (визначник дорівнює 0).")
    print("Система не має єдиного розв'язку (може не мати розв'язків або мати безліч).")
    print("Матричний метод (через обернену матрицю) не може бути застосований.")