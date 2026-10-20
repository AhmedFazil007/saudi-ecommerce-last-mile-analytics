"""Batch import the five source CSVs into MySQL 8. Run schema first in Workbench.
Usage: pip install mysql-connector-python
       python python/load_mysql.py --host localhost --user root
Password prompted securely. Re-running skips populated tables, avoiding duplicate keys.
"""
import argparse,csv,getpass
from pathlib import Path
import mysql.connector
p=argparse.ArgumentParser();p.add_argument('--host',default='localhost');p.add_argument('--port',type=int,default=3306);p.add_argument('--user',default='root');p.add_argument('--database',default='saudi_ecommerce');p.add_argument('--batch-size',type=int,default=5000)
a=p.parse_args();conn=mysql.connector.connect(host=a.host,port=a.port,user=a.user,password=getpass.getpass('MySQL password: '),database=a.database,autocommit=False)
root=Path(__file__).resolve().parents[1]/'data/raw'
for name in ['customers','products','orders','order_items','deliveries']:
 cur=conn.cursor();cur.execute('SELECT COUNT(*) FROM `'+name+'`');existing=cur.fetchone()[0]
 if existing:
  print(f'{name}: already contains {existing:,} rows; skipping. Empty the table explicitly to reload.');cur.close();continue
 with (root/(name+'.csv')).open(encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f);fields=reader.fieldnames
  statement='INSERT INTO `'+name+'` ('+','.join('`'+x+'`' for x in fields)+') VALUES ('+','.join(['%s']*len(fields))+')'
  batch=[];count=0
  for row in reader:
   batch.append(tuple(None if value=='' else value for value in row.values()))
   if len(batch)>=a.batch_size:
    cur.executemany(statement,batch);conn.commit();count+=len(batch);batch=[]
  if batch:cur.executemany(statement,batch);conn.commit();count+=len(batch)
 print(f'{name}: imported {count:,} rows');cur.close()
conn.close()
