import pandas as pd

def load_file(filename):
    df = pd.read_csv(filename, skiprows=[1])

    # Remove junk row ("Date")
    df = df[df["Price"] != "Date"]

    # Convert date column
    df["Price"] = pd.to_datetime(df["Price"])

    # Set index
    df = df.set_index("Price")

    # Convert all columns to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


nifty = load_file("nifty50.csv")
vix = load_file("indiavix.csv")
usd = load_file("usdinr.csv")
brent = load_file("brent_crude.csv")
gold = load_file("gold.csv")


nifty_monthly = nifty["Close"].resample("ME").last()
vix_monthly = vix["Close"].resample("ME").last()
usd_monthly = usd["Close"].resample("ME").last()
brent_monthly = brent["Close"].resample("ME").last()
gold_monthly = gold["Close"].resample("ME").last()


data = pd.concat(
    [
        nifty_monthly,
        vix_monthly,
        usd_monthly,
        brent_monthly,
        gold_monthly
    ],
    axis=1
)


data.columns = [
    "NIFTY",
    "INDIA_VIX",
    "USD_INR",
    "BRENT_CRUDE",
    "GOLD"
]


data.to_csv("market_data_monthly.csv")

print(data.head())
print("\nSuccess! Dataset now includes NIFTY, VIX, USD/INR, Brent, and Gold.")