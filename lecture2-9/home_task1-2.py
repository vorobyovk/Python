import numpy as np

def simplex(c, A, b):
    m, n = len(A), len(c)
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:-1, :n] = A
    tableau[:-1, n:n + m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -np.array(c)
    basic_vars = list(range(n, n + m))
    while True:
        # Крок 1: Вибір розв'язувального стовпця (найбільш від'ємний в останньому рядку)
        pivot_col_index = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col_index] >= 0:
            break  # Оптимум знайдено
        # Крок 2: Вибір розв'язувального рядка (найменше додатне відношення b_i / a_ij)
        positive_ratios = []
        for i in range(m):
            if tableau[i, pivot_col_index] > 0:
                positive_ratios.append(tableau[i, -1] / tableau[i, pivot_col_index])
            else:
                positive_ratios.append(np.inf)

        pivot_row_index = np.argmin(positive_ratios)
        if positive_ratios[pivot_row_index] == np.inf:
            return None, None  # Задача необмежена
        pivot_row_original_index = pivot_row_index
        # Крок 3: Оновлення табло за допомогою елементарних перетворень рядків
        pivot_value = tableau[pivot_row_index, pivot_col_index]
        tableau[pivot_row_index, :] /= pivot_value
        for i in range(m + 1):
            if i != pivot_row_index:
                factor = tableau[i, pivot_col_index]
                tableau[i, :] -= factor * tableau[pivot_row_index, :]
        # Оновлення базисних змінних
        basic_vars[pivot_row_original_index] = pivot_col_index
    # Вилучення оптимального розв'язку та значення цільової функції
    optimal_solution = np.zeros(n)
    for i, var_index in enumerate(basic_vars):
        if var_index < n:
            optimal_solution[var_index] = tableau[i, -1]
    max_objective_value = -tableau[-1, -1]
    return optimal_solution, max_objective_value
# Приклад використання:
c = [2, 9, 6]  # Коефіцієнти цільової функції
A = [[12, 6, 2],  # Коефіцієнти обмежень
     [12, 24, 18],
     [12, 18, 12]]
b = [320, 384, 180]  # Праві частини обмежень
optimal_solution, max_profit = simplex(c, A, b)
if optimal_solution is not None:
    print("Оптимальний розв'язок:")
    print(f"Кількість сайтів (x1): {optimal_solution[0]:.2f}")
    print(f"Кількість інтернет-магазинів (x2): {optimal_solution[1]:.2f}")
    print(f"Кількість інтеграцій з ERP (x3): {optimal_solution[2]:.2f}")
    print(f"Максимальний місячний прибуток: {max_profit:.2f} тис. $")
else:
    print("Задача не має розв'язку або необмежена.")