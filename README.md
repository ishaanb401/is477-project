# Inflation and Stock Market Performance in the United States

## Contributors

- Ishaan Bhargava
- Aamir Abjani

---

## Summary

This project examines the relationship between inflation and stock market performance in the United States from 2000 through 2024. The main goal of the project is to understand whether changes in inflation are associated with changes in monthly S&P 500 returns. Inflation is an important macroeconomic indicator because it affects purchasing power, interest rates, investor expectations, and overall financial market behavior. When inflation rises, investors may become concerned about future Federal Reserve policy, higher borrowing costs, and lower corporate profitability. Because of this, inflation can potentially influence stock market returns and volatility.

The main research question for this project is: **How are monthly changes in inflation related to monthly S&P 500 returns in the United States?** A related question is whether there is a visible pattern between inflation and market performance over time. This project does not attempt to prove that inflation directly causes stock market movements, but it does explore whether a relationship exists between the two variables.

To answer this question, the project integrates two datasets from trustworthy financial and economic data sources. The first dataset is Consumer Price Index data from Federal Reserve Economic Data, also known as FRED. CPI is used as a measure of inflation. The second dataset is historical S&P 500 market data collected from Yahoo Finance through the `yfinance` Python library. These datasets are useful together because they both include time-based observations and can be joined by month.

The project follows a complete data workflow. First, the data is acquired programmatically using a Python script. The FRED API is used to collect CPI data, while `yfinance` is used to collect S&P 500 historical data. The raw files are saved in the repository under `data/raw/`. Next, the datasets are cleaned and standardized. CPI data is already monthly, while S&P 500 data is collected daily and then resampled into monthly values. Monthly inflation rates are calculated using percent change in CPI, and monthly S&P 500 returns are calculated using percent change in the S&P 500 closing price.

After cleaning, the datasets are integrated into one monthly dataset saved as `data/processed/integrated_monthly.csv`. The final dataset is then used to calculate summary statistics, a correlation matrix, and visualizations. The main outputs include line charts showing inflation and S&P 500 returns over time, along with a scatter plot comparing monthly inflation rates and monthly market returns.

Based on the preliminary analysis, the relationship between monthly inflation and monthly S&P 500 returns appears to be relatively weak. The scatter plot does not show a clear linear pattern, suggesting that inflation alone does not explain short-term stock market returns. This makes sense because the stock market is affected by many other factors, including interest rates, corporate earnings, investor sentiment, unemployment, monetary policy, and global events. However, the project still demonstrates how macroeconomic and financial datasets can be integrated and analyzed to explore a real-world economic question.

---

## Data Profile

This project uses two main datasets: CPI data from FRED and S&P 500 market data from Yahoo Finance. Both datasets are time-series datasets and are integrated using a shared monthly date field.

### Dataset 1: FRED CPI Data

The first dataset is Consumer Price Index data collected from Federal Reserve Economic Data. The CPI series used in this project is `CPIAUCNS`, which represents the Consumer Price Index for All Urban Consumers. CPI is commonly used as a measure of inflation because it tracks changes in the prices paid by consumers for goods and services.

The CPI dataset is stored in the repository at:

`data/raw/cpi.csv`

The structure of the dataset is simple and tabular. It contains two main columns:

- `Date`: the date of the CPI observation
- `CPI`: the Consumer Price Index value for that month

The CPI dataset is monthly, which makes it suitable for analyzing inflation trends over time. The values are index values, not percentages. Because of this, the project calculates a derived variable called `inflation_rate_pct`, which measures the monthly percent change in CPI.

This dataset relates directly to the research question because it provides the inflation measure used in the analysis. Without the CPI data, the project would not have a way to measure inflation over time.

### Dataset 2: Yahoo Finance S&P 500 Data

The second dataset is historical S&P 500 data collected from Yahoo Finance using the `yfinance` Python library. The ticker used is `^GSPC`, which represents the S&P 500 index. The S&P 500 is a major stock market index that tracks the performance of large publicly traded U.S. companies, making it a useful measure of overall U.S. stock market performance.

