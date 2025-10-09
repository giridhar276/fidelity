

# pip install pymysql
import pymysql, csv

host = "localhost"

# --- DB connection ---
conn = pymysql.connect(host=host, port=3306, user="root", password="admin@123")
cur = conn.cursor()

# --- read CSV ---
rows = []
with open("employee.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)  # CSV header becomes column list
    for r in reader:
        rows.append(tuple(r))

# --- build SQL using .format for structure, %s for values ---
col_list = ", ".join("`{}`".format(c) for c in headers)               # backtick columns
placeholders = ",".join(["%s"] * len(headers))                         # driver placeholders
sql = "INSERT INTO `empdb`.`employee` ({cols}) VALUES ({vals})".format(
    cols=col_list,
    vals=placeholders
)

# --- insert ---
cur.executemany(sql, rows)
conn.commit()
cur.close()
conn.close()

print("Inserted {} rows.".format(len(rows)))
