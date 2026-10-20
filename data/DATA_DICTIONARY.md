# Data dictionary and grain

All data is fictional and seeded (`20261020`). SAR values are modeled; not actual Saudi transactions.

- **customers** (160,000): one row per customer. `customer_id` PK; `city`, `region`, `signup_date`, `customer_segment`.
- **products** (4,000): one row per SKU. `product_id` PK; `category`, `subcategory`, `unit_price_sar`, `unit_cost_sar`.
- **orders** (400,000): one row per order. `order_id` PK, `customer_id` FK, `order_date`, `order_status`, `payment_method`, `channel`, `discount_sar`, `shipping_fee_sar`, `order_total_sar`.
- **order_items** (1,000,000): one row per order line. `order_item_id` PK, `order_id` FK, `product_id` FK, `quantity`, `unit_price_sar`, `unit_cost_sar`, `line_revenue_sar`.
- **deliveries** (400,000): one row per order. `delivery_id` PK, `order_id` unique FK, `delivery_partner`, `warehouse_city`, `promised_days`, `actual_days`, `delivery_status`, `delivery_cost_sar`, `customer_rating`.

Relationships: `customers 1:N orders 1:N order_items N:1 products`, and `orders 1:1 deliveries`.

**Reconciliation:** `orders.order_total_sar = SUM(order_items.line_revenue_sar) - orders.discount_sar + orders.shipping_fee_sar` (tolerance SAR 0.01). `line_revenue_sar = quantity * unit_price_sar`.

**KPI rules:** Realized delivered sales = order totals with `order_status='Delivered'`. Cancelled, returned and in-transit orders are excluded from that metric. This is a simplified accounting convention for the case study, not a formal revenue-recognition policy. Late delivery = `actual_days > promised_days`, among delivered shipments only. Pre-discount item contribution = gross item sales minus modeled item costs, before allocating discounts, delivery cost or overhead. `customer_segment` is a synthetic label; validate against observed behavior before using it for targeting.

**Limitation:** The generator's 2022–2025 growth trend is designed, not inferred from the Saudi market. Synthetic partner comparisons may be nearly identical by construction, and city-level variation is not evidence of real market demand.
