import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, kstest, norm

# Завантаження даних
url = 'https://docs.google.com/spreadsheets/d/18WCpPS96Tb3cB0FCsIA92PEhcmBkp08sjYhS9DsQfJE/export?format=csv'
df = pd.read_csv(url)

# Виконуємо аналіз для всіх колонок
columns_to_analyze = df.columns

# Функція для перевірки на нормальність
def test_normality(data, column_name):
    alpha = 0.05
    print(f"\n--- Перевірка на нормальність для колонки '{column_name}' ---")

    # Тест Шапіро-Уїлка (добре працює для невеликих та середніх розмірів вибірки)
    if len(data) >= 3 and len(data) <= 5000:
        stat_shapiro, p_shapiro = shapiro(data)
        print(f"Тест Шапіро-Уїлка: статистика={stat_shapiro:.3f}, p={p_shapiro:.3f}")
        if p_shapiro > alpha:
            print(f"Дані з колонки '{column_name}', ймовірно, мають нормальний розподіл (p > {alpha}).")
        else:
            print(f"Дані з колонки '{column_name}', ймовірно, не мають нормального розподілу (p <= {alpha}).")
    else:
        print("Тест Шапіро-Уїлка не застосовується для цієї кількості даних.")

    # Тест Колмогорова-Смирнова (загальний тест, але менш потужний для малих вибірок)
    if len(data) > 0:
        mean = np.mean(data)
        std = np.std(data)
        stat_ks, p_ks = kstest((data - mean) / std, 'norm')
        print(f"Тест Колмогорова-Смирнова: статистика={stat_ks:.3f}, p={p_ks:.3f}")
        if p_ks > alpha:
            print(f"Згідно з тестом Колмогорова-Смирнова, розподіл схожий на нормальний (p > {alpha}).")
        else:
            print(f"Згідно з тестом Колмогорова-Смирнова, розподіл відрізняється від нормального (p <= {alpha}).")
    else:
        print("Недостатньо даних для тесту Колмогорова-Смирнова.")

# Аналіз кожної колонки
for column in columns_to_analyze:
    data = df[column].dropna()  # Видаляємо NaN значення для розрахунків

    if not data.empty:
        mean_val = np.mean(data)
        variance_val = np.var(data)
        std_dev_val = np.std(data)
        # Обчислення кореляції тільки якщо є інші числові стовпці для порівняння
        if len(df.select_dtypes(include=np.number).columns) > 1 and column != 'Product_Sold':
            correlation_val = df[column].corr(df['Product_Sold'])
        else:
            correlation_val = None

        print(f"\n--- Аналіз колонки '{column}' ---")
        print(f"Середнє значення: {mean_val:.2f}")
        print(f"Дисперсія: {variance_val:.2f}")
        print(f"Стандартне відхилення: {std_dev_val:.2f}")

        if correlation_val is not None:
            print(f"Кореляція з 'Product_Sold': {correlation_val:.2f}")
        # Побудова гістограми
        plt.figure(figsize=(8, 6))
        plt.hist(data, bins='auto', edgecolor='black')
        plt.title(f'Гістограма розподілу для колонки "{column}"')
        plt.xlabel(column)
        plt.ylabel('Частота')
        plt.grid(True)
        plt.show()

        # Перевірка на нормальність
        test_normality(data, column)
    else:
        print(f"\n--- Колонка '{column}' порожня або містить лише NaN значення. Аналіз неможливий. ---")