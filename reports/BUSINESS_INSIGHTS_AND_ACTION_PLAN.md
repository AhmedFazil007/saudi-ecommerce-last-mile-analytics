# Business Insights & Management Action Plan

**Saudi E-Commerce & Last-Mile Delivery Analytics | Synthetic 2022–2025 case study**

> **Scope:** Findings are derived from committed synthetic aggregate outputs. They demonstrate business reasoning and recommended tests—not verified market trends, causal effects, realized savings, or performance of actual Saudi companies.

## Executive decision

**Do not optimize for order count alone.** The 2025 simulation generates 31.8% more orders but only 2.1% more delivered sales than 2024. A 20.1% decline in delivered AOV indicates that additional transactions do not carry comparable sales value. Prioritize an explanation of the basket-value change, then test margin-aware commercial interventions and operational reliability improvements.

## Evidence → interpretation → decision

| Evidence from project files | What it suggests | What management should do | What would confirm success |
|---|---|---|---|
| Orders 110,000 → 145,000 (+31.8%); delivered sales SAR 250.41M → 255.63M (+2.1%) in 2024–25 | Transaction growth outpaces sales growth | Decompose sales into delivered orders × AOV; segment by channel, basket size and category | Higher contribution per order without adverse return or cancellation effects |
| Delivered AOV SAR 2,474.03 → 1,976.05 (−20.1%) | Lower sales per delivered order | Check item-count and price/mix changes; run controlled bundle/cross-sell pilots | Incremental contribution and stable customer satisfaction |
| Approximately 29.9% late deliveries; partner rates 29.72–30.30% | Reliability is a broad simulated issue; differences between partners are small | Analyze warehouse × destination × promise length; pilot proactive delay alerts and realistic delivery promises | Lower late %, better rating and lower support burden |
| Riyadh, Jeddah, Dammam together represent ~59.1% of delivered sales | These locations are the largest modeled revenue pools | Prioritize operational diagnostics and cohort comparisons in these locations | Better service and contribution after fulfillment, not simply more orders |
| Mobile App contributes ~61.8% of delivered sales | App is the largest modeled sales channel | Study app basket value, checkout abandonment and retention versus other channels | Improved incremental contribution and retention |
| Electronics + Home & Kitchen account for ~70.1% of delivered gross item sales | Category sales concentration warrants commercial scrutiny | Compare category margins **after** discounts, returns and delivery expense | Contribution improvement with acceptable inventory and service risk |
| 2025 cancellation rate 4.90%; 2025 return rate 2.90% | Some transactions do not become delivered sales | Break down by fulfillment reason, payment method and cohort | Lower preventable losses without hiding genuine customer needs |

### 1. Sales quality: the headline priority

**Evidence:** Annual delivered sales are SAR 163.72M (2022), SAR 229.36M (2023), SAR 250.41M (2024), SAR 255.63M (2025). Delivered AOV is SAR 2,965.82, SAR 2,932.70, SAR 2,474.03 and SAR 1,976.05 respectively.

**Interpretation:** The 2025 order-volume increase did not produce proportionate delivered-sales growth. **Critical caveat:** The synthetic generator deliberately assigns three items to the first 200,000 orders and two items to the remaining 200,000, making the order-value shift partly a construction of the data. This is a *designed diagnostic case*, not evidence of organic customer basket deterioration.

**Actions to test:**
1. Build a delivered-sales bridge: delivered order count × delivered AOV, with discount, item count and category-mix breakouts.
2. Separate repeat buyers, first-time buyers and channels; check whether AOV decline remains within like-for-like cohorts.
3. Trial bundles, cross-sell or free-shipping thresholds on a limited, controlled segment. Avoid incentives that increase revenue but reduce contribution.

**Measure:** Delivered AOV, units per order, average discount/order, gross item margin, contribution after delivery, and repeat purchase within a defined period.

### 2. Delivery: target the process, not a carrier label

**Evidence:** Carrier late percentages in `analysis/delivery_partner_kpis.csv` range from 29.72% (SPL) to 30.30% (Naqel). The spread is only **0.58 percentage points**.

**Interpretation:** The synthetic differences are too small and uncontrolled to justify declaring one carrier superior. Promise length, origin and destination may confound comparisons.

