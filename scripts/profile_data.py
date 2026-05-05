import os
import textwrap
import pandas as pd
import numpy as np

REPORT_PATH = "outputs/reports/data_quality_report.txt"
EXPECTED_START = pd.Period("2000-01", freq="M")
EXPECTED_END   = pd.Period("2024-12", freq="M")


def _header(title: str) -> str:
    bar = "=" * 60
    return f"\n{bar}\n {title}\n{bar}\n"


def _subheader(title: str) -> str:
    return f"\n--- {title} ---\n"


def profile_basic(df: pd.DataFrame, name: str) -> str:
    out = _header(f"DATASET: {name}")
    out += f"Shape         : {df.shape[0]:,} rows x {df.shape[1]} columns\n"
    out += f"Columns       : {list(df.columns)}\n"
    out += f"Memory usage  : {df.memory_usage(deep=True).sum() / 1024:.1f} KB\n"
    out += "\nColumn dtypes:\n"
    for col, dtype in df.dtypes.items():
        out += f"  {col:<25} {dtype}\n"
    return out


def profile_missing(df: pd.DataFrame) -> str:
    out = _subheader("Missing Values")
    missing = df.isnull().sum()
    pct     = (missing / len(df) * 100).round(2)
    if missing.sum() == 0:
        out += "  No missing values found.\n"
    else:
        for col in missing[missing > 0].index:
            out += f"  {col:<25} {missing[col]:>5} missing  ({pct[col]:.2f}%)\n"
    return out


def profile_duplicates(df: pd.DataFrame) -> str:
    out = _subheader("Duplicate Rows")
    n = df.duplicated().sum()
    out += f"  {n} duplicate row(s) found.\n"
    return out


def profile_stats(df: pd.DataFrame) -> str:
    out = _subheader("Descriptive Statistics (numeric columns)")
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        out += "  No numeric columns.\n"
        return out
    stats = numeric.describe().T
    stats["cv_%"] = (stats["std"] / stats["mean"].abs() * 100).round(2)
    out += stats.to_string() + "\n"
    return out


def profile_date_continuity(df: pd.DataFrame, date_col: str, name: str) -> str:
    out = _subheader(f"Date Continuity ({date_col})")
    dates = pd.to_datetime(df[date_col], errors="coerce")
    periods = dates.dt.to_period("M").sort_values()
    full_range = pd.period_range(EXPECTED_START, EXPECTED_END, freq="M")

    out += f"  Observed range : {periods.iloc[0]}  →  {periods.iloc[-1]}\n"
    out += f"  Expected range : {EXPECTED_START}  →  {EXPECTED_END}\n"
    out += f"  Expected months: {len(full_range)}\n"
    out += f"  Present months : {periods.nunique()}\n"

    missing_months = full_range.difference(periods.unique())
    if len(missing_months) == 0:
        out += "  No gaps detected in monthly sequence.\n"
    else:
        out += f"  GAPS ({len(missing_months)}):\n"
        for m in missing_months:
            out += f"    {m}\n"
    return out


def data_quality_assessment():
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    report = ""
    report += "DATA QUALITY REPORT\n"

    #CPI
    cpi = pd.read_csv("data/raw/cpi.csv")
    report += profile_basic(cpi, "CPI (data/raw/cpi.csv)")
    report += profile_missing(cpi)
    report += profile_duplicates(cpi)
    report += profile_date_continuity(cpi, "Date", "CPI")
    report += profile_stats(cpi)

    #S&P 500
    sp500 = pd.read_csv("data/raw/sp500.csv")
    report += profile_basic(sp500, "S&P 500 (data/raw/sp500.csv)")
    report += profile_missing(sp500)
    report += profile_duplicates(sp500)
    report += profile_date_continuity(sp500, "Date", "S&P 500")
    report += profile_stats(sp500)

    #Integrated Dataset
    integrated = pd.read_csv("data/processed/integrated_monthly.csv")
    report += profile_basic(integrated, "Integrated Monthly (data/processed/integrated_monthly.csv)")
    report += profile_missing(integrated)
    report += profile_duplicates(integrated)
    report += profile_stats(integrated)

    with open(REPORT_PATH, "w") as f:
        f.write(report)

    print(report)
    print(f"\nReport saved to {REPORT_PATH}")


if __name__ == "__main__":
    data_quality_assessment()
