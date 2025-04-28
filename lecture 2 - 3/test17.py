import plotly.graph_objects as go
import numpy as np

def dot_product(vector1_start, vector1_end, vector2_start, vector2_end):
    # Обчислюємо вектори
    vector1 = np.array(vector1_end) - np.array(vector1_start)
    vector2 = np.array(vector2_end) - np.array(vector2_start)
    # Обчислюємо скалярний добуток
    scalar_product = np.dot(vector1, vector2)
    return scalar_product

# Задаємо координати векторів
vector1_start = [1, 2]
vector1_end = [4, 6]
vector2_start = [3, 1]
vector2_end = [6, 3]
print(dot_product(vector1_start, vector1_end, vector2_start, vector2_end))

def calculate_cosine_angle(vector1, vector2):
    """
    Функція для визначення косинусного кута між двома векторами.
    Параметри:
    - vector1: Кортеж (x1, y1) з координатами кінця першого вектора.
    - vector2: Кортеж (x2, y2) з координатами кінця другого вектора.
    Повертає:
    - cosine_angle: Косинус кута між векторами.
    """
    dot_product = np.dot(vector1, vector2)
    magnitude_vector1 = np.linalg.norm(vector1)
    magnitude_vector2 = np.linalg.norm(vector2)
    cosine_angle = dot_product / (magnitude_vector1 * magnitude_vector2)
    return cosine_angle

# Приклад використання функції з двома векторами
vector1 = (3, 4)
vector2 = (1, 2)
cosine_angle = calculate_cosine_angle(vector1, vector2)
angle_degrees = np.degrees(np.arccos(cosine_angle))
print(f"Косинусний кут між векторами: {cosine_angle:.2f}")
print(f"Кут між векторами у градусах: {angle_degrees:.2f}")
