import pandas as pd

df = pd.read_csv('counties.csv')
print(df)
print()
pivot_df = pd.pivot_table(df, values='Population', index=['Province'], aggfunc='sum')
print(pivot_df)
