import pandas as pd

df = pd.read_csv("data.csv")

df = df.drop_duplicates()

df = df.fillna(method='ffill')

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower().str.strip()

print(df.head())