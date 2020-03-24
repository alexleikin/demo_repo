import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fruits.csv')

tbl = df.groupby(['Fruit', 'Name'], as_index=False).sum().pivot('Fruit', 'Name', 'Number').fillna(0)

print(tbl)

tbl.head(20).plot(kind='bar', figsize=(10, 5))
plt.title('Fruits By Name')
plt.ylabel('Consumed Fruits by Person')
plt.xlabel('Number of Fruits')


plt.show()
print(df)
# print(df.head(5))
print("hello")
