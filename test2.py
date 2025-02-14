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
