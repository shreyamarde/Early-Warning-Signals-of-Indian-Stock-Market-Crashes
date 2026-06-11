import pandas as pd

# Load data and keep dates as index
df_clean = pd.read_csv(
    "clean_market_data.csv",
    index_col=0,
    parse_dates=True
)

# Calculate drawdown
rolling_max = df_clean["NIFTY"].cummax()

df_clean["Drawdown"] = (
    (df_clean["NIFTY"] - rolling_max)
    / rolling_max
) * 100

# Show 20 worst drawdowns with dates
worst_drawdowns = (
    df_clean[["NIFTY", "Drawdown"]]
    .sort_values("Drawdown")
    .head(20)
)

print(worst_drawdowns)