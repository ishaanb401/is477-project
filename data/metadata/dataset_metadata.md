```md
# Dataset Metadata

## Dataset 1: FRED CPI Data

- **Source:** Federal Reserve Economic Data (FRED)
- **Series ID:** CPIAUCSL
- **Description:** Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
- **Access method:** FRED API
- **Format:** JSON converted to CSV
- **Temporal coverage:** Depends on API response
- **Unit:** Index 1982-1984=100
- **Use in project:** Used to calculate monthly inflation rate

## Dataset 2: Yahoo Finance S&P 500 Data

- **Source:** Yahoo Finance
- **Ticker:** ^GSPC
- **Description:** Historical daily prices for the S&P 500 index
- **Access method:** Python yfinance library
- **Format:** CSV
- **Temporal coverage:** Configurable in script
- **Unit:** USD
- **Use in project:** Used to calculate monthly market returns

## Integration Key

- **Shared variable:** Date / month period

## Notes on Processing

- Daily stock data is resampled to month-end values
- CPI data is already monthly
- Monthly percent change is computed for both CPI and stock prices
```
