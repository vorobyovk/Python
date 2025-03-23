import pandas as pd
import matplotlib.pyplot as plt

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Maria', 'Petro', 'Sophia', 'Max', 'Natalia', 'Vadym'],
    'Вік': [21, 22, 20, 19, 23, 22, 21, 20, 19, 21],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)
print(students_df)

older_students = students_df[students_df['Вік'] > 20]
print(older_students)

students_df.to_csv('students.csv', index=False)

file_path = 'students.csv'
data_df = pd.read_csv(file_path)
print(data_df.head())

print("Shape of the DataFrame:", data_df.shape)
print(data_df.describe())
data_df.info()

students_df['Вік'].plot(kind='hist', title='Вікова група студентів')
plt.show() #you can if see or save
#plt.savefig('students_age.pdf',bbox_inches='tight')

