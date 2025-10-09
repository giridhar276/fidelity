# 3_read_table_to_csv_pandas.py
# pip install snowflake-connector-python pandas
import pandas as pd
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

df = pd.read_sql(f"SELECT * FROM {TABLE}", conn)
df.to_csv(OUT_CSV, index=False)
print(f"Wrote {len(df)} rows to {OUT_CSV}")
conn.close()
