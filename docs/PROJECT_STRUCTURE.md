# Repository structure

```text
Saudi_Ecommerce.pbip                  Power BI project entry point
Saudi_Ecommerce.Report/               Editable report definition and assets
Saudi_Ecommerce.SemanticModel/        TMDL semantic model and measures
mysql/                                01 schema, 02 load, 03 checks, 04 analysis, 05 views
python/                               Synthetic generator, MySQL loader, validation, aggregates
data/DATA_DICTIONARY.md               Entity grains, relationships, KPI definitions
data/sample/                          Five small synthetic sample CSV files
analysis/                             KPI CSVs, aggregate JSON and quality checks
excel/Business_Impact_Scenarios.xlsx  Hypothetical business-impact model
reports/Executive_Analysis_and_Recommendations.pdf
screenshots/                           Six dashboard screenshots in presentation order
docs/                                  Setup, project structure and validation checklist
requirements.txt
README.md
```

Generated large CSV files under `data/raw/` and the offline `data/saudi_ecommerce.sqlite` are not tracked. To reproduce them run `python python/generate_synthetic_data.py`.

Do not rename or separate `Saudi_Ecommerce.Report/` and `Saudi_Ecommerce.SemanticModel/`; the Power BI report references the semantic model by relative path. No separate HTML dashboard is part of this project.
