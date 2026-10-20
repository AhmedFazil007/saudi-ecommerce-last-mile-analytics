import csv,random,sqlite3,datetime,os,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'data'/'raw'
P.mkdir(parents=True,exist_ok=True)
DB=ROOT/'data'/'saudi_ecommerce.sqlite'
R=random.Random(20261020)
N_CUSTOMERS=160000; N_PRODUCTS=4000; N_ORDERS=400000
cities=['Riyadh','Jeddah','Dammam','Khobar','Makkah','Madinah','Tabuk','Abha','Taif','Jubail','Al Ahsa','Buraydah']
weights=[29,20,10,7,8,6,4,4,4,3,3,2]
regions=['Riyadh','Makkah','Eastern','Eastern','Makkah','Madinah','Tabuk','Asir','Makkah','Eastern','Eastern','Qassim']
cat=['Electronics','Fashion','Beauty','Home & Kitchen','Groceries','Sports','Automotive','Books & Stationery']
catw=[17,22,12,15,17,8,5,4]
price_ranges=[(80,4200),(25,700),(18,500),(35,2300),(7,250),(25,1300),(25,1500),(10,350)]
orders_by_year={2022:60000,2023:85000,2024:110000,2025:145000}
conn=sqlite3.connect(DB);c=conn.cursor()
c.executescript('''PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF;
CREATE TABLE customers(customer_id INTEGER PRIMARY KEY,city TEXT NOT NULL,region TEXT NOT NULL,signup_date TEXT NOT NULL,customer_segment TEXT NOT NULL);
CREATE TABLE products(product_id INTEGER PRIMARY KEY,category TEXT NOT NULL,subcategory TEXT NOT NULL,unit_price_sar REAL NOT NULL,unit_cost_sar REAL NOT NULL);
CREATE TABLE orders(order_id INTEGER PRIMARY KEY,customer_id INTEGER NOT NULL,order_date TEXT NOT NULL,order_status TEXT NOT NULL,payment_method TEXT NOT NULL,channel TEXT NOT NULL,discount_sar REAL NOT NULL,shipping_fee_sar REAL NOT NULL,order_total_sar REAL NOT NULL,FOREIGN KEY(customer_id) REFERENCES customers(customer_id));
CREATE TABLE order_items(order_item_id INTEGER PRIMARY KEY,order_id INTEGER NOT NULL,product_id INTEGER NOT NULL,quantity INTEGER NOT NULL,unit_price_sar REAL NOT NULL,unit_cost_sar REAL NOT NULL,line_revenue_sar REAL NOT NULL,FOREIGN KEY(order_id) REFERENCES orders(order_id),FOREIGN KEY(product_id) REFERENCES products(product_id));
CREATE TABLE deliveries(delivery_id INTEGER PRIMARY KEY,order_id INTEGER NOT NULL UNIQUE,delivery_partner TEXT NOT NULL,warehouse_city TEXT NOT NULL,promised_days INTEGER NOT NULL,actual_days INTEGER,delivery_status TEXT NOT NULL,delivery_cost_sar REAL NOT NULL,customer_rating INTEGER,FOREIGN KEY(order_id) REFERENCES orders(order_id));
''')
files={}
for table,head in {
'customers':['customer_id','city','region','signup_date','customer_segment'],
'products':['product_id','category','subcategory','unit_price_sar','unit_cost_sar'],
'orders':['order_id','customer_id','order_date','order_status','payment_method','channel','discount_sar','shipping_fee_sar','order_total_sar'],
'order_items':['order_item_id','order_id','product_id','quantity','unit_price_sar','unit_cost_sar','line_revenue_sar'],
'deliveries':['delivery_id','order_id','delivery_partner','warehouse_city','promised_days','actual_days','delivery_status','delivery_cost_sar','customer_rating']}.items():
 f=open(P/(table+'.csv'),'w',newline='',encoding='utf-8');w=csv.writer(f);w.writerow(head);files[table]=(f,w)
def write(table,rows):
 files[table][1].writerows(rows)
 c.executemany('INSERT INTO '+table+' VALUES ('+','.join(['?']*len(rows[0]))+')',rows)
for start in range(1,N_CUSTOMERS+1,10000):
 rows=[]
 for i in range(start,min(start+10000,N_CUSTOMERS+1)):
  city=R.choices(cities,weights)[0];date=datetime.date(2021,1,1)+datetime.timedelta(days=R.randrange(365));seg=R.choices(['New','Returning','Loyal','Business'],[38,37,20,5])[0]
  rows.append((i,city,regions[cities.index(city)],str(date),seg))
 write('customers',rows)
