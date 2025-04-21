import numpy as np
import math

def scale(vector, sx, sy):
    """Масштабування вектора."""
    matrix = np.array([[sx, 0], [0, sy]])
    return np.dot(matrix, vector)

def reflect_origin(vector):
    """Відображення вектора відносно початку координат."""
    matrix = np.array([[-1, 0], [0, -1]])
    return np.dot(matrix, vector)

def translate(vector, tx, ty):
    """Перенесення вектора."""
    return np.array([vector[0] + tx, vector[1] + ty])

def shear_y(vector, angle_degrees):
    """Зсув вектора по осі Y."""
    angle_radians = math.radians(angle_degrees)
    tan_theta = math.tan(angle_radians)
    matrix = np.array([[1, tan_theta], [0, 1]])
    #print(f"matrix: {matrix}")
    return np.dot(matrix, vector)

def rotate(vector, angle_degrees):
    """Поворот вектора."""
    angle_radians = math.radians(angle_degrees)
    cos_theta = math.cos(angle_radians)
    sin_theta = math.sin(angle_radians)
    matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])
#    print(f"matrix: {matrix}")
    return np.dot(matrix, vector)

# Заданий вектор
v = np.array([2, 1])  # Припустимо, початковий вектор (можете змінити)

# Крок 2.1: Змінити вектор в 2 рази по осі OX та збільшити в 3 рази по осі OY.
v1 = scale(v, 2, 3)
print(f"Після масштабування (2.1): {v1}")

# Крок 2.2: Відобразити вектор відносно початку координат.
v2 = reflect_origin(v)
print(f"Після відображення (2.2): {v2}")

# Крок 2.4: Змістити (shear) вектор на 60° по осі OY.
v4 = shear_y(v, 60)
print(f"Після зсуву по Y на 60° (2.4): {v4}")

# Крок 2.5: Повернути вектор на 30°.
v5 = rotate(v, 30)
print(f"Після повороту на 30° (2.5): {v5}")

# Крок 2.3: Перенести вектор на -3 по осі OX та на 1 по осі OY.
v3 = translate(v, -3, 1)
print(f"Після перенесення (-3, 1) (2.3): {v3}")

# Крок 2.6: Об'єднати перетворення з кроків 1, 2, 4, 5 в одну матрицю та застосувати її до початкового вектору.
# Матриця об'єднаного перетворення (M6 = M5 * M4 * M2 * M1)
angle_rad_30 = math.radians(30)
cos_30 = math.cos(angle_rad_30)
sin_30 = math.sin(angle_rad_30)
tan_60 = math.tan(math.radians(60))

M1 = np.array([[2, 0], [0, 3]])
M2 = np.array([[-1, 0], [0, -1]])
M4 = np.array([[1, tan_60], [0, 1]])
M5 = np.array([[cos_30, -sin_30], [sin_30, cos_30]])

M6 = np.dot(M5, np.dot(M4, np.dot(M2, M1)))
print(f"Об'єднана матриця (2.6):\n{M6}")
v6 = np.dot(M6, v)
print(f"Результат застосування об'єднаної матриці (2.6): {v6}")

# Застосування перенесення (крок 2.3) до результату об'єднаних лінійних перетворень
v_final = translate(v6, -3, 1)
print(f"Кінцевий результат після всіх перетворень: {v_final}")