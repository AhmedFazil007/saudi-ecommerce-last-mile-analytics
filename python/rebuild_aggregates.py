"""Rebuild key aggregate CSV files from the bundled offline SQLite copy.
The portfolio's main SQL scripts are written for MySQL Workbench.
"""
import sqlite3,csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
c=sqlite3.connect(root/'data/saudi_ecommerce.sqlite');c.row_factory=sqlite3.Row
queries={
 'annual_kpis.csv': "SELECT substr(order_date,1,4) year,count(*) orders,count(distinct customer_id) active_customers,round(sum(case when order_status='Delivered' then order_total_sar else 0 end),2) delivered_sales_sar,round(avg(case when order_status='Delivered' then order_total_sar end),2) delivered_aov_sar,round(100.0*sum(order_status='Cancelled')/count(*),2) cancellation_pct FROM orders GROUP BY 1 ORDER BY 1",
 'city_kpis.csv': "SELECT c.city,count(*) orders,round(sum(case when o.order_status='Delivered' then o.order_total_sar else 0 end),2) delivered_sales_sar FROM orders o JOIN customers c ON c.customer_id=o.customer_id GROUP BY 1 ORDER BY delivered_sales_sar DESC",
 'delivery_partner_kpis.csv': "SELECT delivery_partner,sum(delivery_status='Delivered') delivered_orders,round(100.0*sum(delivery_status='Delivered' and actual_days>promised_days)/nullif(sum(delivery_status='Delivered'),0),2) late_delivery_pct FROM deliveries GROUP BY 1 ORDER BY late_delivery_pct DESC"}
for filename,sql in queries.items():
 rows=[dict(r) for r in c.execute(sql)]
 with (root/'analysis'/filename).open('w',newline='',encoding='utf8') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
 print(filename,len(rows))
