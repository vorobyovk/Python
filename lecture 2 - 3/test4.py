import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Створення векторів для координат осей
axis_x = np.array([1, 0])
axis_y = np.array([0, 1])


# Побудова системи координат і векторів
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, axis_x[0], axis_x[1], angles='xy', scale_units='xy', scale=1, color='r', label='Вісь X')
plt.quiver(0, 0, axis_y[0], axis_y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Вісь Y')


# Позначення початку координат
plt.scatter(0, 0, color='black', marker='o')


# Додавання підписів
plt.text(axis_x[0], axis_x[1], ' X', fontsize=12, color='r', va='bottom', ha='left')
plt.text(axis_y[0], axis_y[1], ' Y', fontsize=12, color='b', va='bottom', ha='left')


# Налаштування вигляду графіка
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Система координат з одиничними векторами')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()
plt.show()




# Створення ортонормованого базису
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])


# Створення 3D-графіка
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


# Додавання векторів до графіка
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='Вектор 1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', label='Вектор 2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='Вектор 3')


# Налаштування вигляду графіка
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_zlabel('Вісь Z')
ax.set_title('Ортонормований базис у 3D')
ax.legend()


# Відображення графіка
plt.show()

# Створення двох колінеарних векторів
vector_a = np.array([2, 3])
vector_b = 2 * vector_a


# Побудова системи координат і векторів
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, vector_a[0], vector_a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Вектор A')
plt.quiver(0, 1, vector_b[0], vector_b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Вектор B')


# Позначення початку координат
plt.scatter(0, 0, color='black', marker='o')


# Додавання підписів
plt.text(vector_a[0], vector_a[1], ' A', fontsize=12, color='r', va='bottom', ha='left')
plt.text(vector_b[0], vector_b[1], ' B', fontsize=12, color='b', va='bottom', ha='left')


# Налаштування вигляду графіка
plt.xlim(-1, 7)
plt.ylim(-1, 9)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Колінеарні вектори на площині')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()
plt.show()