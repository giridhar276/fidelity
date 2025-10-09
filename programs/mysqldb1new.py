

# pip install pymysql
import pymysql, csv, os

host = "localhost"

conn = pymysql.connect(host=host, port=3306, user="root", password="admin@123")
cur = conn.cursor()

rows = []
with open("employee.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)                 # skip header
    for r in reader:
        rows.append(tuple(r))

# Build a VALUES placeholder once based on column count
placeholders = ",".join(["%s"] * len(headers))
sql = f"INSERT INTO empdb.employee VALUES ({placeholders})"

cur.executemany(sql, rows)
conn.commit()
conn.close()
print(f"Inserted {len(rows)} rows.")
