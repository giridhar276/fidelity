

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
csv_path = "employee.csv"
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

# 1) Load CSV and show basic info (ensure it’s not empty)
df = pd.read_csv(csv_path)
print("CSV shape:", df.shape)

# 2) Write to MySQL (replace or use 'append')
with engine.begin() as conn:  # explicit transactional begin->commit
    df.to_sql(table_name, con=conn, if_exists="replace", index=False, method="multi", chunksize=1000)

# 3) Verify: count rows, confirm DB/port in use, and peek few rows
with engine.connect() as conn:
    print("Connected DB:", conn.execute(text("SELECT DATABASE()")).scalar_one())
    print("Server port  :", conn.execute(text("SELECT @@port")).scalar_one())
    n = conn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`")).scalar_one()
    print("Row count in table:", n)
