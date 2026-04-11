import yfinance as yf
import pandas as pd
from fredapi import Fred
import os
 
FRED_API_KEY = os.getenv("FRED_API_KEY")
START_DATE   = "2000-01-01"
END_DATE     = "2024-12-31"
 
sp500_daily = yf.download("^GSPC", start=START_DATE, end=END_DATE,
                           auto_adjust=True, progress=False)
sp500_daily.columns = sp500_daily.columns.get_level_values(0)
sp500 = sp500_daily.resample("M").agg({
    "Open":   "first",
    "High":   "max",
    "Low":    "min",
    "Close":  "last",
    "Volume": "sum",
})
sp500.index.name = "Date"
sp500.to_csv("data/raw/sp500.csv")
print(f"S&P 500: {len(sp500):,} monthly rows saved to data/raw/sp500.csv")
 
fred = Fred(api_key=FRED_API_KEY)
cpi  = fred.get_series("CPIAUCNS", observation_start=START_DATE,
                                    observation_end=END_DATE)
cpi  = cpi.reset_index()
cpi.columns = ["Date", "CPI"]
cpi.to_csv("data/raw/cpi.csv", index=False)
print(f"CPI:     {len(cpi):,} rows saved to data/raw/cpi.csv")