import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Завантаження даних з MyDrive
url = 'https://docs.google.com/spreadsheets/d/1OPnEAT64Patnj_Ifhwn_pM1c15rsBNIoFrtz38A1_W4/edit?usp=sharing'
url = url[:url.find('/edit')] + '/export?format=csv'
df = pd.read_csv(url)

# Загальна інфо
print("Загальна інформація про датасет:")
print(df.info())

# Статистичні характеристики
print("Описові статистики:", df.describe())

# Типи даних
print("Типи даних у стовпцях:\n", df.dtypes)

# Пропущені значення
print("Кількість пропущених значень:\n", df.isnull().sum())

# Пропуски (числові: середнім значенням, категоріальні: найбільш популярне значення)
numeric_columns = df.select_dtypes(include=["number"]).columns
categorical_columns = df.select_dtypes(include=["object"]).columns

imputer = SimpleImputer(strategy="mean")
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

# use hint
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Числові ознаки use hint
for col in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Розподіл {col}")
    plt.show()

# Кореляція ознак - use google and hint
numeric_df = df.select_dtypes(include=["number"])
plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Кореляційна матриця \n")
plt.show()

# Заміна 0 1
binary_features = ["Floor", "Rent"]  # Тут можна вписувати ознаки я вписав ці

# use hint
for feature in binary_features:
    if feature in df.columns:
        df[feature] = LabelEncoder().fit_transform(df[feature])
    else:
        print(f"⚠️ Увага: Стовпець '{feature}' відсутній у датасеті! Пропускаємо.") # use hint