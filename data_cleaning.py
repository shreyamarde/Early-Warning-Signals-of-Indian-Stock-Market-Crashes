import pandas as pd

df = pd.read_csv("market_data_monthly.csv", index_col=0, parse_dates=True)

print(df.head())

print(df.shape)

print(df.info())

print(df.describe())

print(df.isnull().sum())

missing_percent = df.isnull().sum() / len(df) * 100
print(missing_percent)

print(df.duplicated().sum())
df = df.drop_duplicates()

print(df.dtypes)

df_full = df
df_clean = df.dropna()

import matplotlib.pyplot as plt

df_clean.boxplot(column=[
    "NIFTY",
    "INDIA_VIX",
    "USD_INR",
    "BRENT_CRUDE",
    "GOLD"
])

plt.show()

df_full = df
df_clean = df.dropna()

print("Original Shape:", df.shape)
print("Clean Shape:", df_clean.shape)

print(df_clean.index.min())
print(df_clean.index.max())

quality_report = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Missing %": df.isnull().sum() / len(df) * 100,
    "Data Type": df.dtypes
})

print(quality_report)
df_clean.to_csv("clean_market_data.csv")