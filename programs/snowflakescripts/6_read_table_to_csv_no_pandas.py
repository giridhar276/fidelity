# 6_read_table_to_csv_no_pandas.py
# pip install snowflake-connector-python
import csv
import snowflake.connector as sf
from getpass import getpass

ACCOUNT   = "ZRINJJH-KF54576"
USER      = "GIRIDHAR276"
ROLE      = "ACCOUNTADMIN"
WAREHOUSE = "MY_WH"
DATABASE  = "MY_DB"
SCHEMA    = "PUBLIC"
TABLE     = "EMPLOYEE"

OUT_CSV = "employee_out.csv"
#PASSWORD = getpass("Snowflake password: ")
PASSWORD = "Nolimits@12345"

conn = sf.connect(account=ACCOUNT, user=USER, password=PASSWORD,
                  warehouse=WAREHOUSE, database=DATABASE, schema=SCHEMA, role=ROLE)

with conn.cursor() as cur:
    cur.execute(f"SELECT * FROM {TABLE}")
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    w.writerows(rows)

conn.close()
print(f"Wrote {len(rows)} rows to {OUT_CSV}")