The raw S&P 500 dataset is stored in the repository at:

`data/raw/sp500.csv`

The dataset includes monthly market information. The original data is downloaded at a daily frequency and then resampled into monthly values. The columns include:

- `Date`: the month-end date
- `Open`: the first opening value of the month
- `High`: the highest value during the month
- `Low`: the lowest value during the month
- `Close`: the final closing value of the month
- `Volume`: total monthly trading volume

The most important column for this project is `Close`, because it is used to calculate monthly S&P 500 returns. A derived variable called `sp500_return_pct` is calculated as the monthly percent change in the closing value.

This dataset relates to the research question because it provides the stock market performance measure used in the analysis.

### Integrated Dataset

The final integrated dataset is stored at:

`data/processed/integrated_monthly.csv`

This dataset combines the CPI and S&P 500 datasets by month. It includes CPI values, monthly inflation rates, S&P 500 monthly market values, and monthly S&P 500 returns.

The two datasets are integrated using a shared monthly time period. Since CPI is monthly and S&P 500 data originally comes daily, the S&P 500 data is resampled to monthly frequency before merging. This allows both datasets to be compared at the same time scale.

### Ethical and Legal Considerations

The datasets used in this project are public economic and financial datasets. They do not contain personal, private, confidential, or sensitive information. Because the project does not involve individual-level data, there are no major privacy or consent concerns.

However, there are still legal and ethical responsibilities related to data use. The project cites the original data sources and uses the data only for academic purposes. FRED data and Yahoo Finance data are subject to their own terms of use. The project does not claim ownership over the original source data. The project code is licensed separately in the `LICENSE` file, while data usage notes are documented in `DATA_LICENSE.md`.

---

## Data Quality

The data quality assessment focused on completeness, consistency, validity, and usability of the CPI, S&P 500, and integrated datasets. Since the project uses time-series data from two different sources, one of the most important quality issues was making sure the datasets could be aligned correctly by date.

For the CPI dataset, the main quality checks included verifying that the `Date` column could be converted into a valid datetime format, checking that the `CPI` column was numeric, and confirming that the data followed a monthly frequency. The CPI data was generally clean because it came from FRED, a reliable economic data source. However, the CPI values had to be converted into numeric form to avoid issues during percent change calculations.

For the S&P 500 dataset, the main quality checks included verifying the date format, checking that the market columns were numeric, and confirming that monthly values were correctly created from the original daily data. The S&P 500 data includes `Open`, `High`, `Low`, `Close`, and `Volume` values. Since this project focuses on monthly returns, the `Close` column was especially important. Any missing or invalid closing prices would affect the return calculation.

A major data quality issue was the difference in frequency between the two datasets. CPI data is monthly, while Yahoo Finance data is originally daily. If these datasets were joined directly without transformation, many dates would not match. This issue was addressed by resampling the S&P 500 data to monthly values before integration. The project uses the first opening value, maximum high value, minimum low value, final closing value, and total volume for each month.

The integrated dataset was also assessed for missing values and duplicate records. The first row of the integrated dataset is removed because monthly percent change calculations require a previous month. This means that the first valid inflation and stock return values begin after the first month of available data. This is expected and does not indicate an error.

The project also generates data quality and integrity artifacts. The file `outputs/tables/data_quality_report.csv` summarizes row counts, column counts, missing values, duplicate rows, and date coverage for the datasets. The file `data/metadata/checksums.txt` stores SHA-256 checksums for important raw, processed, and output files. These checksums help verify whether files have changed after the workflow was executed.

Overall, the datasets are appropriate for the project because they come from reliable public sources, use structured tabular formats, and share a common time-based attribute. The main limitation is that the data supports correlation and exploratory analysis, but not strong causal claims.

---

## Data Cleaning

