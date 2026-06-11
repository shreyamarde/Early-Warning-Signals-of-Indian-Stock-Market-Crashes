import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt



# Load dataset correctly
df = pd.read_csv(
    "market_data_monthly.csv",
    index_col=0,
    parse_dates=True
)

# Visualize missing data
msno.matrix(df)

plt.show()