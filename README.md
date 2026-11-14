# Reliable File Ingestion and Data Pipeline

## Project Overview

This project implements an end-to-end reliable data ingestion and processing pipeline using Python, Pandas, NumPy, and DuckDB.

The pipeline processes e-commerce order data through multiple stages, including ingestion, validation, transformation, duplicate detection, late-arriving data handling, and publishing into an analytical warehouse.

The main objective is to build a reliable and reproducible data pipeline that handles data quality issues, duplicate records, invalid data, and large datasets.

## Architecture

```text
             Incoming Data
                   |
                   v
                Raw Zone
                   |
                   v
            Validation Layer
                   |
             +-----+-----+
             |           |
             v           v
        Valid Records  Invalid Records
             |           |
             v           v
       Validated Zone  Quarantine Zone
             |
             v
        Transformation
             |
             v
          Curated Zone
             |
             v
        DuckDB Warehouse
             |
             v
       Analytical Queries
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline development |
| Pandas | Data processing and transformation |
| NumPy | Data generation and numerical operations |
| DuckDB | Analytical data warehouse |
| SQL | Data querying and validation |
| Jupyter Notebook | Development environment |
| Pytest | Automated testing |
| Git and GitHub | Version control |

## Project Features

1. Batch file ingestion
2. Raw data storage
3. Schema validation
4. Business rule validation
5. Null value detection
6. Duplicate record detection
7. Invalid record quarantine
8. Data cleaning and transformation
9. Idempotent data publishing
10. Late-arriving data handling
11. Replay and backfill workflow
12. DuckDB analytical warehouse
13. Data reconciliation
14. Logging and monitoring
15. Performance testing with 100,000 records
16. Automated validation tests

## Data Pipeline Layers

### 1. Incoming Zone
Receives source CSV files containing transactional order data.

### 2. Raw Zone
Stores ingested source data for further processing.

### 3. Validated Zone
Stores records that pass schema and business validation.

### 4. Curated Zone
Contains cleaned and transformed data ready for analytical processing.

### 5. Quarantine Zone
Stores invalid records separately for investigation and correction.

## Data Warehouse Design

The warehouse uses a dimensional data model.

### Dimension Tables

- `dim_customers` – Customer information.
- `dim_products` – Product information.

### Fact Tables

- `fact_orders` – Functional order-level analytical data.
- `fact_orders_performance` – Separate performance-test data.

**Fact grain:** One row per order.

## Data Quality and Validation

The pipeline checks:

- Required columns
- Missing values
- Duplicate order IDs
- Invalid quantities
- Invalid prices
- Invalid order statuses
- Customer and product references
- Foreign key integrity

Invalid records are separated into the quarantine zone.

## Reliability Features

- Duplicate detection
- Idempotent publishing
- Late-arriving data processing
- Replay and backfill support
- Source-to-target reconciliation
- Execution logging
- Pipeline status monitoring

## Performance Testing

A separate performance test uses a generated dataset of 100,000 order records.

Performance testing covers:

- Data ingestion time
- Data transformation time
- Memory usage
- Processing throughput
- Warehouse loading
- Query execution

Performance results are available in:

`reports/performance_report.csv`

## Automated Testing

The project includes notebook-based validation tests and a standalone pytest test module.

### Notebook Tests

9 validation checks covering data quality, database integrity, empty input, duplicate records, invalid data, and idempotency.

### Pytest Tests

8 tests covering:

- Happy path
- Empty input
- Duplicate records
- Missing required fields
- Invalid quantity
- Invalid price
- Invalid status
- Malformed schema

Run the tests:

```bash
python -m pytest tests/test_pipeline.py -v
```

## Monitoring and Logging

Pipeline execution details are recorded in:

- `logs/pipeline_execution.log`
- `reports/pipeline_monitoring_report.csv`

Monitoring includes record counts, execution status, reconciliation results, and errors.

## Project Structure

```text
reliable-file-ingestion-pipeline/
│
├── Data Pipeline/
│   └── 01_data_pipeline.ipynb
│
├── README.md
├── data.zip
│
├── logs/
│
├── reports/
│   ├── performance_report.csv
│   └── pipeline_monitoring_report.csv
│
└── tests/
    └── test_pipeline.py
```

Additional documentation and data folders can be added as the project is organized.

## Setup and Execution

### 1. Clone the repository

```bash
git clone https://github.com/k-shiva248/reliable-file-ingestion-pipeline.git
```

### 2. Navigate to the project directory

```bash
cd reliable-file-ingestion-pipeline
```

### 3. Install dependencies

```bash
pip install pandas numpy duckdb jupyter pytest
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `Data Pipeline/01_data_pipeline.ipynb` and execute the cells in sequence.

## Storage Implementation

This project uses local directories to simulate data storage zones such as raw, validated, curated, and quarantine.

DuckDB is used as the local analytical warehouse. The implementation does not require cloud infrastructure.

## Limitations and Future Improvements

- Integrate cloud object storage such as AWS S3 or Azure Blob Storage.
- Orchestrate workflows using Apache Airflow.
- Add a cloud-based analytical warehouse such as Snowflake.
- Implement CI/CD for automated testing and deployment.
- Improve historical tracking of changing records.

## Author

**Shiva Prasad**

GitHub: https://github.com/k-shiva248


