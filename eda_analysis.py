import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_clean = pd.read_csv(
    "clean_market_data.csv",
    index_col=0,
    parse_dates=True
)

plt.figure(figsize=(12,6))
plt.plot(df_clean.index, df_clean["NIFTY"])
plt.title("NIFTY 50 Over Time")
plt.xlabel("Year")
plt.ylabel("NIFTY")
plt.grid(True)
plt.show()

df_clean[[
    "NIFTY",
    "INDIA_VIX",
    "USD_INR",
    "BRENT_CRUDE",
    "GOLD"
]].plot(subplots=True, figsize=(12,10))

plt.show()

df_clean.hist(figsize=(12,8), bins=20)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))

sns.heatmap(
    df_clean.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()

df_clean["NIFTY_Return"] = df_clean["NIFTY"].pct_change() * 100
plt.figure(figsize=(12,6))

plt.plot(df_clean.index, df_clean["NIFTY_Return"])
plt.axhline(0, linestyle="--")

plt.title("Monthly NIFTY Returns")
plt.show()

worst_months = df_clean["NIFTY_Return"].sort_values().head(15)

print(worst_months)

rolling_max = df_clean["NIFTY"].cummax()

drawdown = (df_clean["NIFTY"] - rolling_max) / rolling_max * 100

df_clean["Drawdown"] = drawdown

plt.figure(figsize=(12,6))

plt.plot(df_clean.index, df_clean["Drawdown"])
plt.title("NIFTY Drawdowns")
plt.ylabel("% Drawdown")
plt.show()

returns = df_clean.pct_change() * 100

returns = returns.dropna()

plt.figure(figsize=(8,6))

sns.heatmap(
    returns.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation of Monthly Returns")

plt.show()