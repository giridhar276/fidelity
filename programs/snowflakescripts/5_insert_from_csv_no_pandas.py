# 5_insert_from_csv_no_pandas.py
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

CSV_PATH = "employee.csv"
#PASSWORD = getpass("Snowflake password: ")
PASSWORD = "Nolimits@12345"

# Helper: safe int conversion
def to_int_or_none(x):
    x = (x or "").strip()
    try:
        return int(float(x))
    except ValueError:
        return None

# Define the column order we will insert
COLS = ["AGE","WORKCLASS","FNLWGT","EDUCATION","EDUCATIONAL_NUM","MARITAL_STATUS",
        "OCCUPATION","RELATIONSHIP","RACE","GENDER","CAPITAL_GAIN","CAPITAL_LOSS",
        "HOURS_PER_WEEK","NATIVE_COUNTRY","INCOME"]

NUMERIC = {"AGE","FNLWGT","EDUCATIONAL_NUM","CAPITAL_GAIN","CAPITAL_LOSS","HOURS_PER_WEEK"}

conn = sf.connect(account=ACCOUNT, user=USER, password=PASSWORD,
                  warehouse=WAREHOUSE, database=DATABASE, schema=SCHEMA, role=ROLE)

with conn.cursor() as cur, open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # Normalize CSV header keys to uppercase with underscores
    def norm(h): return h.strip().upper().replace("-", "_").replace(" ", "_")
    headers_map = {norm(h): h for h in reader.fieldnames}

    placeholders = ",".join(["%s"] * len(COLS))
    sql = f"INSERT INTO {TABLE} ({','.join(COLS)}) VALUES ({placeholders})"

    rows = []
    for r in reader:
        vals = []
        for c in COLS:
            src = headers_map.get(c)
            val = r.get(src, "") if src else ""
            if c in NUMERIC:
                vals.append(to_int_or_none(val))
            else:
                vals.append(val if val != "" else None)
        rows.append(tuple(vals))

    if rows:
        cur.executemany(sql, rows)
    print(f"Inserted {len(rows)} rows.")

conn.close()
