


import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = "root"
password = quote_plus("admin@123")  # encodes '@'
host = "localhost"
port = 3306
database = "empdb"



engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
pd.read_csv("employee.csv").to_sql("employee", con=engine, if_exists="replace", index=False)
print("Done.")