products=[]
for i in range(1,N_PRODUCTS+1):
 ix=R.choices(range(len(cat)),catw)[0];lo,hi=price_ranges[ix];price=round(R.uniform(lo,hi),2);cost=round(price*R.uniform(.52,.83),2)
 products.append((i,cat[ix],f'{cat[ix]} - Segment {1+i%8}',price,cost))
write('products',products)
products_by_id={p[0]:p for p in products}
startid=1;item_id=1;total_sales=0;status_counts=Counter();year_totals=Counter()
for year,n in orders_by_year.items():
 startdate=datetime.date(year,1,1);days=(datetime.date(year+1,1,1)-startdate).days
 for batchstart in range(0,n,5000):
  orderrows=[];itemrows=[];deliveryrows=[]
  for j in range(batchstart,min(batchstart+5000,n)):
   oid=startid;startid+=1;customer=R.randint(1,N_CUSTOMERS);day=startdate+datetime.timedelta(days=R.randrange(days));date=str(day)
   # 3 items for first 200k orders, 2 for remaining 200k = exactly 1M items
   nitems=3 if oid<=200000 else 2
   subtotal=0.0
   for _ in range(nitems):
    pid=R.randint(1,N_PRODUCTS);prod=products_by_id[pid];qty=R.choices([1,2,3,4],[72,19,7,2])[0];line=round(prod[3]*qty,2);subtotal+=line
    itemrows.append((item_id,oid,pid,qty,prod[3],prod[4],line));item_id+=1
   subtotal=round(subtotal,2);discount=round(subtotal*R.choices([0,.05,.1,.15,.2],[45,22,18,10,5])[0],2)
   shipping=0.0 if subtotal>=250 else R.choice([12.0,15.0,20.0]);total=round(subtotal-discount+shipping,2)
   status=R.choices(['Delivered','Cancelled','Returned','In Transit'],[89,5,3,3] if year==2025 else [92,5,3,0])[0]
   pay=R.choices(['Mada','Apple Pay','Credit Card','Cash on Delivery','STC Pay'],[40,20,22,10,8])[0]
   channel=R.choices(['Mobile App','Website','Marketplace'],[62,29,9])[0]
   orderrows.append((oid,customer,date,status,pay,channel,discount,shipping,total))
   promise=R.choice([1,2,3,4,5]);actual=max(1,promise+R.choices([-1,0,1,2,3],[12,58,17,9,4])[0]) if status in ('Delivered','Returned') else None
   delivery_status={'Delivered':'Delivered','Cancelled':'Cancelled','Returned':'Returned','In Transit':'In Transit'}[status]
   deliveryrows.append((oid,oid,R.choice(['SPL','Aramex','SMSA','Naqel','In-house']),R.choice(['Riyadh','Jeddah','Dammam']),promise,actual,delivery_status,round(R.uniform(9,42),2) if status!='Cancelled' else 0.0,R.choices([1,2,3,4,5],[4,5,13,33,45])[0] if status in ('Delivered','Returned') else None))
   total_sales+=total;status_counts[status]+=1;year_totals[year]+=1
  write('orders',orderrows);write('order_items',itemrows);write('deliveries',deliveryrows)
  conn.commit()
conn.executescript('''CREATE INDEX idx_orders_customer ON orders(customer_id);CREATE INDEX idx_orders_date ON orders(order_date);CREATE INDEX idx_items_order ON order_items(order_id);CREATE INDEX idx_items_product ON order_items(product_id);CREATE INDEX idx_deliveries_order ON deliveries(order_id);''')
conn.commit()
checks={t:c.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in files}
assert checks=={'customers':160000,'products':4000,'orders':400000,'order_items':1000000,'deliveries':400000},checks
assert c.execute('SELECT COUNT(*) FROM order_items i LEFT JOIN orders o ON i.order_id=o.order_id WHERE o.order_id IS NULL').fetchone()[0]==0
assert c.execute('SELECT COUNT(*) FROM deliveries d LEFT JOIN orders o ON d.order_id=o.order_id WHERE o.order_id IS NULL').fetchone()[0]==0
summary={'dataset':'100% synthetic; fictional businesses, transactions, customers and operations','tables':checks,'total_rows':sum(checks.values()),'yearly_orders':dict(year_totals),'order_status_counts':dict(status_counts),'gross_order_value_sar_including_cancelled_and_returned':round(total_sales,2),'seed':20261020}
(P/'dataset_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
for f,w in files.values():f.close()
conn.close()
print(json.dumps(summary,indent=2))
