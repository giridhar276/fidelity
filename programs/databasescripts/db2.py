

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# --- config ---
user = "root"
password = quote_plus("admin@123")  # encodes '@'
host = "localhost"
port = 3306
database = "empdb1"
table_name = "employee"
out_csv = "employee_out.csv"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# Option 1: read entire table
df = pd.read_sql_table(table_name, con=engine)

# (Alternative) Option 2: custom query
# df = pd.read_sql(f"SELECT * FROM `{table_name}` WHERE 1", con=engine)

df.to_csv(out_csv, index=False)
print(f"Exported {len(df)} rows to {out_csv}.")
