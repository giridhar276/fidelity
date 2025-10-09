# 1_create_table_pandas.py
# pip install snowflake-connector-python
import snowflake.connector as sf
from getpass import getpass

ACCOUNT   = "ZRINJJH-KF54576"
USER      = "GIRIDHAR276"
ROLE      = "ACCOUNTADMIN"
WAREHOUSE = "MY_WH"
DATABASE  = "MY_DB"
SCHEMA    = "PUBLIC"
TABLE     = "EMPLOYEE"

#PASSWORD = getpass("Snowflake password: ")
PASSWORD = "Nolimits@12345"

ddl = f"""
CREATE TABLE IF NOT EXISTS {TABLE} (
  AGE NUMBER,
  WORKCLASS STRING,
  FNLWGT NUMBER,
  EDUCATION STRING,
  EDUCATIONAL_NUM NUMBER,
  MARITAL_STATUS STRING,
  OCCUPATION STRING,
  RELATIONSHIP STRING,
  RACE STRING,
  GENDER STRING,
  CAPITAL_GAIN NUMBER,
  CAPITAL_LOSS NUMBER,
  HOURS_PER_WEEK NUMBER,
  NATIVE_COUNTRY STRING,
  INCOME STRING
);
"""

conn = sf.connect(account=ACCOUNT, user=USER, password=PASSWORD, role=ROLE)
with conn.cursor() as cur:
    cur.execute(f"USE WAREHOUSE {WAREHOUSE}")
    cur.execute(f"USE DATABASE {DATABASE}")
    cur.execute(f"USE SCHEMA {SCHEMA}")
    cur.execute(ddl)
    print(f"Table {TABLE} ready.")
conn.close()
