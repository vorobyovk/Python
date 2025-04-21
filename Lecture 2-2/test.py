import numpy as np
A = np.array(
     [[1, -2, 3],
     [1, -2, 2],
     [-2, 0, 1],
     ]
)
print(round(np.linalg.det(A)))

# A = np.array(
#     [[-4, 9],
#      [0, 5],
#      ]
#     )
# print(round(np.linalg.det(A)))

# # Оголошення вихідної матриці
# matrix = np.array([[1, 0, 3],
#                    [-1, -1, 2],
#                    [4, 7, 2]])
# # Обчислення оберненої матриці
# inverse_matrix = np.linalg.inv(matrix)
# print("Вихідна матриця:")
# print(matrix)
# print("\nОбернена матриця:")
# print(inverse_matrix)

# a = np.array(
#     [[3, 0, 0],
#      [2, 1, 0],
#      [1, 1, 1]]
#     )
# b = np.array([60, 50, 90])

# print(f"A = {a}")
# print(b)
# print(np.linalg.solve(a, b))

# a = np.array([[3, 0, 0], [1, 2, 0], [0, 1, -1]])
# b = np.array([30, 18, 2])
# x = np.linalg.solve(a, b)

# print ("Матриця A:\n", a)
# print ("Вектор b:\n", b)
# print ("Розв'язання системи:\n", x)

# res = 0.5*x[2]+x[0]*0.5*x[1]
# print(res)

# a = np.array(
#     [[2, 3, 4],
#      [1, 2, 0],
#      [3, 0, 1]]
#     )
# b = np.array([150, 70, 90])

# print(f"A = {a}")
# print(b)
# print(np.linalg.solve(a, b))