import sympy
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def integrate_rectangle(func, a, b, n=1000):
    #Чисельне інтегрування методом прямокутників.
    h = (b - a) / n
    integral = 0
    for i in range(n):
        midpoint = a + (i + 0.5) * h
        integral += func(midpoint) * h
    return integral

def integrate_trapezoidal(func, a, b, n=1000):
    #Чисельне інтегрування методом трапецій.
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

def integrate_simpson(func, a, b, n=1000):
    #Чисельне інтегрування методом Сімпсона.
    if n % 2 != 0:
        raise ValueError("Кількість інтервалів n повинна бути парною для методу Сімпсона.")
    h = (b - a) / n
    integral = func(a) + func(b)
    for i in range(1, n, 2):
        integral += 4 * func(a + i * h)
    for i in range(2, n - 1, 2):
        integral += 2 * func(a + i * h)
    integral *= h / 3
    return integral

# Визначаємо символьну змінну
x = sympy.Symbol('x')

# Визначаємо функцію f(x)
f_sym = 2 * (
    (4 / (1.2 * sympy.sqrt(2 * sympy.pi))) * sympy.exp(-sympy.Rational(1, 2) * ((x - 11) / 1.2)**2) +
    (7 / (2.4 * sympy.sqrt(2 * sympy.pi))) * sympy.exp(-sympy.Rational(1, 2) * ((x - 15) / 2.4)**2)
)

# 1. Візуалізація функції
x_vals = np.linspace(0, 24, 400)
f_vals_num = sympy.lambdify(x, f_sym, 'numpy')(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals_num, label='f(x) - Ефективність роботи')
plt.xlabel('Час доби (години)')
plt.ylabel('Кількість тасок за одиницю часу')
plt.title('Залежність ефективності роботи від часу доби')
plt.grid(True)
plt.legend()
plt.show()

# 2. Невизначений інтеграл
F_sym = sympy.integrate(f_sym, x)
print(f"Невизначений інтеграл f(x): {F_sym}")
# 3. Визначений інтеграл від a до b
a = 9
b = 18
integral_sym = sympy.integrate(f_sym, (x, a, b))
print(f"Визначений інтеграл f(x) від {a} до {b}: {integral_sym}")
# Обчислюємо середню кількість тасок
average_tasks_sym = integral_sym / (b - a)
print(f"Середня кількість тасок (аналітично): {average_tasks_sym}")

# Завдааня2. Перетворюємо символьну функцію в числовий формат
f_num = sympy.lambdify(x, f_sym, 'numpy')
# Рахуємо інтеграл методом прямокутників
integral_rectangle_num = integrate_rectangle(f_num, a, b)
print(f"Визначений інтеграл f(x) від {a} до {b} (метод прямокутників): {integral_rectangle_num}")
# Обчислюємо середню кількість тасок (метод прямокутників)
average_tasks_rectangle = integral_rectangle_num / (b - a)
print(f"Середня кількість тасок (метод прямокутників): {average_tasks_rectangle}")

# Завдання 3. Рахуємо інтеграл методом трапецій
integral_trapezoidal_num = integrate_trapezoidal(f_num, a, b)
print(f"Визначений інтеграл f(x) від {a} до {b} (метод трапецій): {integral_trapezoidal_num}")
# Обчислюємо середню кількість тасок (метод трапецій)
average_tasks_trapezoidal = integral_trapezoidal_num / (b - a)
print(f"Середня кількість тасок (метод трапецій): {average_tasks_trapezoidal}")

# Завдання 4. Рахуємо інтеграл методом Сімпсона
try:
    integral_simpson_num = integrate_simpson(f_num, a, b, n=1000)
    print(f"Визначений інтеграл f(x) від {a} до {b} (метод Сімпсона): {integral_simpson_num}")
    # Обчислюємо середню кількість тасок (метод Сімпсона)
    average_tasks_simpson = integral_simpson_num / (b - a)
    print(f"Середня кількість тасок (метод Сімпсона): {average_tasks_simpson}")
except ValueError as e:
    print(f"Помилка: {e}")

# Завдання 5. Рахуємо інтеграл за допомогою scipy.integrate.quad
integral_scipy, abserr = integrate.quad(f_num, a, b)
print(f"Визначений інтеграл f(x) від {a} до {b} (scipy.integrate.quad): {integral_scipy}, з абсолютною похибкою {abserr}")
# Обчислюємо середню кількість тасок (scipy.integrate.quad)
average_tasks_scipy = integral_scipy / (b - a)
print(f"Середня кількість тасок (scipy.integrate.quad): {average_tasks_scipy}") 
