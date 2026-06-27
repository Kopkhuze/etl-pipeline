# ETL Pipeline — Chicago Tracffic 

A modular Python-based ETL (Extract, Transform, Load) pipeline built around the Chicago Traffic dataset. This project demonstrates the ability to ingest data from multiple source types, apply transformation logic, and load the results into a target database or file store.

Built as a data engineering portfolio project.

---
## Project Structure

## Project Structure

    etl-pipeline/
    ├── src/
    │   ├── extract/        # Data ingestion — CSV, Parquet, Database, API
    │   ├── transform/      # Cleaning, feature engineering, aggregations
    │   └── load/           # Output to database or file
    ├── data/
    │   ├── raw/            # Raw source data (unmodified)
    │   └── processed/      # Transformed, ready-to-use data
    ├── tests/              # Unit tests for each pipeline stage
    ├── pipeline.py         # Main entry point — runs the full pipeline
    └── README.md
---

## Data Source

**Chicago Traffic Records** 

The extract module supports pulling this data from:
- CSV files


---

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
git clone https://github.com/Kopkhuze/etl-pipeline.git
cd etl-pipeline
pip install -r requirements.txt
```

### Running the Pipeline

```bash
python pipeline.py
```

---

## Tech Stack

- **Language:** Python 3.11
- **Data processing:** pandas
- **Database:** SQLite / PostgreSQL
- **Testing:** unittest

---

## Project Status

In active development — extract module complete, transform and load coming soon.

---

## Author

**Kobedi** — Data Engineering Graduate

