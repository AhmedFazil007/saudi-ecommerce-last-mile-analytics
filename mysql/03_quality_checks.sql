USE saudi_ecommerce;
SELECT 'customers' table_name, COUNT(*) rows_found FROM customers UNION ALL SELECT 'products',COUNT(*) FROM products UNION ALL SELECT 'orders',COUNT(*) FROM orders UNION ALL SELECT 'order_items',COUNT(*) FROM order_items UNION ALL SELECT 'deliveries',COUNT(*) FROM deliveries;
-- Expected: 160000, 4000, 400000, 1000000, 400000.
SELECT COUNT(*) orphan_order_customers FROM orders o LEFT JOIN customers c ON c.customer_id=o.customer_id WHERE c.customer_id IS NULL;
SELECT COUNT(*) orphan_order_items FROM order_items i LEFT JOIN orders o ON o.order_id=i.order_id WHERE o.order_id IS NULL;
SELECT COUNT(*) orphan_products FROM order_items i LEFT JOIN products p ON p.product_id=i.product_id WHERE p.product_id IS NULL;
SELECT COUNT(*) duplicate_delivery_order_ids FROM (SELECT order_id FROM deliveries GROUP BY order_id HAVING COUNT(*)>1) x;
SELECT COUNT(*) order_total_mismatches FROM orders o JOIN (SELECT order_id,SUM(line_revenue_sar) gross FROM order_items GROUP BY order_id) i ON i.order_id=o.order_id WHERE ABS(o.order_total_sar-(i.gross-o.discount_sar+o.shipping_fee_sar))>0.01;
