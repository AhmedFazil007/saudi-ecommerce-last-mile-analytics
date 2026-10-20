# Reproducing the project

## Requirements
- MySQL Server 8 and MySQL Workbench
- Power BI Desktop with PBIP/TMDL support
- Python 3.10+ for data generation and analysis (scripts may need to be uploaded separately)

## Workflow
1. Obtain the five synthetic CSV files (`customers`, `products`, `orders`, `order_items`, `deliveries`). These large files are not currently included in this repository.
2. Execute `mysql/01_schema.sql` in MySQL Workbench, then import CSVs in dependency order: customers, products, orders, order_items, deliveries. Verify column mapping, dates, and encoding.
3. Run `mysql/03_quality_checks.sql` and resolve any discrepancies before interpreting results.
4. Run `mysql/04_business_analysis.sql` and `mysql/05_powerbi_views.sql` for analysis and reporting views.
5. Open `Saudi_Ecommerce.pbip` in Power BI Desktop. Configure the MySQL data source and credentials for your environment and refresh the semantic model.
6. Compare KPIs with SQL results, test slicers and cross-filtering, and inspect all six report pages.

## Important limitations
- Data are entirely synthetic, representing a fictional business in Saudi Arabia during 2022–2025.
- Product gross profit does not equal net profit: order discounts, delivery costs, operating expenses and overhead require separate treatment.
- Excel scenarios, if added, are hypothetical rather than achieved financial benefits.
- Report rendering and MySQL refresh require validation in the user's local Power BI Desktop installation.
