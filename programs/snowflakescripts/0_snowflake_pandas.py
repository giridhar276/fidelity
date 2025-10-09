

# snowflake_pandas_rw_demo.py
# pip install snowflake-connector-python pandas

import snowflake.connector as sf
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
from getpass import getpass

ACCOUNT   = "ZRINJJH-KF54576"
USER      = "GIRIDHAR276"
ROLE      = "ACCOUNTADMIN"

WAREHOUSE = "MY_WH"
DATABASE  = "MY_DB"
SCHEMA    = "PUBLIC"
TABLE     = "DEMO_PEOPLE"

#PASSWORD = getpass("Enter your Snowflake password: ")
PASSWORD = "Nolimits@12345"
conn = sf.connect(
    account=ACCOUNT,
    user=USER,
    password=PASSWORD,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA,
    role=ROLE,
)

# sample DataFrame
pdf = pd.DataFrame({
    "ID":   [1, 2, 3],
    "NAME": ["A", "B", "C"]
})

with conn.cursor() as cur:
    # create or replace table with matching columns
    cur.execute(f"CREATE OR REPLACE TABLE {TABLE} (ID NUMBER, NAME STRING);")

# write pandas → Snowflake
ok, nchunks, nrows, _ = write_pandas(conn, pdf, TABLE)
print(f"write_pandas ok={ok}, rows_written={nrows}")

# read back with pandas
out = pd.read_sql(f"SELECT * FROM {TABLE} ORDER BY ID", conn)
print(out)

conn.close()
print("Pandas write/read demo complete.")
