import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(
    "clean_market_data.csv",
    index_col=0,
    parse_dates=True
)



events = {
    "Global Financial Crisis": "2008-10-31",
    "Eurozone Crisis": "2011-12-31",
    "Global Selloff": "2016-02-29",
    "COVID Crash": "2020-03-31"
}


# Monthly percentage changes

df["VIX_Change"] = (
    df["INDIA_VIX"].pct_change() * 100
)

df["USDINR_Change"] = (
    df["USD_INR"].pct_change() * 100
)

# Z-score normalization

df["VIX_Z"] = (
    df["VIX_Change"]
    - df["VIX_Change"].mean()
) / df["VIX_Change"].std()

df["USDINR_Z"] = (
    df["USDINR_Change"]
    - df["USDINR_Change"].mean()
) / df["USDINR_Change"].std()

# Improved Risk Score

df["Risk_Score_Z"] = (
    df["VIX_Z"]
    + df["USDINR_Z"]
)



for event_name, event_date in events.items():

    event_date = pd.to_datetime(event_date)

    start_date = event_date - pd.DateOffset(months=12)

    window = df.loc[start_date:event_date]

    plt.figure(figsize=(12,5))

    plt.plot(
        window.index,
        window["Risk_Score"],
        linewidth=2
    )

    plt.axvline(
        event_date,
        linestyle="--"
    )

    plt.title(
        f"Crash Risk Score Before {event_name}"
    )

    plt.ylabel("Risk Score")

    plt.grid(True)

    plt.show()

    print("\nTop 20 Risk Score Spikes\n")

print(
    df["Risk_Score"]
    .sort_values(ascending=False)
    .head(20)
)

risk_table = df[
    [
        "INDIA_VIX",
        "USD_INR",
        "VIX_Change",
        "USDINR_Change",
        "Risk_Score"
    ]
]

risk_table.to_csv(
    "crash_risk_score.csv"
)

print(
    "Saved: crash_risk_score.csv"
)