from scipy.optimize import linprog

# Коэффіцієнти цільової функциї
c = [-2, -9, -6]

# Матриця коэффіцієнтів обмежень
A = [[12, 6, 2],
     [12, 24, 18],
     [12, 18, 12]]

# Вектор правих частин обмежень
b = [320, 384, 180]

# Границы переменных 
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)
bounds = [x_bounds, y_bounds, z_bounds]

# Рішення задачі лінійного программування
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Вивід результатів
if res.success:
    optimal_sites = res.x[0]
    optimal_magazines = res.x[1]
    optimal_erp = res.x[2]
    max_profit = -res.fun  # Змінюємо знак, оскільки ми мінімізуємо цільову функцію 
    print(f"Оптимальна кількість сайтів: {optimal_sites:.2f}")
    print(f"Оптимальна колькість інтернет-магазинів: {optimal_magazines:.2f}")
    print(f"Оптимальна кількість інтеграцій з ERP: {optimal_erp:.2f}")
    print(f"Максимальний місячний прибуток: {max_profit:.2f} тыс. $")
else:
    print(f"Задача оптимизації не має рішення: {res.message}")