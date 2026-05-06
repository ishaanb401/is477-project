# Data Dictionary

## Project

**Title:** Inflation and Stock Market Performance in the United States

This data dictionary describes the structure and meaning of the main datasets used in the project. The project combines Consumer Price Index data from FRED with S&P 500 historical market data from Yahoo Finance to study the relationship between inflation and stock market returns.

---

## Dataset 1: `data/raw/cpi.csv`

### Description

This dataset contains monthly Consumer Price Index values from the Federal Reserve Economic Data (FRED) API. CPI is used to calculate the monthly inflation rate.

### Columns

| Column | Data Type | Description                               | Example      |
| ------ | --------- | ----------------------------------------- | ------------ |
| `Date` | Date      | Date of the CPI observation               | `2000-01-01` |
| `CPI`  | Float     | Consumer Price Index value for that month | `168.8`      |

### Notes

- Source: FRED API
- Series ID: `CPIAUCNS`
- Frequency: Monthly
- CPI is reported as an index value, not a percent.
- Monthly inflation is calculated later using percent change in CPI.

---

## Dataset 2: `data/raw/sp500.csv`

### Description

This dataset contains monthly S&P 500 market data collected from Yahoo Finance using the `yfinance` Python library. The original daily market data is resampled to monthly values during acquisition.

### Columns

| Column   | Data Type | Description                                         | Example       |
| -------- | --------- | --------------------------------------------------- | ------------- |
| `Date`   | Date      | Month-end date for the S&P 500 observation          | `2000-01-31`  |
| `Open`   | Float     | First opening price of the S&P 500 during the month | `1469.25`     |
| `High`   | Float     | Highest S&P 500 price during the month              | `1478.00`     |
| `Low`    | Float     | Lowest S&P 500 price during the month               | `1350.14`     |
| `Close`  | Float     | Last closing price of the S&P 500 during the month  | `1394.46`     |
| `Volume` | Integer   | Total reported trading volume for the month         | `21494400000` |

### Notes

- Source: Yahoo Finance through `yfinance`
- Ticker: `^GSPC`
- Original frequency: Daily
- Stored frequency: Monthly
- Monthly stock returns are calculated later using percent change in the `Close` column.

---

## Dataset 3: `data/processed/integrated_monthly.csv`

### Description

This is the final integrated dataset used for analysis. It combines CPI data and S&P 500 data at the monthly level. The datasets are merged using a shared month variable.

### Columns

| Column               | Data Type       | Description                                     | Example       |
| -------------------- | --------------- | ----------------------------------------------- | ------------- |
| `month`              | String / Period | Month used as the integration key               | `2000-02`     |
| `cpi_date`           | Date            | Original CPI observation date                   | `2000-02-01`  |
| `CPI`                | Float           | Consumer Price Index value for the month        | `169.8`       |
| `inflation_rate_pct` | Float           | Monthly percent change in CPI                   | `0.5924`      |
| `Open`               | Float           | First S&P 500 opening price during the month    | `1394.46`     |
| `High`               | Float           | Highest S&P 500 price during the month          | `1444.55`     |
| `Low`                | Float           | Lowest S&P 500 price during the month           | `1325.07`     |
| `Close`              | Float           | Last S&P 500 closing price during the month     | `1366.42`     |
| `Volume`             | Integer         | Total S&P 500 trading volume during the month   | `20912000000` |
| `sp500_return_pct`   | Float           | Monthly percent change in S&P 500 closing price | `-2.0105`     |

---

## Derived Variables

### `inflation_rate_pct`

This variable is calculated from the CPI column:

```text
inflation_rate_pct = monthly percent change in CPI
```
