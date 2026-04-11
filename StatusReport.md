# Status Report

## Project Title

Inflation and Stock Market Performance in the United States

## Team Members

- Team Member 1: Ishaan Bhargava
- Team Member 2: Aamir Abjani

---

## 1. Progress Update on Project Plan Tasks

### 1. Data lifecycle

We have continued to structure the project around a full data lifecycle that includes collection, storage, cleaning, integration, analysis, and documentation. At this stage, we have already implemented the data collection and integration portions of the workflow and created supporting documentation for reproducibility. The current workflow is documented in [`docs/workflow_diagram.md`](docs/workflow_diagram.md).

### 2. Files, storage, and organization

We finalized a repository structure that separates raw data, processed data, scripts, outputs, and metadata. This organization makes it easier to track provenance and distinguish between original and transformed files. Relevant artifacts include:

- [`data/raw/`](data/raw/)
- [`data/processed/`](data/processed/)
- [`scripts/`](scripts/)
- [`outputs/`](outputs/)
- [`data/metadata/dataset_metadata.md`](data/metadata/dataset_metadata.md)

### 3. Ethical data handling

We confirmed that both datasets are publicly accessible and do not contain personal or sensitive data. Our current documentation notes the sources and intended academic use of the data. We are still reviewing any terms of use language that should be cited more explicitly in the final report.

### 4. Data collection and acquisition

This task is substantially complete. We selected and accessed two trustworthy datasets using two different access methods:

- FRED CPI data through the FRED API
- S&P 500 historical data through the `yfinance` Python library

Artifacts:

- [`scripts/fetch_data.py`](scripts/fetch_data.py)

### 5. Extraction and enrichment

This part remains limited because enrichment was optional in our project plan. We have not yet added a third variable, but we may extend the analysis later by including interest rates or unemployment as contextual variables from FRED.

### 6. Data integration

This task is in progress and largely functional. We created a script that standardizes dates, converts daily stock prices to monthly values, computes monthly inflation and return rates, and merges the datasets on a shared monthly key.

Artifacts:

- [`scripts/integrate_data.py`](scripts/integrate_data.py)
- [`data/processed/integrated_monthly.csv`](data/processed/integrated_monthly.csv) _(generated after running pipeline)_

### 7. Data quality

Initial quality assessment has begun. We checked for missing values, invalid dates, and numeric conversion issues. We also identified one of the main quality challenges in the project: the two sources operate at different temporal frequencies. This is being addressed by monthly resampling of stock data. Quality checks are currently implemented in the scripts and will be expanded further in the final version.

Artifacts:

- [`scripts/integrate_data.py`](scripts/integrate_data.py)

### 8. Data cleaning

Cleaning methods implemented so far include:

- converting date fields into a standardized datetime format
- coercing numeric columns into numeric types
- dropping invalid or missing records
- resampling daily S&P 500 data to monthly values
- computing percent changes for inflation and stock returns

Artifacts:

- [`scripts/integrate_data.py`](scripts/integrate_data.py)

### 9. Workflow automation and provenance

This task is in progress. We now have an automated pipeline script that runs the full workflow from collection to output generation. This improves provenance because each transformation step is scripted instead of being done manually.

Artifacts:

- [`scripts/run_pipeline.py`](scripts/run_pipeline.py)
- [`docs/workflow_diagram.md`](docs/workflow_diagram.md)

### 10. Reproducibility and provenance

We have made good progress here by organizing the repository clearly, documenting dependencies in `requirements.txt`, and adding execution instructions in the README. Reproducibility will be improved further by adding version details and final output snapshots before project submission.

Artifacts:

- [`requirements.txt`](requirements.txt)

### 11. Metadata and documentation

This task is partially complete. We created an initial metadata file that documents data sources, formats, variables, and integration logic. We plan to expand this with additional field-level descriptions and data quality notes.

Artifacts:

- [`data/metadata/dataset_metadata.md`](data/metadata/dataset_metadata.md)

---

## 2. Updated Timeline

