import os
import pandas as pd


def clean_and_integrate(
    cpi_path: str = "data/raw/cpi.csv",
    sp500_path: str = "data/raw/sp500.csv",
    output_path: str = "data/processed/integrated_monthly.csv"
) -> pd.DataFrame:

    cpi = pd.read_csv(cpi_path)
    cpi["Date"] = pd.to_datetime(cpi["Date"], errors="coerce")
    cpi["CPI"] = pd.to_numeric(cpi["CPI"], errors="coerce")
    cpi = cpi.dropna(subset=["Date", "CPI"]).sort_values("Date")

    cpi["inflation_rate_pct"] = cpi["CPI"].pct_change() * 100
    cpi["month"] = cpi["Date"].dt.to_period("M")

    sp500 = pd.read_csv(sp500_path)
    sp500["Date"] = pd.to_datetime(sp500["Date"], errors="coerce")

    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
    for col in numeric_cols:
        if col in sp500.columns:
            sp500[col] = pd.to_numeric(sp500[col], errors="coerce")

    sp500 = sp500.dropna(subset=["Date", "Close"]).sort_values("Date")

    sp500["sp500_return_pct"] = sp500["Close"].pct_change() * 100
    sp500["month"] = sp500["Date"].dt.to_period("M")

    integrated = pd.merge(
        cpi[["month", "Date", "CPI", "inflation_rate_pct"]],
        sp500[["month", "Open", "High", "Low", "Close", "Volume", "sp500_return_pct"]],
        on="month",
        how="inner"
    )

    integrated = integrated.rename(columns={"Date": "cpi_date"})
    integrated = integrated.dropna().reset_index(drop=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    integrated.to_csv(output_path, index=False)
    print(f"Integrated dataset saved to {output_path}")

    return integrated


if __name__ == "__main__":
    clean_and_integrate()