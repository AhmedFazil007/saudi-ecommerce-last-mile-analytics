"""Verify source CSV structure and relationships using a built-in SQLite database.
The database is used ONLY for portable offline validation; project SQL runs on MySQL.
"""
import sqlite3,csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
con=sqlite3.connect(root/'data/saudi_ecommerce.sqlite')
expected={'customers':160000,'products':4000,'orders':400000,'order_items':1000000,'deliveries':400000}
for table,n in expected.items():
 actual=con.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
 assert actual==n,(table,actual,n)
 print(f'PASS {table}: {actual:,} rows')
checks={
 'orphan_orders':'SELECT COUNT(*) FROM orders o LEFT JOIN customers c ON c.customer_id=o.customer_id WHERE c.customer_id IS NULL',
 'orphan_items':'SELECT COUNT(*) FROM order_items i LEFT JOIN orders o ON o.order_id=i.order_id WHERE o.order_id IS NULL',
 'orphan_products':'SELECT COUNT(*) FROM order_items i LEFT JOIN products p ON p.product_id=i.product_id WHERE p.product_id IS NULL',
 'duplicate_delivery_orders':'SELECT COUNT(*) FROM (SELECT order_id FROM deliveries GROUP BY order_id HAVING COUNT(*)>1)',
 'reconciliation':'SELECT COUNT(*) FROM orders o JOIN (SELECT order_id,SUM(line_revenue_sar) gross FROM order_items GROUP BY order_id) x ON x.order_id=o.order_id WHERE ABS(o.order_total_sar-(x.gross-o.discount_sar+o.shipping_fee_sar))>0.01'}
for name,sql in checks.items():
 n=con.execute(sql).fetchone()[0];assert n==0,(name,n);print(f'PASS {name}: 0 issues')
print('All tests passed')
