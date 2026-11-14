# Reliable File Ingestion & Data Pipeline

## 1. Project Overview

This project implements a reliable, end-to-end data ingestion and processing pipeline using Python, Pandas, and DuckDB.

The pipeline processes incoming CSV files through multiple stages: ingestion, validation, data cleaning, transformation, and publishing into a DuckDB analytical warehouse.

It is designed to handle common real-world data engineering challenges such as duplicate records, invalid data, late-arriving files, repeated file delivery, and pipeline recovery.

## 2. Project Objectives

- Build an end-to-end data pipeline.
- Separate raw, validated, curated, and quarantine data.
- Validate incoming records before publishing.
- Identify and handle duplicate records.
- Handle invalid and missing values.
- Support late-arriving data and replay.
- Make publishing idempotent.
- Maintain pipeline logs and execution reports.
- Test pipeline functionality and data quality.
- Measure performance using large datasets.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline development |
| Pandas | Data cleaning and transformation |
| NumPy | Data generation and numerical operations |
| DuckDB | Analytical data warehouse |
| SQL | Data querying and validation |
| Jupyter Notebook | Development and execution |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## 4. Pipeline Architecture

The pipeline follows a layered data processing approach.

```text
Incoming CSV Files
        |
        v
   Ingestion Layer
        |
        v
     RAW Layer
        |
        v
  Validation Layer
        |
        +-------------------+
        |                   |
        v                   v
  Validated Data       Quarantine Data
        |
        v
 Transformation Layer
        |
        v
   Curated Layer
        |
        v
 Publishing Layer
        |
        v
 DuckDB Warehouse
        |
        v
 Reports and Monitoring
```

## 5. Project Folder Structure

```text
CandidateWorkspace/
│
├── 01_data_pipeline.ipynb
│
├── data/
│   ├── incoming/
│   ├── raw/
│   ├── validated/
│   ├── curated/
│   └── quarantine/
│
├── warehouse/
│   └── warehouse.duckdb
│
├── logs/
│
├── reports/
│
├── tests/
│   └── test_pipeline.py
│
├── README.md
├── requirements.txt
├── DATA_DICTIONARY.md
├── DESIGN_NOTES.md
└── .gitignore
```

## 6. Pipeline Workflow

### Step 1: Data Ingestion

- Read incoming CSV files using Pandas.
- Load source data into the raw layer.
- Track source file information.
- Support processing of newly received files.

### Step 2: Data Validation

- Check required columns.
- Validate data types.
- Identify missing values.
- Check invalid quantities and prices.
- Validate business rules.
- Identify duplicate records.

Invalid records are separated into the quarantine layer.

### Step 3: Data Transformation

- Clean and standardize data.
- Convert columns into appropriate data types.
- Remove or handle duplicate records according to business rules.
- Prepare clean data for analytical processing.

### Step 4: Late-Arriving Data Handling

- Identify late-arriving records.
- Process late files through the pipeline.
- Support replay and backfill of previously received data.

### Step 5: Data Publishing

- Load curated records into DuckDB.
- Use SQL to publish data into warehouse tables.
- Handle duplicate delivery using idempotent publishing logic.
- Avoid inserting duplicate business records.

### Step 6: Logging and Monitoring

- Maintain pipeline execution logs.
- Record processing status.
- Track successful and failed records.
- Generate monitoring and performance reports.

### Step 7: Testing

- Test empty input.
- Test duplicate records.
- Test missing required fields.
- Test invalid quantities and prices.
- Test invalid statuses.
- Test malformed input schemas.
- Validate publishing behavior.

## 7. Data Warehouse Design

The warehouse uses a dimensional modelling approach.

Example tables:

| Table | Description |
|---|---|
| dim_customers | Customer information |
| dim_products | Product information |
| fact_orders | Order-level transactional data |

The fact table stores business transactions, while dimension tables provide descriptive information for analytical queries.

## 8. Reliability Features

The project focuses on the following reliability requirements:

- **Data validation:** Prevent invalid records from entering the curated layer.
- **Quarantine:** Separate bad records for investigation.
- **Duplicate handling:** Identify repeated records.
- **Idempotency:** Prevent duplicate publishing when the same data is processed again.
- **Late-arriving data:** Support processing of delayed files.
- **Replay and backfill:** Allow previously received data to be processed again.
- **Logging:** Maintain information about pipeline execution.
- **Testing:** Verify important pipeline scenarios.

## 9. Performance Testing

A larger synthetic dataset is used to evaluate pipeline performance.

Performance measurements can include:

- Number of records processed.
- Data ingestion time.
- Transformation time.
- Publishing time.
- Total execution time.

Actual performance results are available in the generated reports.

## 10. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Jupyter Notebook
- Git

### Install dependencies

```bash
pip install -r requirements.txt
```

### Clone the repository

```bash
git clone https://github.com/k-shiva248/reliable-file-ingestion-pipeline.git
```

### Navigate to the project folder

```bash
cd reliable-file-ingestion-pipeline
```

### Run the notebook

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open `01_data_pipeline.ipynb` and execute the notebook cells in order.

The pipeline creates the required local data folders and DuckDB warehouse as configured in the notebook.

## 11. Expected Outputs

After successful execution, the project generates:

- Raw input data.
- Validated datasets.
- Curated datasets.
- Quarantined invalid records.
- DuckDB warehouse tables.
- Pipeline execution logs.
- Performance reports.
- Monitoring reports.

## 12. Limitations and Future Improvements

The current implementation uses local files and DuckDB to simulate a data engineering pipeline.

Possible future improvements:

- Integrate cloud object storage such as Amazon S3 or Azure Blob Storage.
- Schedule workflows using Apache Airflow.
- Use dbt for warehouse transformations.
- Add automated retries and recovery mechanisms.
- Add pipeline alerting and dashboards.
- Deploy the pipeline to a cloud environment.

## 13. Conclusion

This project demonstrates the development of a reliable data ingestion pipeline with validation, transformation, data quality checks, duplicate handling, late-arriving data support, and analytical publishing.

It demonstrates practical data engineering concepts using Python, Pandas, SQL, DuckDB, and automated testing.

