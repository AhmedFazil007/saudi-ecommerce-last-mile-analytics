# Saudi E-Commerce & Last-Mile Delivery Analytics

**MySQL Workbench · Python · Power BI · Excel · Business analysis**

I built this independent portfolio project to investigate a practical question: **when an e-commerce business gets more orders, is it also improving its commercial performance?**

The project uses **1,964,000 fully synthetic records** across five related tables—customers, products, orders, order items and deliveries—modeling a fictional Saudi e-commerce operation from **2022 to 2025**. These are not actual Saudi market figures, real customer records or verified delivery-company results.

## What stood out to me

- Annual orders increased from **60,000 (2022)** to **145,000 (2025)**.
- In 2025, orders increased **31.8%**, but delivered sales grew only **2.1%** compared with 2024.
- Average delivered order value decreased from approximately **SAR 2,966** in 2022 to **SAR 1,976** in 2025.
- Around **29.94%** of modeled delivered orders arrived later than promised.

**My interpretation:** Rising order volume alone is not enough to demonstrate stronger performance. I'd investigate product mix, discounts, sales channels and customer cohorts before recommending additional marketing investment. I would also examine late shipments by warehouse, partner and promised-delivery window rather than blaming a particular carrier without a fair comparison.

## What I would recommend

1. **Protect basket value:** Examine the reasons behind falling average order value, then test bundles and cross-sell offers where incremental margin supports them.
2. **Improve delivery reliability:** Compare like-for-like shipments and run a limited operational pilot before changing carrier allocation.
3. **Use careful profitability definitions:** Product contribution excludes some order-level discounts, fulfillment costs and overhead. It must not be presented as net profit.
4. **Model business opportunities transparently:** Excel scenarios illustrate possible outcomes under explicit assumptions—not actual achieved savings.

## Project deliverables

| Location | Contents |
|---|---|
| `mysql/` | Five numbered SQL scripts: schema, data loading, checks, business analysis and reporting views |
| `python/` | Synthetic data generator, MySQL loader, dataset validator and aggregate rebuilder |
| `Saudi_Ecommerce.pbip` | Power BI project entry point |
| `Saudi_Ecommerce.Report/` | Editable six-page report definition and resources |
| `Saudi_Ecommerce.SemanticModel/` | Power BI semantic model, relationships and measures |
| `analysis/` | Saved KPI aggregates and quality-check results |
| `data/` | Data dictionary, five sample CSV files and instructions for generating full data locally |
| `excel/` | Assumption-driven business-impact scenario workbook |
| `reports/` | Executive analysis and recommendations PDF |
| `screenshots/` | Six dashboard screenshots in presentation order |
| `docs/` | Setup instructions, project structure and publication validation checklist |

The full synthetic dataset contains **160,000 customers, 4,000 products, 400,000 orders, 1,000,000 order items and 400,000 deliveries**. Large raw CSVs and database files are generated locally and deliberately excluded from GitHub to keep the repository manageable.

## Quick start

The full synthetic dataset is reproducible but is **not** included in GitHub. Run the generator only when you are ready to create a local dataset. Delete or move a previous generated `data/saudi_ecommerce.sqlite` database before rerunning; otherwise table creation will fail. Do not commit local databases, credentials or full raw CSVs.


1. Install Python dependencies: `pip install -r requirements.txt`.
2. Run `python python/generate_synthetic_data.py` to generate local CSV files under `data/raw/` and an offline SQLite copy under `data/` (these are not committed).
3. Execute `mysql/01_schema.sql` in MySQL Workbench, then use `python python/load_mysql.py --host localhost --user root` or adapt `mysql/02_load_data.sql`.
4. Run `mysql/03_quality_checks.sql` and review the results.
5. Open `Saudi_Ecommerce.pbip` in Power BI Desktop, configure the MySQL connection, and refresh.

See [setup instructions](docs/SETUP.md), [dashboard screenshots](screenshots/), and [executive report](reports/Executive_Analysis_and_Recommendations.pdf).

## MySQL and Power BI

MySQL Server 8 and **MySQL Workbench** are the primary database environment. The Power BI project is designed to connect to the `saudi_ecommerce` database with the five tables above.

**Verification note:** The PBIP files and measures were checked programmatically; the final report rendering and MySQL refresh still need to be tested in Power BI Desktop. Please do not treat hypothetical Excel scenarios as realized business results.

---

*Independent portfolio project. All figures and entities in the dataset are synthetic.*