import pandas as pd
import matplotlib.pyplot as plt

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
temperature = pd.Series([23, 17, 17, 16, 15, 14, 17, 20], index=date)
print(temperature)

data = {
    'Місто': ['Київ', 'Львів', 'Одеса', 'Харків', None, 'Львів'],
    'Температура': [25, 32, None, 24, 23, 32],
    'Вологість': ['60%', '70%', '65%', '55%', None, '70%'],
    'Дата': ['2021-08-01', '2021-08-01', '2021-08-02', '2021-08-02', '2021-08-03', '2021-08-01']
}
df = pd.DataFrame(data)
df.drop_duplicates(subset=['Місто', 'Дата'], inplace=True)
df.dropna(subset=['Місто'], inplace=True)
df['Вологість'] = df['Вологість'].str.rstrip('%').astype(float)/100
df.plot(kind='bar', x='Місто', y='Температура')
plt.show() #you can if see or save

print("=============================================")
data1 = {
    "name": {"1": "Michael", "2": "John"},
    "country": {"1": "Canada", "2": "USA"},
    "age": {"1": 25, "2": 32}
}
employees1 = pd.DataFrame(data1)
data2 = {
    "name": {"3": "Liza", "4": "Jhon"},
    "country": {"3": "Australia", "4": "Denmark"},
    "age": {"3": 19, "4": 23}
}
employees2 = pd.DataFrame(data2)
employees = pd.concat([employees1, employees2])
print(employees)

print("=============================================")
data1 = {
    "name": ["Michael", "John"],
    "country": ["Canada", "USA"],
}
data2 = {
    "name": ["Michael", "Liza"],
    "age": [25, 19]
}
employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)
merged = pd.merge(employees1, employees2, on='name', how='outer')
print(merged)

print("=============================================")
data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура C': [25, 28, 24]
}
weather_df = pd.DataFrame(data)
print(weather_df)
weather_df['Температура F'] = weather_df['Температура C'].apply(lambda temp: (temp * 9/5) + 32)
print(weather_df)

