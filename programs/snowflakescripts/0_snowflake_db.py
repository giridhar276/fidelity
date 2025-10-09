

# snowflake_setup_and_smoketest.py
# pip install snowflake-connector-python

import snowflake.connector as sf
from getpass import getpass

ACCOUNT   = "ZRINJJH-KF54576"   # from your screenshot
USER      = "GIRIDHAR276"       # from your screenshot
ROLE      = "ACCOUNTADMIN"      # from your screenshot

# choose names you'd like to use
WAREHOUSE = "MY_WH"
DATABASE  = "MY_DB"
SCHEMA    = "PUBLIC"

PASSWORD = 'Nolimits@12345'

conn = sf.connect(
    account=ACCOUNT,       # do NOT include https:// or .snowflakecomputing.com here
    user=USER,
    password=PASSWORD,
    role=ROLE,
)

with conn.cursor() as cur:
    # Create/ensure objects
    cur.execute(f"""
        CREATE WAREHOUSE IF NOT EXISTS {WAREHOUSE}
          WITH WAREHOUSE_SIZE='XSMALL' AUTO_SUSPEND=60 AUTO_RESUME=TRUE;
    """)
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE};")
    cur.execute(f"USE WAREHOUSE {WAREHOUSE};")
    cur.execute(f"USE DATABASE {DATABASE};")
    cur.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA};")
    cur.execute(f"USE SCHEMA {SCHEMA};")

    # Show context + a quick version check
    cur.execute("SELECT CURRENT_REGION(), CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA(), CURRENT_VERSION();")
    print(cur.fetchone())

conn.close()
print("Setup & smoke test complete.")
