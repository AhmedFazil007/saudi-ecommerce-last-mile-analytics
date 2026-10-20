# Saudi E-Commerce & Last-Mile Delivery Analytics

**Business question:** *Are more orders creating more value—or just more operational work?*

**MySQL · Python · Power BI · Excel · Business analysis**

> **Portfolio case study — 100% synthetic data.** This is a fictional Saudi e-commerce business covering 2022–2025. Figures, cities, carriers, and outcomes are simulated; they do not describe actual Saudi market performance or real delivery partners.

## Executive decision brief

**The central finding: order volume is expanding much faster than delivered sales.** In 2025, modeled orders grew **31.8%**, while delivered sales grew **2.1%**. Delivered average order value (AOV) declined **20.1%** year over year. Management should investigate basket composition and customer economics before prioritizing additional order acquisition.

| 2025 indicator | Result | Business interpretation |
|---|---:|---|
| Orders | **145,000** | **+31.8% YoY**; more transactions to serve |
| Delivered sales | **SAR 255.63M** | **+2.1% YoY**; modest sales expansion |
| Delivered AOV | **SAR 1,976** | **−20.1% YoY**; smaller realized baskets |
| Late delivery rate | **~29.9%** | About 3 in 10 completed deliveries missed the modeled promise |
| Cancellation rate | **4.90%** | Operational leakage worth segmenting by reason, channel and geography |

**Recommended management priorities:** (1) diagnose falling basket value, (2) improve delivery reliability through targeted operational tests, and (3) focus retention and merchandising efforts on contribution—not only transaction count.

[Read the full decision-oriented business analysis →](reports/BUSINESS_INSIGHTS_AND_ACTION_PLAN.md)

## Dashboard: six management views

| Page | Decision it supports | Preview |
|---|---|---|
| Executive Overview | Is growth creating business value? | [View](screenshots/01_executive_overview.png) |
| Sales & Profitability | Which categories and trends merit attention? | [View](screenshots/02_sales_profitability.png) |
| Customer Intelligence | Which customers and channels deserve investigation? | [View](screenshots/03_customer_intelligence.png) |
| Delivery & Logistics | Where should service reliability improve? | [View](screenshots/04_delivery_logistics.png) |
| Order Quality | Where are cancellations and returns occurring? | [View](screenshots/05_order_quality.png) |
| Business Opportunities | Which improvement hypotheses should be tested? | [View](screenshots/06_business_opportunities.png) |

![Executive Overview dashboard](screenshots/01_executive_overview.png)

## Insights that change decisions

### 1. Growth without comparable basket value
2024 → 2025 orders: **110,000 → 145,000**. Delivered sales: **SAR 250.41M → SAR 255.63M**. Delivered AOV: **SAR 2,474 → SAR 1,976**.

**Action:** Segment AOV by year, channel, product category, discount band and customer cohort. Pilot margin-aware bundles or cross-sell offers **only after** determining what drove the change. The synthetic generator intentionally changes items per order, so the trend should **not** be attributed to customer behavior without qualification.

### 2. Delivery reliability is a cross-partner issue
The modeled late-delivery rate is approximately **29.9%**. Carrier late rates are clustered between **29.72% and 30.30%**.

**Action:** Compare shipments with similar warehouse, city, promise length and order characteristics. Test better promise-setting and exception alerts before selecting a “worst” carrier. Differences here are synthetic and do not demonstrate actual carrier quality.

### 3. Commercial activity is concentrated
Riyadh, Jeddah and Dammam account for approximately **59.1%** of modeled delivered sales. The mobile app contributes approximately **61.8%** of delivered sales.

**Action:** Prioritize analysis of service levels, repeat purchase behavior and basket economics in these major segments; avoid interpreting simulated geographic allocation as real market demand.

### 4. Category contribution needs careful definition
Electronics and Home & Kitchen account for approximately **70.1% of delivered gross item sales** across categories. This is **before** order-level discounts, shipping charges, delivery costs and overhead.

**Action:** Compare **contribution after discount and fulfillment costs**, not gross item sales alone, before reallocating marketing or inventory budgets.

## Recommended 30–60–90 day plan

| When | Management experiment | KPI to monitor |
|---|---|---|
| Days 1–30 | Diagnose basket decline by mix, order size and discounts; establish like-for-like baselines | Delivered AOV, sales/order, pre-discount item margin |
| Days 31–60 | Pilot targeted bundles and delivery exception alerts on limited cohorts | Incremental contribution/order, late delivery %, complaints |
| Days 61–90 | Evaluate pilot versus matched control; scale only statistically and commercially credible improvements | Contribution after fulfillment, repeat purchase, service-level attainment |

**Decision rule:** Treat each intervention as a hypothesis. No savings, uplift or causal impact has been demonstrated by this synthetic case study.

## Project contents

| Location | Purpose |
|---|---|
| [Business insights and action plan](reports/BUSINESS_INSIGHTS_AND_ACTION_PLAN.md) | Findings, evidence, recommendations, tests and caveats |
| [Executive PDF](reports/Executive_Analysis_and_Recommendations.pdf) | Downloadable executive narrative |
| [Power BI project](Saudi_Ecommerce.pbip) | Entry point for editable six-page PBIP/TMDL report |
| `Saudi_Ecommerce.Report/` and `Saudi_Ecommerce.SemanticModel/` | Report assets, semantic model, relationships and DAX |
| [Dashboard screenshots](screenshots/) | Visual previews of all six report pages |
| [SQL](mysql/) | Schema, loading, quality checks, analysis and reporting views |
| [Python](python/) | Data generation, MySQL loading, offline checks and aggregates |
| [Analysis outputs](analysis/) | CSV and JSON aggregates used for documented findings |
| [Data dictionary and samples](data/) | Entity definitions and five synthetic sample datasets |
| [Scenario workbook](excel/Business_Impact_Scenarios.xlsx) | Assumption-driven business-impact scenarios, **not achieved results** |
| [Setup and validation](docs/SETUP.md) | Reproduction instructions and validation checklist |

## Reproduce the analysis

The full dataset contains **1,964,000 simulated records**: 160,000 customers, 4,000 products, 400,000 orders, 1,000,000 order items and 400,000 deliveries. Large raw CSVs and local databases are excluded from GitHub.

```bash
pip install -r requirements.txt
python python/generate_synthetic_data.py
python python/validate_dataset.py
```

Create the MySQL database using `mysql/01_schema.sql`, then run `python python/load_mysql.py --host localhost --user root`. Open `Saudi_Ecommerce.pbip` in Power BI Desktop, configure the MySQL source and refresh. See [full setup instructions](docs/SETUP.md).

**Re-run caution:** Move or delete the previously generated `data/saudi_ecommerce.sqlite` file before regenerating; the generator creates tables from scratch.

## Methodology and limitations

- **Delivered sales** sum order totals for orders marked `Delivered`; this is a case-study convention, not formal revenue recognition.
- **Delivered AOV** = delivered sales / delivered orders. It differs from sales / all orders.
- **Late delivery %** = delivered shipments with actual days exceeding promised days / completed deliveries.
- **Category gross item sales** are not net sales; estimated product margin is not net profit.
- The 2022–2025 trajectory and operational distributions are **designed into the generator**. These are analytical practice signals, not evidence about real Saudi consumers, merchants or logistics providers.
- Committed KPI extracts are snapshots. Recompute and reconcile against regenerated data before treating them as independently verified.
- The Power BI report still requires local opening, refresh and end-to-end validation. See [validation checklist](docs/VALIDATION_CHECKLIST.md).

*Independent business analytics portfolio project. All customer and operational data are fictional.*
