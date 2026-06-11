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


def analyze_event(event_name, event_date):

    event_date = pd.to_datetime(event_date)

    start_date = event_date - pd.DateOffset(months=12)

    window = df.loc[start_date:event_date]

    print("\n")
    print("=" * 60)
    print(f"EVENT: {event_name}")
    print("=" * 60)


    summary = {}

    for col in [
        "NIFTY",
        "INDIA_VIX",
        "USD_INR",
        "BRENT_CRUDE",
        "GOLD"
    ]:

        first_value = window[col].iloc[0]
        last_value = window[col].iloc[-1]

        pct_change = (
            (last_value - first_value)
            / first_value
        ) * 100

        summary[col] = round(
            pct_change,
            2
        )

    summary_df = pd.DataFrame(
        summary,
        index=["% Change Before Crash"]
    )

    print(summary_df)


    fig, axs = plt.subplots(
        5,
        1,
        figsize=(14, 12),
        sharex=True
    )

    variables = [
        "NIFTY",
        "INDIA_VIX",
        "USD_INR",
        "BRENT_CRUDE",
        "GOLD"
    ]

    for i, col in enumerate(variables):

        axs[i].plot(
            window.index,
            window[col],
            linewidth=2
        )

        axs[i].axvline(
            event_date,
            linestyle="--"
        )

        axs[i].set_title(col)

        axs[i].grid(True)

    plt.suptitle(
        f"{event_name} - 12 Month Event Window",
        fontsize=16
    )

    plt.tight_layout()

    plt.show()

    return summary_df


all_results = []

for name, date in events.items():

    result = analyze_event(
        name,
        date
    )

    result.index = [name]

    all_results.append(result)


final_results = pd.concat(
    all_results
)

print("\n")
print("=" * 80)
print("FINAL EVENT COMPARISON")
print("=" * 80)

print(final_results)

final_results.to_csv(
    "event_study_results.csv"
)

print(
    "\nSaved: event_study_results.csv"
)


