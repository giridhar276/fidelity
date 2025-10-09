
import pandas as pd
import pantab

# 1) Load your CSV
df = pd.read_csv("employee_100.csv")   # or "employee.csv"

# (Optional) clean column names a bit
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(r"[^\w]+", "_", regex=True)
)

# 2) Write to Hyper
# Table name can be just "employee" (schema defaults to Extract)
pantab.frame_to_hyper(df, "employee.hyper", table="employee", table_mode="w")
print("Created employee.hyper")
