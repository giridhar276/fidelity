

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# --- config ---
user = "root"
password = "admin@123"
host = "localhost"
port = 3306
database = "empdb1"
table_name = "employee"
out_csv = "employee_out1.csv"
# --------------

# Build engine safely
url = URL.create(
    drivername="mysql+pymysql",
    username=user,
    password=password,
    host=host,
    port=port,
    database=database,
)
engine = create_engine(url, future=True)

# 1) Verify connection details
with engine.connect() as conn:
    print("Connected DB:", conn.execute(text("SELECT DATABASE()")).scalar_one())
    print("Server port  :", conn.execute(text("SELECT @@port")).scalar_one())

# 2) Read entire table (or switch to a custom query below)
with engine.connect() as conn:
    # Option A: whole table
    df = pd.read_sql(text(f"SELECT * FROM `{table_name}`"), conn)
    # Option B (custom): df = pd.read_sql(text(f"SELECT col1, col2 FROM `{table_name}` WHERE 1"), conn)

print("Fetched shape:", df.shape)

# 3) Write to CSV
df.to_csv(out_csv, index=False)
print(f"Exported {len(df)} rows to {out_csv}.")
