import yfinance as yf
import pandas as pd
from fredapi import Fred
import os
import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


def save_checksums(file_paths, output_path="data/metadata/checksums.txt"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write("file_path,sha256\n")
        for file_path in file_paths:
            checksum = calculate_sha256(file_path)
            f.write(f"{file_path},{checksum}\n")

    print(f"Checksums saved to {output_path}")
 
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

sp500_path = "data/raw/sp500.csv"

sp500.index.name = "Date"
sp500.to_csv(sp500_path)
print(f"S&P 500: {len(sp500):,} monthly rows saved to {sp500_path}")
 
fred = Fred(api_key=FRED_API_KEY)
cpi_path = "data/raw/cpi.csv"
cpi  = fred.get_series("CPIAUCNS", observation_start=START_DATE,
                                    observation_end=END_DATE)
cpi  = cpi.reset_index()
cpi.columns = ["Date", "CPI"]
cpi.to_csv(cpi_path, index=False)
print(f"CPI:     {len(cpi):,} rows saved to {cpi_path}")

save_checksums([
    cpi_path,
    sp500_path
])