The data cleaning process was designed to make the CPI and S&P 500 datasets consistent, usable, and ready for integration. The cleaning process was performed using Python and pandas.

The first cleaning step was standardizing date formats. Both datasets contain date fields, but date values must be interpreted consistently before the datasets can be merged. The `Date` column in each dataset was converted into a pandas datetime object. Any rows with invalid dates were removed because they could not be used for time-series integration.

The second cleaning step was converting numeric columns into proper numeric data types. In the CPI dataset, the `CPI` column was converted to a numeric type. In the S&P 500 dataset, the `Open`, `High`, `Low`, `Close`, and `Volume` columns were converted to numeric types. This step was necessary because data downloaded from APIs or libraries can sometimes contain values stored as strings. Numeric conversion ensures that calculations such as percent change, summary statistics, and correlations work correctly.

The third major cleaning step was frequency alignment. CPI data is monthly, but S&P 500 data is originally daily. To make the datasets compatible, the S&P 500 data was resampled to monthly frequency. The monthly S&P 500 dataset uses the first opening price of the month, highest high, lowest low, final closing price, and total trading volume. This resampling step addressed the mismatch between daily and monthly data.

Next, derived variables were created. Monthly inflation was calculated using the percent change in CPI. Monthly S&P 500 return was calculated using the percent change in the monthly closing value. These derived variables are the main variables used in the final analysis.

After the derived variables were created, missing values were removed. The first row of each percent change calculation is missing because there is no previous month available for comparison. These rows were dropped from the final integrated dataset. Rows with missing required values were also removed so that analysis would not be affected by incomplete observations.

Finally, a shared `month` field was created in both datasets. This field converts each date into a monthly period and is used as the integration key. The cleaned CPI data and cleaned S&P 500 data were merged using this shared month value. The final integrated dataset was saved as `data/processed/integrated_monthly.csv`.

These cleaning steps helped address the main data quality issues in the project: inconsistent date formats, possible numeric formatting problems, different time frequencies, and missing values created during percent change calculations.

---

## Findings

The analysis focused on the relationship between monthly inflation rates and monthly S&P 500 returns from 2000 through 2024. The main outputs are stored in the `outputs/` folder.

The summary statistics are stored at:

`outputs/tables/summary_statistics.csv`

The correlation matrix is stored at:

`outputs/tables/correlation_matrix.csv`

The visualizations are stored at:

- `outputs/figures/inflation_rate.png`
- `outputs/figures/sp500_returns.png`
- `outputs/figures/inflation_vs_returns_scatter.png`

The monthly inflation rate chart shows that inflation changed substantially over the study period. Some periods had relatively low and stable inflation, while other periods showed sharper month-to-month changes. These changes reflect larger macroeconomic conditions and economic shocks.

The S&P 500 monthly returns chart shows that stock market returns are much more volatile than monthly inflation. While inflation usually changes gradually, monthly stock returns can move sharply upward or downward. This difference suggests that the stock market reacts to a wider range of factors beyond inflation alone.

The scatter plot comparing monthly inflation and S&P 500 monthly returns does not show a strong linear relationship. Points are spread across the graph, which suggests that monthly inflation by itself is not a strong predictor of monthly S&P 500 returns. The correlation matrix also suggests that the relationship is weak.

This finding is important because it shows that even though inflation is economically important, stock market performance is influenced by many additional factors. These may include interest rate expectations, Federal Reserve policy, corporate earnings, investor sentiment, recessions, employment data, and global events.

Overall, the project found that inflation and stock market returns can be integrated and compared meaningfully using time-series data, but the direct monthly relationship between the two appears limited. The project supports the idea that inflation is one useful macroeconomic indicator, but it should not be used alone to explain short-term stock market performance.

The correlation between monthly inflation rate and monthly S&P 500 returns was 0.01561, indicating a weak relationship.

---

## Future Work

