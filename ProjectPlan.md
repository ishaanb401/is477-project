**BearDown Project Proposal**

**Overview**  
The goal of our project is to examine the relationship between inflation and stock market performance in the United States. We will analyze how changes in inflation rates may affect the returns of the S\&P 500 over time. Inflation is an important economic indicator that can influence investor behavior, interest rates, and overall market conditions. We want to better understand whether higher inflation is associated with lower stock market returns, increased volatility, or delayed effects on the market.  
For our analysis, we will combine macroeconomic data from the Federal Reserve Bank of St. Louis and historical stock market data from Yahoo Finance. FRED provides reliable time-series data for economic indicators. We will focus on the Consumer Price Index (CPI), which is commonly used to measure inflation. Yahoo Finance provides historical daily prices for the S\&P 500 index. We decided to integrate these datasets because they both include data-based time series data.  
We will first collect the datasets and store them in structured files such as CSVs. We will then clean the data by fixing missing values, standardizing date formats, and adjusting the time frequency so both datasets can be compared. We are planning to convert daily stock prices to monthly averages. After cleaning, we will integrate both datasets using Python and the Pandas library based on the date variable. Finally, we will conduct exploratory analysis and visualizations to identify patterns, correlations, and possible delayed effects between inflation and stock market returns. We will document and automate the analysis to make sure it is reproducible.

**Team**  
Ishaan Bhargava \- Data Collection, Storage, and Documentation  
Ishaan will focus on acquiring the datasets and organizing the data infrastructure. He will collect inflation data from the Federal Reserve Bank of St. Louis and historical S\&P 500 stock price data from Yahoo Finance. He will be responsible for downloading and accessing the datasets through APIs, and storing the data in CSV files while also organizing the project directory.  
Other responsibilities include documenting the data sources, file structures, and metadata, including dataset descriptions, variable explanations, and license or usage policies. He will also help assess the ethical considerations and data usage constraints related to the datasets.

Aamir Abjani \- Data Processing, Integration, and Analysis  
Aamir will focus on preparing and analyzing the data. He will clean the datasets by handling missing values, standardizing date formats, and aligning time intervals between both datasets. He will also integrate both datasets in Python on the date.  
After integration, he will conduct exploratory data analysis, create visualizations, and compute summary statistics to examine the relationship between inflation and stock market returns. Finally he will implement and automated workflow to ensure the analysis can be reproduced

Ishaan and Aamir will collaborate on interpreting the results, writing the final report, and reviewing the project.

**Research Question**

How does inflation, measured by the U.S. Consumer Price Index (CPI), affect S\&P 500 stock market returns and are there effects that are observable over time?

**Datasets**

The first dataset we will be using is the Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (CPIAUCSL) from FRED. This is a time series dataset that collects CPI data in monthly intervals. The data from this dataset dates back to 1947\. While we are unsure if we will go back that far to answer our research question, we will have plenty of data for the purpose of this project. This dataset is a price index of goods and services paid by urban consumers. The percent changes in the price index measure the inflation rate between any two time periods. This index tracks \~88% of the total population including wage earners, clerical workers, technical workers, self-employed, short-term workers, unemployed, retirees, and those individuals not in the labor force. CPI’s in this index are based on prices for food, shelter, clothing, transportation, service fees, and sales tax. Prices are collected monthly from \~4,000 housing units and \~26,000 retail establishments across 87 urban areas. From this dataset we will be able to recognize periods of inflation and deflation.

The second dataset we will be using is the S\&P 500 (^GSPC) from Yahoo Finance. This dataset is a benchmark index that tracks the performance of the 500 largest publicly traded U.S. companies. The dataset includes information such as open price, close price, high price, low price, and volume. For the purpose of this project we will be closely looking at the close price to see how S\&P 500 returns are affected. The data from the ^GSPC dataset goes all the way back to 1927, which is further back than the FRED dataset. While we definitely won’t be able to use all of this data, we have more than enough to work with and accurately answer our research question.