**Actions to test:**
1. Produce a shipment-level late-rate matrix by warehouse, city, promised days and carrier.
2. Audit whether promised delivery windows reflect actual capacity.
3. Pilot preemptive exception alerts and compare matched shipments or randomized cohorts.

**Measure:** Late delivery %, p90 actual delivery days, customer rating, cost per completed delivery, exception resolution time.

### 3. Customer and channel economics

**Evidence:** Mobile App delivered sales = **SAR 555.56M** out of approximately **SAR 899.11M** across all channels, or **61.8%**. This is a multi-year figure, not 2025 alone.

**Interpretation:** The app is the largest modeled channel, but volume does not prove profitability or superior retention.

**Actions to test:** Compare delivered AOV, cancellation, return, discount and contribution by channel and customer cohort; target retention experiments only where incremental value is demonstrated.

**Measure:** 30/60/90-day repeat rate, delivered AOV by cohort, contribution/customer and cancellation by channel.

### 4. Geography: focus diagnostics where activity is concentrated

**Evidence:** Multi-year delivered sales: Riyadh **SAR 262.06M**, Jeddah **SAR 179.56M**, Dammam **SAR 89.85M**. Combined: approximately **59.1%** of all modeled delivered sales.

**Interpretation:** These are the largest simulated sales pools, not independently measured Saudi market opportunities.

**Actions to test:** Investigate city-specific fulfillment cost, delivery time, product mix and return behavior. Pilot improvements in high-volume operational segments before expanding geographically.

**Measure:** Contribution after fulfillment per order, delivery reliability, cancellation/return rates and retention by city.

### 5. Product mix: move from revenue to contribution

**Evidence:** Electronics gross delivered item sales = **SAR 444.29M**; Home & Kitchen = **SAR 222.06M**. Combined share of all modeled gross delivered item sales is approximately **70.1%**.

**Interpretation:** High gross sales do not automatically mean high net contribution. The category file excludes order-level discounts, shipping, delivery costs and overhead.

**Actions to test:** Allocate discounts and fulfillment costs with an explicit, documented method. Compare categories on contribution and return-adjusted economics before adjusting spend or inventory.

**Measure:** Item margin %, discount-adjusted margin, fulfillment cost per order, return-adjusted contribution.

## 30–60–90 day execution roadmap

| Stage | Owner (proposed) | Deliverable | Go/no-go condition |
|---|---|---|---|
| Days 1–30: Diagnose | Commercial analytics + operations | Validated sales/AOV bridge, cohort cuts, delivery SLA baseline | Source-to-dashboard reconciliation and agreed KPI definitions |
| Days 31–60: Pilot | Merchandising + fulfillment | Limited basket-value and delivery-alert experiments | Clean control comparison, adequate sample, no deterioration in contribution or service |
| Days 61–90: Decide | Finance + commercial leadership | Experiment readout and prioritization matrix | Scale only when net incremental benefit and operational feasibility are credible |

## Questions for management

1. Is the fall in AOV due to basket size, pricing, discounts, mix, or a reporting-definition change?
2. Are new orders profitable after discounts, returns, delivery and customer-support costs?
3. Which service failures are preventable, and what would it cost to prevent them?
4. Are repeat customers generating higher *contribution* or merely more transactions?
5. Which intervention has the highest evidence-backed return after implementation costs?

## Evidence and guardrails

**Data files:** `analysis/annual_kpis.csv`, `analysis/aggregates.json`, `analysis/channel_kpis.csv`, `analysis/city_kpis.csv`, `analysis/category_kpis.csv`, `analysis/delivery_partner_kpis.csv`, `analysis/quality_checks.csv`.

**Definitions:** `data/DATA_DICTIONARY.md`. **Methodology and reproducibility:** `docs/SETUP.md`. **Scenario model:** `excel/Business_Impact_Scenarios.xlsx` (hypothetical assumptions only).

The aggregate files are committed snapshots and were not freshly recalculated in this document. Verify results against a regenerated dataset and Power BI before claiming full end-to-end validation. None of the proposed interventions has been tested for causal impact. All figures are fictional.
