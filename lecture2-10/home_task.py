import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import requests

def load_data_from_url(url):
    """
    Завантажує дані з URL, перевіряє доступність та повертає DataFrame.
    """
    try:
        # Перевірка доступності URL
        response = requests.head(url)
        response.raise_for_status()  # Перевірка на помилки HTTP
        print(f"URL '{url}' доступний. Завантаження даних...")
        # Завантаження даних
        url = url[:url.find('/edit')] + '/export?format=csv'
        df = pd.read_csv(url)
        print("Дані успішно завантажено.")
        return df
    except requests.exceptions.RequestException as e:
        print(f"Помилка при доступі до URL '{url}': {e}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Помилка: Завантажений файл з '{url}' порожній.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

def analyze_data(df):
    """
    Проводить базовий аналіз даних: інформація, статистика, типи даних, пропущені значення.
    """
    print("\nЗагальна інформація про датасет:")
    print(df.info())
    print("\nОписові статистики:")
    print(df.describe())
    print("\nТипи даних у стовпцях:")
    print(df.dtypes)
    print("\nКількість пропущених значень:")
    print(df.isnull().sum())

def handle_missing_values(df):
    """
    Обробляє пропущені значення в DataFrame: для числових стовпців - заповнення середнім,
    для категоріальних - заповнення модою.
    """
    numeric_cols = df.select_dtypes(include=["number"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    if not numeric_cols.empty:
        imputer = SimpleImputer(strategy="mean")
        df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    else:
        print("Увага: Відсутні числові стовпці для заповнення пропущених значень.")

    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def visualize_numeric_features(df):
    """
    Візуалізує розподіл числових ознак за допомогою гістограм.
    """
    numeric_cols = df.select_dtypes(include=["number"]).columns
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Розподіл {col}")
        plt.show()

def plot_correlation_matrix(df):
    """
    Будує та відображає кореляційну матрицю для числових ознак.
    """
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
        plt.title("Кореляційна матриця")
        plt.show()
    else:
        print("Увага: Відсутні числові стовпці для побудови кореляційної матриці.")

def encode_binary_features(df, binary_features):
    """
    Кодує бінарні ознаки (замінює значення на 0 та 1) за допомогою LabelEncoder.
    """
    for feature in binary_features:
        if feature in df.columns:
            df[feature] = LabelEncoder().fit_transform(df[feature])
        else:
            print(f"⚠️ Увага: Стовпець '{feature}' відсутній у датасеті! Пропускаємо.")
    return df


# Основний блок виконання
if __name__ == "__main__":
    # URL для завантаження даних
    data_url = 'https://docs.google.com/spreadsheets/d/1OPnEAT64Patnj_Ifhwn_pM1c15rsBNIoFrtz38A1_W4/edit?usp=sharing'
    # Завантаження даних
    df = load_data_from_url(data_url)
    if df is not None:
        # Аналіз даних
        analyze_data(df)
        # Обробка пропущених значень
        df = handle_missing_values(df)
        # Візуалізація числових ознак
        visualize_numeric_features(df)
        # Побудова кореляційної матриці
        plot_correlation_matrix(df)
        # Кодування бінарних ознак
        binary_features_to_encode = ["Floor", "Rent"]  # Список бінарних ознак для кодування
        df = encode_binary_features(df, binary_features_to_encode)
