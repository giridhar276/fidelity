
### multiple dataframes

import pandas as pd
import pantab

df1 = pd.read_csv("employee_100.csv")
df2 = pd.read_csv("another.csv")

# keys: (schema, table). Schema “Extract” is conventional.
pantab.frames_to_hyper(
    {("Extract", "employee"): df1, ("Extract", "another_table"): df2},
    "multi.hyper",
    # mode="w" creates/overwrites the file
)
