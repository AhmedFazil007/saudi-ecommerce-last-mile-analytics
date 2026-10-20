# Repository layout and upload checklist

```
Saudi_Ecommerce.pbip
Saudi_Ecommerce.Report/             # Power BI report definition (keep exact name)
Saudi_Ecommerce.SemanticModel/      # Power BI semantic model (keep exact name)
screenshots/                         # Six descriptively named dashboard screenshots
mysql/                               # SQL schema, quality checks, analysis and views
python/                              # Data generation, loading and validation scripts (pending)
analysis/                            # Validated KPI summaries (pending)
data/sample/                         # Small synthetic sample CSVs and data dictionary (pending)
dashboard/                           # Optional standalone browser dashboard (pending)
excel/                               # Optional assumption-based scenario workbook (pending)
reports/                             # Executive analysis and recommendations (pending)
docs/                                # Setup, project structure and validation checklist
```

The editable PBIP report uses a relative path to `Saudi_Ecommerce.SemanticModel`. **Do not rename or separate the `.Report` and `.SemanticModel` folders without updating Power BI references.**

Avoid uploading database credentials, real customer records, multi-gigabyte datasets, `.pbix` cache files or Power BI local settings. Large raw synthetic datasets are better distributed through a separate release or data hosting service.
