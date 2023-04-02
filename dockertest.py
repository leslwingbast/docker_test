import pandas as pd

df = pd.read_csv('counties.csv')
print(df.info)
pivot_df = pd.pivot_table(df, values='Population', index=['Province'], aggfunc='sum')
print(pivot_df.info)
