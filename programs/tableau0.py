


# csv_to_hyper_linebyline.py
# Convert CSV -> Tableau .hyper (all TEXT), simple and explicit, no "if" conditions.

from tableauhyperapi import HyperProcess, Connection, Telemetry, TableDefinition, TableName, SqlType, Inserter, CreateMode
import csv

csv_path  = "employee_100.csv"
hyper_path = "employee3.hyper"
schema = "Extract"
table  = "employee1"

# 1) Read header
f_header = open(csv_path, newline="", encoding="utf-8")
reader_header = csv.reader(f_header)
headers = next(reader_header)
f_header.close()

# 2) Clean header names
def clean(s):
    return (s.strip().lower()
            .replace(" ", "_").replace("-", "_").replace("/", "_")
            .replace("(", "").replace(")", ""))

cols = [clean(h) for h in headers]

# 3) Define table (all TEXT columns)
table_def = TableDefinition(TableName(schema, table))
for c in cols:
    table_def.add_column(c, SqlType.text())

# 4) Start Hyper, create/replace DB, create schema & table
with HyperProcess(Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU) as hp:
    with Connection(hp.endpoint, hyper_path, CreateMode.CREATE_AND_REPLACE) as conn:
        conn.catalog.create_schema(schema)
        conn.catalog.create_table(table_def)

        # 5) Open CSV (data rows)
        with open(csv_path, newline="", encoding="utf-8") as f_data:
            r = csv.reader(f_data)
            next(r)  # skip header row

            # 6) Insert rows
            with Inserter(conn, table_def) as inserter:
                for row in r:
                    inserter.add_row(row)
                inserter.execute()

print("Created:", hyper_path)
