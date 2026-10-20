# Synthetic data

This fictional Saudi e-commerce case study models five linked tables: 160,000 customers, 4,000 products, 400,000 orders, 1,000,000 order items and 400,000 deliveries (1,964,000 rows total).

- `DATA_DICTIONARY.md` describes fields, relationships, grains and KPI definitions.
- `sample/` contains five small sample CSV files.
- Run `python python/generate_synthetic_data.py` to produce complete CSVs in `raw/` and `saudi_ecommerce.sqlite` here locally. These large generated files should remain outside GitHub.

The records, business operations and modeled figures are entirely synthetic; no real customer information is used.