| Task                                                  | Status                    | Expected Completion | Responsible     |
| ----------------------------------------------------- | ------------------------- | ------------------- | --------------- |
| Finalize dataset access and scripts                   | Completed                 | 4/7                 | Ishaan Bhargava |
| Organize repository and metadata structure            | Completed                 | 4/8                 | Ishaan Bhargava |
| Clean CPI and S&P 500 data                            | In Progress               | 4/21                | Aamir Abjani    |
| Integrate datasets into one monthly table             | In Progress               | 4/21                | Aamir Abjani    |
| Produce initial visualizations and summary statistics | In Progress               | 4/21                | Aamir Abjani    |
| Expand data quality assessment                        | Not Started / In Progress | 4/21                | Both            |
| Refine documentation and provenance notes             | In Progress               | 4/28                | Ishaan Bhargava |
| Draft final report and interpretation                 | Not Started               | 5/1                 | Both            |
| Final review and repository cleanup                   | Not Started               | 5/1                 | Both            |

---

## 3. Changes to the Project Plan

The overall research question has remained the same, but we made a few practical changes to the original plan as the implementation became more concrete.

First, we decided to use the FRED API directly instead of manually downloading CSV files. This makes the workflow more automated and better aligned with the reproducibility goals of the project. Second, we chose to use the `yfinance` Python library for Yahoo Finance data instead of manual export, again to support automation and consistent provenance. Third, we refined the integration strategy by converting stock data to monthly values before merging with CPI data, since the two sources come in different native frequencies.

Based on feedback from Milestone 2, we also made the project structure more explicit by separating raw data, processed data, outputs, and metadata into different folders. We also added a workflow diagram and more specific documentation artifacts, since the earlier plan described these ideas but did not yet show them in the repository.

---

## 4. Challenges and Problems Encountered

### Different time frequencies

The biggest issue so far has been that CPI data is monthly while S&P 500 data from Yahoo Finance is daily. This made direct integration impossible without transformation. We resolved this by resampling the stock data to monthly frequency before computing returns and merging.

### Data formatting inconsistencies

Another issue was that different sources return data in different schemas and formats. FRED returns JSON through the API, while `yfinance` returns a pandas DataFrame. We addressed this by writing separate collection scripts and standardizing the output into CSV files with consistent date formatting.

### Reproducibility concerns

A challenge in the early project plan was that manual downloads would make it harder for others to reproduce the work. We addressed this by scripting the collection process and documenting dependencies in `requirements.txt` and the README.

### Remaining issue: deeper quality assessment

Although the basic cleaning steps are complete, we still need a more formal quality assessment section that reports missingness, date coverage, and possible anomalies in the final integrated dataset. We plan to add this in the next phase by generating summary checks automatically.

---

## 5. Team Member Contributions

### Ishaan Bhargava Contribution Summary

I worked on the project setup, repository organization, and data acquisition workflow. I helped identify the final datasets, created the folder structure for raw and processed data, wrote the script for collecting CPI data from the FRED API, and contributed to the README and metadata documentation. I also helped review ethical and reproducibility considerations for the project.

### Aamir Abjani Contribution Summary

I worked on data processing and analysis tasks. I created the scripts for collecting stock market data with `yfinance`, integrating the CPI and S&P 500 datasets, and generating summary outputs and visualizations. I also helped define the cleaning strategy, especially for aligning the different data frequencies, and reviewed the integrated dataset for quality issues.

---

## 6. Current Repository Artifacts

### Data and metadata

- [`data/metadata/dataset_metadata.md`](data/metadata/dataset_metadata.md)

### Scripts

- [`scripts/fetch_data.py`](scripts/fetch_data.py)
- [`scripts/integrate_data.py`](scripts/integrate_data.py)
- [`scripts/run_pipeline.py`](scripts/run_pipeline.py)

### Documentation

- [`README.md`](README.md)
- [`docs/workflow_diagram.md`](docs/workflow_diagram.md)

### Outputs

- [`outputs/figures/`](outputs/figures/)
- [`outputs/tables/`](outputs/tables/)

---

## 7. Next Steps

Our next steps are to run the full pipeline, generate the processed dataset and figures, expand the data quality assessment, and continue improving documentation. After that, we will begin drafting the final analysis and interpretation of results.

---