To answer our research question we must be able to integrate the two datasets with each other. We will do this through the use of the date column. Both the FRED CPI dataset and the S\&P 500 Yahoo Finance dataset have a date column that has aggregate monthly data. We will use one inflation value and one market return value per row to answer our research question. This is not set in stone, but this gives us a good foundation for us to build off of as we begin our project. 

**Timeline**

Plan

Files, Storage, Organization

We will use CSV files because both datasets are structured time-series data  
We plan on having the following directory structure

* Project  
  * Data  
    * Raw (original downloaded datasets)  
    * Cleaned (processed datasets ready for analysis)  
  * Scripts (python code for cleaning, integration, and analysis)  
  * Outputs (charts, results, and summary statistics)  
  * Documentation (metadata and project explanations)

Ethical Data Handling

The datasets used for the project are publicly available economic and financial datasets. This means there are no issues related to personal data, consent, or privacy. Both sources allow public access to their datasets for research and educational purposes.  
We will respect all licensing and terms of use by properly citing data sources. No copyrighted or restricted datasets will be redistributed, and all datasets will be used strictly for academic analysis.

Data Collection and Acquisition

Dataset 1 \- Inflation Data

* Source: Federal Reserve Bank of St. Louis FRED  
* Indicator: Consumer Price Index (CPI)  
* Access Method: API or CSV download  
* Frequency: Monthly time-series data

Dataset 2 \- Stock Market Data

* Source: Yahoo Finance  
* Indicator: Historical S\&P 500 prices  
* Access Method: Downloaded CSV or Python yfinance library  
* Frequency: Daily data

Data Integration

Datasets will be integrated using Python and the Pandas library. Since the inflation data is monthly and stock data is daily, stock prices will be converted into monthly average returns before integration. After adjusting time frequencies, the datasets will be merged using the date field as the key variable.

Data Quality Assessment  
A data quality check will be performed before analysis. This will include checking for missing values, inconsistent timestamps, duplicate entries, and unusual outliers in the datasets. Summary statistics and visualizations will be used to identify potential issues. If significant data gaps exist, they will be documented and addressed during cleaning.

Data Cleaning  
Several cleaning steps will be applied to ensure the datasets are suitable for analysis. Missing values will be handled by either removing incomplete rows or applying appropriate interpolation methods. Date formats will be standardized across both datasets. Daily stock prices will be aggregated into monthly averages to align with the CPI data frequency. Any obvious outliers or formatting inconsistencies will also be corrected.

Workflow Automation, Reproducibility, and Data Documentation  
We will automate the workflow using Python. These scripts will perform data collection, integration, and analysis. We will include all scripts, datasets, and documentation needed to reproduce the analysis, along with instructions on how to run the workflow. Documentation of the project will include dataset sources descriptions of variables, units of measurement, time coverage, and data collection methods.

Task Plan

* Week 1 (3/10) \- Project Setup  
  * Define research questions and datasets  
  * Download datasets  
  * Organize project folders  
  * Responsibility: Ishaan Bhargava  
* Week 3 (3/24) \- Data Preparation  
  * Assess data quality  
  * Perform data cleaning and formatting  
  * Convert stock data to monthly values  
  * Responsibility: Aamir Abjani  
* Week 5 (4/7) \- Data Integration  
  * Merge datasets using Python  
  * Perform exploratory analysis and visualization  
  * Responsibility: Aamir Abjani  
* Week 7 (4/21) \- Automation and Documentation  
  * Create automated scripts for the workflow  
  * Write metadata and documentation  
  * Prepare final report  
  * Responsibility: Ishaan Bhargava & Aamir Abjani

Constraints  
Datasets may have different time frequencies, which will need to be addressed by converting daily stock data to monthly values. Inflation data may not perfectly capture real-time economic conditions that affect markets. Stock market performance can be influenced by many factors besides inflation, such as interest rates or geopolitical events, which means we may not be able to draw strong conclusions.

Gaps  
At this stage, some aspects of the project still need further clarification. Specific inflation indicators from FRED and the exact time range of the analysis still need to be finalized. The team may also explore whether additional economic indicators, like interest rates, should be included to improve the analysis. Our process may evolve as new insights are discovered during the project.