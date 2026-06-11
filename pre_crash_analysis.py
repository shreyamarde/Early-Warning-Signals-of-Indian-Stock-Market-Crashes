import pandas as pd

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


def calculate_changes(event_date, months):

    event_date = pd.to_datetime(event_date)

    start_date = event_date - pd.DateOffset(months=months)

    start_row = df.loc[:start_date].iloc[-1]
    end_row = df.loc[event_date]

    results = {}

    for col in [
        "NIFTY",
        "INDIA_VIX",
        "USD_INR",
        "BRENT_CRUDE",
        "GOLD"
    ]:

        pct_change = (
            (end_row[col] - start_row[col])
            / start_row[col]
        ) * 100

        results[col] = round(pct_change, 2)

    return results


six_month_results = []

for event_name, event_date in events.items():

    row = calculate_changes(
        event_date,
        6
    )

    row["Event"] = event_name

    six_month_results.append(row)

six_month_df = pd.DataFrame(
    six_month_results
)

six_month_df = six_month_df.set_index(
    "Event"
)

print("\n")
print("=" * 80)
print("6 MONTH PRE-CRASH ANALYSIS")
print("=" * 80)
print(six_month_df)


three_month_results = []

for event_name, event_date in events.items():

    row = calculate_changes(
        event_date,
        3
    )

    row["Event"] = event_name

    three_month_results.append(row)

three_month_df = pd.DataFrame(
    three_month_results
)

three_month_df = three_month_df.set_index(
    "Event"
)

print("\n")
print("=" * 80)
print("3 MONTH PRE-CRASH ANALYSIS")
print("=" * 80)
print(three_month_df)


six_month_df.to_csv(
    "six_month_pre_crash.csv"
)

three_month_df.to_csv(
    "three_month_pre_crash.csv"
)

print("\nFiles Saved Successfully!")