import numpy as np
import matplotlib.pyplot as plt

# def print_diagonals(matrix):
#     rows, cols = len(matrix), len(matrix[0])

#     if rows != cols:
#         print("Матриця не є квадратною. Головна та побічна діагоналі не визначені.")
#         return

#     main_diagonal = [matrix[i][i] for i in range(rows)]
#     anti_diagonal = [matrix[i][cols - 1 - i] for i in range(rows)]

#     print("Головна діагональ:", main_diagonal)
#     print("Побічна діагональ:", anti_diagonal)

# Приклад використання
# matrix_example = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_diagonals(matrix_example)
# matrix1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
# print(matrix1)
# identity_matrix = np.eye(4, k=-1)
# print(identity_matrix)

# identity_matrix = np.eye(4, k=1)
# print(identity_matrix)
# identity_matrix = np.eye(4, k=-1)
# print(identity_matrix)

# added_matrix = np.add(matrix1, identity_matrix)
# print(added_matrix)

# a = np.array([ [1,1], [1,1]])
# b = np.array([ [1,1], [1,1]])
# total = a.dot(b)
# print(total)

# c = np.array([[4, 6], [3, 2]])
# d = np.array([[8, 2], [3, 1]])
# total = c.dot(d)
# print(total)

# a = np.array([ [1, 0, -6], [0, 1, -6.5], [0, 0, 1] ])
# b = np.array([ [1.5, 4, 3.5], [2, 1, 5], [1, 1, 1] ])
# total = a.dot(b)
# print(total)

a = np.array([ [-2, -2], [2, -2], [2, 2], [-2, 2] ])
b = np.array([ [1, -np.tan(32)], [0, 1] ])
c = np.array([ [1, 0], [0, -1] ])
total = a.dot(c)
print(total)
print(a)

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot(total[:, 0], total[:, 1], "g")
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Line Plot')
ax.plot(a[:, 0], a[:, 1], "r")
plt.show()

