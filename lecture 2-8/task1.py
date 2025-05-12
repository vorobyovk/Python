import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma, norm
import scipy.stats as stats

def stock_price_change():
    """Генерує випадкову зміну ціни акції з гамма-розподілу."""
    alpha = 0.3
    beta = 1.1
    return gamma.rvs(a=alpha, scale=1/beta)

def stock_price_at_time(t):
    """Розраховує ціну акції в момент часу t."""
    price = 0
    for _ in range(t):
        change = stock_price_change()
        price += change
    return price

def simulate_n_times(n: int, t: int):
    """Запускає симуляцію n разів для заданого часу t."""
    final_prices = [stock_price_at_time(t) for _ in range(n)]
    return final_prices

def plot_histogram_and_test_normality(data, t, num_simulations):
    """Будує гістограму розподілу та перевіряє нормальність."""
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins='auto', density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title(f'Розподіл ціни акції в момент часу t={t} ({num_simulations} симуляцій)')
    plt.xlabel('Ціна акції')
    plt.ylabel('Щільність ймовірності')

    # Перевірка на нормальність за допомогою тесту Шапіро-Уїлка
    stat, p = stats.shapiro(data)
    print(f"Час t={t}: Тест Шапіро-Уїлка - статистика={stat:.3f}, p-значення={p:.3f}")
    alpha = 0.05
    if p > alpha:
        print(f"Час t={t}: Згідно з тестом Шапіро-Уїлка, розподіл виглядає нормальним (немає достатньо доказів відхилення нульової гіпотези).")
    else:
        print(f"Час t={t}: Згідно з тестом Шапіро-Уїлка, розподіл, ймовірно, не є нормальним (є докази відхилення нульової гіпотези).")

    # Накладання кривої нормального розподілу (якщо кількість симуляцій велика)
    if num_simulations > 100:
        mu, std = norm.fit(data)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        title = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
        plt.title(title)

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_simulations = 100  # Загальна кількість симуляцій

    # a) Побудова гістограми розподілу x (зміни ціни в один момент часу)
    changes = [stock_price_change() for _ in range(num_simulations)]
    plt.figure(figsize=(8, 5))
    plt.hist(changes, bins='auto', density=True, alpha=0.6, color='skyblue', edgecolor='black')
    plt.title(f'Розподіл зміни ціни акції (n={num_simulations})')
    plt.xlabel('Зміна ціни')
    plt.ylabel('Щільність ймовірності')
    plt.grid(True)
    plt.show()

    # б) Запуск симуляції для різних значень t
    time_points = [1, 10, 30, 60]  # Приблизно до 60 з кроком, що дозволяє побачити динаміку

    for t in time_points:
        final_prices = simulate_n_times(num_simulations, t)
        plot_histogram_and_test_normality(final_prices, t, num_simulations)

    print("\nЗробіть висновки про зміну розподілу зі збільшенням t, аналізуючи отримані гістограми та результати тестів на нормальність.")