There are several ways this project could be improved in the future. One important extension would be to include additional macroeconomic indicators, such as the federal funds rate, unemployment rate, GDP growth, or Treasury yields. Inflation does not affect markets in isolation, so adding more variables would provide a more complete view of the relationship between economic conditions and stock market performance.

Another useful improvement would be to examine lagged relationships. The stock market may not respond to inflation immediately. Investors may react to inflation expectations, Federal Reserve announcements, or future interest rate changes rather than the CPI number itself. A future version of this project could test whether inflation changes are related to stock market returns one month, three months, or six months later.

The analysis could also separate the data into different economic periods. For example, the relationship between inflation and stock returns may differ during recessions, financial crises, pandemic periods, or high-inflation periods. Comparing different time periods could reveal patterns that are not visible in the full dataset.

Another possible improvement would be to compare nominal and real returns. This project uses nominal S&P 500 returns, but inflation-adjusted returns may provide a better measure of investor purchasing power. Calculating real returns could make the analysis more meaningful from an investment perspective.

The project could also be expanded beyond the United States. Similar methods could be used to compare inflation and stock market returns in other countries, as long as reliable CPI and market index data are available. This would allow for cross-country comparisons and might reveal whether the U.S. pattern is unique or common across markets.

A final area for future work is improving the reproducibility package. Although the current project includes scripts, metadata, checksums, and output files, future versions could include a more advanced workflow system such as Snakemake. A workflow manager would make it easier to rerun only the parts of the project that changed and would provide stronger provenance tracking.

Overall, the project taught us that data integration requires more than simply joining two files. Time frequency, date formatting, derived variables, documentation, and reproducibility all matter when working with real-world datasets.

---

## Challenges

One of the main challenges in this project was working with datasets that had different time frequencies. The CPI dataset from FRED is monthly, while the S&P 500 data from Yahoo Finance is originally daily. This meant the datasets could not be directly merged using the exact date values. To solve this problem, the S&P 500 data was resampled to monthly frequency. This allowed both datasets to be integrated using a shared month field.

Another challenge was making sure the workflow was reproducible. At first, it would have been possible to manually download CSV files, but that would make it harder for another person to reproduce the project. To address this issue, we used the FRED API and the `yfinance` Python library to collect the data programmatically. This makes the data acquisition process more transparent and repeatable.

A third challenge involved handling API credentials. The FRED API requires an API key, but API keys should not be committed to GitHub. To address this, the project stores the key in a local `fred_api_key.txt` file and includes that file in `.gitignore`. This protects the key while still allowing the workflow to run locally.

Another issue was interpreting the results carefully. It would be misleading to claim that inflation causes stock market returns based only on this analysis. The project only examines correlation and visual patterns. Stock market performance is affected by many other variables, so the findings need to be described as exploratory rather than causal.

Finally, we needed to create several different types of documentation and artifacts, including metadata, a data dictionary, checksums, scripts, visualizations, and output tables. Organizing these files clearly was important so that reviewers could understand the workflow. We addressed this by separating raw data, processed data, metadata, scripts, outputs, and documentation into different folders.

---

## Reproducing

To reproduce this project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/ishaanb401/is477-project.git
cd is477-project
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. A FRED API key is also required to fetch CPI data. A free key can be obtained at https://fred.stlouisfed.org/docs/api/api_key.html. Once obtained, create a .env file in the root of the project and add your key as FRED_API_KEY.

4. Run the data acquisition script:

```bash
python scripts/fetch_data.py
```

5. Run the full analysis pipeline:

```bash
python scripts/run_pipeline.py
```

All outputs will be saved to outputs and the integrated dataset will be saved to data/processed/integrated_monthly.csv.

---

## References

U.S. Bureau of Labor Statistics. Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (CPIAUCNS). Federal Reserve Bank of St. Louis. https://fred.stlouisfed.org/series/CPIAUCNS

Yahoo Finance. S&P 500 (^GSPC) Historical Data. https://finance.yahoo.com/quote/%5EGSPC/history/

---
