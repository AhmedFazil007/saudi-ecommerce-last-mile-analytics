# Reproducing the Saudi E-Commerce analytics project

## Requirements
- Python 3.10+ and dependencies in `requirements.txt`
- MySQL Server 8 with MySQL Workbench
- Power BI Desktop with PBIP/TMDL support

## 1. Generate the synthetic source data
From the repository root:

```bash
pip install -r requirements.txt
python python/generate_synthetic_data.py
```

This creates five large CSVs under `data/raw/` and an offline SQLite database at `data/saudi_ecommerce.sqlite`. They are intentionally excluded from version control. Generation may require significant time and disk space. **Before rerunning the generator**, remove or move an existing `data/saudi_ecommerce.sqlite` file; the script creates its tables from scratch and does not overwrite an existing database. Generated CSVs in `data/raw/` are overwritten. The existing `data/sample/` files are for inspection, not the complete dataset.

## 2. Load MySQL
Run `mysql/01_schema.sql` in MySQL Workbench, then either:

```bash
python python/load_mysql.py --host localhost --user root
```

or edit the file paths in `mysql/02_load_data.sql` and execute it in Workbench with LOCAL INFILE enabled. The loader imports tables in foreign-key-safe order. Passwords are prompted, not stored in source files.

## 3. Validate and analyze
Run `mysql/03_quality_checks.sql`, `mysql/04_business_analysis.sql`, and `mysql/05_powerbi_views.sql`. Use `python python/validate_dataset.py` for offline validation of the generated SQLite copy; use `python python/rebuild_aggregates.py` to regenerate selected KPI CSVs. Other committed analysis files represent the original synthetic case study.

## 4. Open Power BI
Open `Saudi_Ecommerce.pbip` from the repository root. Keep `Saudi_Ecommerce.Report/` and `Saudi_Ecommerce.SemanticModel/` together, configure the local MySQL source, refresh and compare visuals against SQL KPIs.

## Interpretation
All data are synthetic and the 2022–2025 growth patterns are modeled. Estimated product gross profit is not net profit. The Excel scenarios are hypothetical, not realized savings. Final Power BI Desktop rendering and refresh must be verified locally.
