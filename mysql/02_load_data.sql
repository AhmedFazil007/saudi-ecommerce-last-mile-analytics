-- OPTION A: import with Python: python python/load_mysql.py --host localhost --user root
-- OPTION B: MySQL Workbench connection must allow LOCAL INFILE; replace full paths below.
-- Use forward slashes in Windows paths, e.g. C:/Users/.../customers.csv
USE saudi_ecommerce;
LOAD DATA LOCAL INFILE 'REPLACE_WITH_FULL_PATH/customers.csv' INTO TABLE customers
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES
(customer_id,city,region,signup_date,customer_segment);
LOAD DATA LOCAL INFILE 'REPLACE_WITH_FULL_PATH/products.csv' INTO TABLE products
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES
(product_id,category,subcategory,unit_price_sar,unit_cost_sar);
LOAD DATA LOCAL INFILE 'REPLACE_WITH_FULL_PATH/orders.csv' INTO TABLE orders
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES
(order_id,customer_id,order_date,order_status,payment_method,channel,discount_sar,shipping_fee_sar,order_total_sar);
LOAD DATA LOCAL INFILE 'REPLACE_WITH_FULL_PATH/order_items.csv' INTO TABLE order_items
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES
(order_item_id,order_id,product_id,quantity,unit_price_sar,unit_cost_sar,line_revenue_sar);
-- Empty numeric columns should be NULL; Python loader is recommended for this table.
LOAD DATA LOCAL INFILE 'REPLACE_WITH_FULL_PATH/deliveries.csv' INTO TABLE deliveries
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES
(delivery_id,order_id,delivery_partner,warehouse_city,promised_days,@actual_days,delivery_status,delivery_cost_sar,@customer_rating)
SET actual_days=NULLIF(TRIM(@actual_days),''),customer_rating=NULLIF(TRIM(@customer_rating),'');
