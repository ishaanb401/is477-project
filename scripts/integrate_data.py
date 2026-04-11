import os
import pandas as pd


def clean_and_integrate(
    fred_path: str = "data/raw/fred_cpi.csv",
    market_path: str = "data/raw/sp500_daily.csv",
    output_path: str = "data/processed/integrated_monthly.csv"
) -> pd.DataFrame:

    cpi = pd.read_csv(fred_path)
    market = pd.read_csv(market_path)

    cpi["date"] = pd.to_datetime(cpi["date"], errors="coerce")
    cpi["CPIAUCSL"] = pd.to_numeric(cpi["CPIAUCSL"], errors="coerce")
    cpi = cpi.dropna(subset=["date", "CPIAUCSL"]).sort_values("date")

    cpi["inflation_rate_pct"] = cpi["CPIAUCSL"].pct_change() * 100

    date_col = "Date"
    if date_col not in market.columns:
        possible = [c for c in market.columns if c.lower() == "date"]
        if possible:
            date_col = possible[0]
        else:
            raise ValueError("Could not find a Date column in market data.")

    market[date_col] = pd.to_datetime(market[date_col], errors="coerce")
    market = market.dropna(subset=[date_col]).sort_values(date_col)

    price_col = None
    for candidate in ["Adj Close", "Close"]:
        if candidate in market.columns:
            price_col = candidate
            break

    if not price_col:
        raise ValueError("Could not find Adj Close or Close column in market data.")

    market[price_col] = pd.to_numeric(market[price_col], errors="coerce")
    market = market.dropna(subset=[price_col])

    market = market[[date_col, price_col]].copy()
    market = market.rename(columns={date_col: "date", price_col: "sp500_price"})
    market = market.set_index("date").resample("M").last().reset_index()

    market["sp500_return_pct"] = market["sp500_price"].pct_change() * 100

    cpi["month"] = cpi["date"].dt.to_period("M")
    market["month"] = market["date"].dt.to_period("M")

    integrated = pd.merge(
        cpi[["month", "date", "CPIAUCSL", "inflation_rate_pct"]],
        market[["month", "sp500_price", "sp500_return_pct"]],
        on="month",
        how="inner"
    )

    integrated = integrated.rename(columns={"date": "cpi_date"})
    integrated = integrated.dropna().reset_index(drop=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    integrated.to_csv(output_path, index=False)
    print(f"Saved integrated dataset to {output_path}")

    return integrated


if __name__ == "__main__":
    clean_and_integrate()