# What I learned from the Saudi E-Commerce Analytics Project

*My business observations and recommendations | Synthetic dataset, 2022–2025*

I built this project to practice looking at a business as a whole, rather than treating sales, customers and delivery operations as separate reports. After working through the figures, I found a few areas I would investigate if I were reviewing this business's performance.

The dataset is fictional. My conclusions describe the patterns in this case study, not real Saudi market conditions, and the recommendations below are ideas to test rather than improvements I have already delivered.

## 1. More orders didn't mean much more sales

This was the finding that interested me most.

| Metric | 2024 | 2025 |
|---|---:|---:|
| Orders | 110,000 | 145,000 |
| Delivered sales | SAR 250.41M | SAR 255.63M |
| Average delivered order value | SAR 2,474 | SAR 1,976 |

Orders rose **31.8%**, but delivered sales increased only **2.1%**. Average delivered order value dropped by **20.1%**.

If I looked only at order count, I might have called this strong growth. Looking at the sales figures changed my view: the business was processing more transactions without getting a comparable increase in delivered sales.

I would first check whether the change came from the number of items per order, the types of products sold, pricing or discounts. One important limitation is that the synthetic generator deliberately uses fewer items per order in the later records. That means part of this pattern comes from how I constructed the case-study data, not from observed customer behavior.

**My suggestion:** Understand the drop in basket value before increasing acquisition spending. If the breakdown supports it, try product bundles or cross-selling on a small customer group, then compare contribution per order—not only sales.

## 2. Late deliveries deserve attention, but blaming a carrier would be premature

About **29.9%** of completed deliveries were late in the simulated dataset. When I compared delivery partners, their late rates were close: **29.72% to 30.30%**.

I don't think that is enough to label one partner as good or bad. The difference could be related to the delivery promise, warehouse, destination or simply the way the synthetic data was generated.

**My suggestion:** Break down late deliveries by warehouse, city and promised delivery days. I would test more realistic delivery estimates and alerts for orders at risk of delay, then see whether the late rate improves without making delivery too expensive.

## 3. A few cities and channels account for much of the sales

Across the four-year dataset, **Riyadh, Jeddah and Dammam accounted for about 59.1% of delivered sales**. The **mobile app contributed around 61.8%**.

That tells me where the biggest simulated sales volumes are. It doesn't tell me which customers are most profitable, whether the app has the best retention, or where a real Saudi retailer should expand.

**My suggestion:** Start by comparing basket value, repeat orders, returns and delivery costs in the largest cities and channels. I would rather understand these differences before recommending expansion or additional marketing spend.

## 4. The best-selling categories may not be the most profitable

Electronics and Home & Kitchen represented approximately **70.1% of gross item sales for delivered orders**.

That sounds promising, but the gross item sales measure is calculated before order-level discounts and fulfillment expenses. I would not use it on its own to decide where to invest.

**My suggestion:** Estimate contribution after allocating discounts and delivery costs, document the allocation method and compare categories on the same basis. Only then would I consider changes to promotions or inventory priorities.

## 5. What I would look into next

If I continued this as a business analysis assignment, I would focus on three practical questions:

1. **Why is average order value falling?** I would compare items per order, discount rates, category mix and customer groups.
2. **Where are deliveries going wrong?** I would check which routes and promised delivery windows have the highest late rates.
3. **Which sales are worth growing?** I would look beyond revenue and calculate a more complete contribution measure after discounts and fulfillment costs.

I would start with the existing SQL queries and Power BI report, confirm that the measures reconcile, and then test possible improvements on a limited group before recommending wider changes.

## What this project taught me

The most useful lesson for me was that a dashboard can show growth while hiding a more complicated business picture. An increase in orders looked positive at first, but it became less convincing when I compared it with sales and average order value.

It also reminded me not to treat every difference as an explanation. The dataset is synthetic, and some of its patterns were intentionally built into the generator. I can use those patterns to practice analysis and decision-making, but I cannot claim they prove what happens in a real business.

### Files behind these observations

- [Annual KPIs](../analysis/annual_kpis.csv)
- [Delivery partner KPIs](../analysis/delivery_partner_kpis.csv)
- [City KPIs](../analysis/city_kpis.csv)
- [Channel KPIs](../analysis/channel_kpis.csv)
- [Category KPIs](../analysis/category_kpis.csv)
- [Data dictionary](../data/DATA_DICTIONARY.md)
- [Business impact scenario workbook](../excel/Business_Impact_Scenarios.xlsx)

The KPI files are saved snapshots. I have not claimed a fresh end-to-end rerun or Power BI refresh as part of this write-up. The Excel scenarios are assumptions, not realized results.
