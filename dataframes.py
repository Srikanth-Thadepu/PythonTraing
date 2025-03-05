import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
print(df)

# print(df[df["Age"]>30])

df_sorted=df.sort_values(by="Age")
print(df_sorted)

print(df.groupby("City").count())

print(df.fillna("Unknown"))

print(df[df.index==1])