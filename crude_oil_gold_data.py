import yfinance as yf

start_date = "2000-01-01"
end_date = "2025-12-31"


brent = yf.download(
    "BZ=F",
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=False
)

brent.to_csv("brent_crude.csv")
print("Saved: brent_crude.csv")


gold = yf.download(
    "GC=F",
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=False
)

gold.to_csv("gold.csv")
print("Saved: gold.csv")

print("\nDownload completed successfully!")