import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mountains_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])
print(mountains_height)

mountains_height_name = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)
print(mountains_height_name)
print(mountains_height_name["Goverla"])
print(mountains_height > 2030)

sort_index = mountains_height_name.sort_values()
print(sort_index)

def square(x):
    return x**2

squared_height = mountains_height_name.apply(square)
print(squared_height)

other_mountains = pd.Series([2001.1, 1998.4], index=['Rebra', 'Menchul'])
all_mountains = pd.concat([mountains_height_name, other_mountains])
print(all_mountains)

all_mountains.plot(kind='bar')   

data = [[1, 'Alice'], [2, 'Bob']]
df = pd.DataFrame(data, columns=['ID', 'Name'])

data = {'ID': [1, 2], 'Name': ['Alice', 'Bob']}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.dtypes)


contacts = pd.DataFrame(
    {
        "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
        ],
        "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
        ],
        "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
        ],
        "favorite": [False, False, True, False, True],
    },
    index=[1, 2, 3, 4, 5],
)
print(contacts)

persons = pd.read_excel("test1.xlsx")
print(persons)

contacts = pd.DataFrame(
    {
        "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
        ],
        "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
        ],
        "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
        ],
        "age": [
            53,
            24,
            43,
            35,
            29,
        ],
        "favorite": [False, False, True, False, True],
    },
    index=[1, 2, 3, 4, 5],
)
contacts.to_excel('test2.xlsx', sheet_name='Contacts')
print(contacts)

employees = pd.read_json("test3.json", orient="split")
print(employees)

data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"}
}
employees = pd.DataFrame(data)
employees.to_json("test4.json", orient="split")
print(employees)

print("====================================")
value = contacts.loc[2:4, 'name':'email']
print(value)

value = contacts.iloc[2:4, 0:2]
print(value)

grouped = contacts.groupby('name')
mean_name = grouped['age'].mean()
print(mean_name)

sorted_contacts = contacts.sort_values(by='age', ascending=False)
print(sorted_contacts)

print("====================================")
cleaned_contacts = contacts.dropna()
print(cleaned_contacts)