# 2_insert_from_csv_pandas.py
# pip install snowflake-connector-python pandas
import pandas as pd
import snowflake.connector as sf
from snowflake.connector.pandas_tools import write_pandas
from getpass import getpass

ACCOUNT   = "ZRINJJH-KF54576"
USER      = "GIRIDHAR276"
ROLE      = "ACCOUNTADMIN"
WAREHOUSE = "MY_WH"
DATABASE  = "MY_DB"
SCHEMA    = "PUBLIC"
TABLE     = "EMPLOYEE"

CSV_PATH = "employee.csv"
#PASSWORD = getpass("Snowflake password: ")
PASSWORD = "Nolimits@12345"
# read csv and normalize column names to match table
df = pd.read_csv(CSV_PATH)
df.columns = [c.strip().upper().replace("-", "_").replace(" ", "_") for c in df.columns]

conn = sf.connect(account=ACCOUNT, user=USER, password=PASSWORD,
                  warehouse=WAREHOUSE, database=DATABASE, schema=SCHEMA, role=ROLE)

ok, nchunks, nrows, _ = write_pandas(conn, df, TABLE)
print(f"Inserted rows: {nrows}, ok={ok}")
conn.close()
