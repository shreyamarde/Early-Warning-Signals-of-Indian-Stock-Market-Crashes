import yfinance as yf
import pandas as pd

start_date = "2000-01-01"
end_date = "2025-12-31"

# NIFTY 50
nifty = yf.download(
    "^NSEI",
    start=start_date,
    end=end_date,
    auto_adjust=True
)

# India VIX
vix = yf.download(
    "^INDIAVIX",
    start=start_date,
    end=end_date,
    auto_adjust=True
)

# USD/INR
usd_inr = yf.download(
    "INR=X",
    start=start_date,
    end=end_date,
    auto_adjust=True
)

# Save
nifty.to_csv("nifty50.csv")
vix.to_csv("indiavix.csv")
usd_inr.to_csv("usdinr.csv")

print("Downloaded successfully!")