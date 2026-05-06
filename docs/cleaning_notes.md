# Data Cleaning Notes

The CPI dataset was cleaned by converting the Date column to datetime format and converting CPI values to numeric values. Missing or invalid dates and CPI values were removed.

The S&P 500 dataset was cleaned by converting the Date column to datetime format and ensuring Open, High, Low, Close, and Volume were numeric. Daily S&P 500 data was resampled into monthly OHLCV data during acquisition.

The integrated dataset was created by converting both datasets to a monthly period and merging on that shared month field. Percent change calculations created missing values in the first row, so those rows were removed before analysis.
