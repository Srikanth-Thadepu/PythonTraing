import pandas as pd

data={'Sales': [100, 150, 200, 120, 180],
    'Region': ['North', 'North', 'South', 'South', 'North'],
    'State': ['CA', 'NY', 'TX', 'FL', 'CA'],
    'Year': [2022, 2022, 2022, 2022, 2023]
    }

df=pd.DataFrame(data)
df.set_index(["Region","State","Year"],inplace=True)
print(df)