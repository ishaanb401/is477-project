import os
import pandas as pd
import matplotlib.pyplot as plt

from fetch_fred_data import fetch_fred_series
from fetch_market_data import fetch_sp500_data
from integrate_data import clean_and_integrate


def generate_summary(df: pd.DataFrame, output_dir: str = "outputs") -> None:
    os.makedirs(f"{output_dir}/figures", exist_ok=True)
    os.makedirs(f"{output_dir}/tables", exist_ok=True)

    corr = df[["inflation_rate_pct", "sp500_return_pct"]].corr()
    corr.to_csv(f"{output_dir}/tables/correlation_matrix.csv")
    print("Saved correlation matrix.")

    summary = df[["inflation_rate_pct", "sp500_return_pct"]].describe()
    summary.to_csv(f"{output_dir}/tables/summary_statistics.csv")
    print("Saved summary statistics.")

    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(df["cpi_date"]), df["inflation_rate_pct"])
    plt.title("Monthly Inflation Rate")
    plt.xlabel("Date")
    plt.ylabel("Percent")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/figures/inflation_rate.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(df["cpi_date"]), df["sp500_return_pct"])
    plt.title("Monthly S&P 500 Returns")
    plt.xlabel("Date")
    plt.ylabel("Percent")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/figures/sp500_returns.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(df["inflation_rate_pct"], df["sp500_return_pct"])
    plt.title("Inflation vs S&P 500 Monthly Returns")
    plt.xlabel("Inflation Rate (%)")
    plt.ylabel("S&P 500 Return (%)")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/figures/inflation_vs_returns_scatter.png")
    plt.close()

    print("Saved figures.")


def main() -> None:
    fetch_fred_series("CPIAUCSL", "data/raw/fred_cpi.csv")
    fetch_sp500_data(output_path="data/raw/sp500_daily.csv")
    integrated = clean_and_integrate(
        fred_path="data/raw/fred_cpi.csv",
        market_path="data/raw/sp500_daily.csv",
        output_path="data/processed/integrated_monthly.csv"
    )
    generate_summary(integrated)


if __name__ == "__main__":
    main()