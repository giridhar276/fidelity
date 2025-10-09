

# mysql_to_csv_min.py
import pandas as pd
import pymysql

host="localhost"; port=3306
user="root"; password="admin@123"
database="empdb1"; table="employee"
out_csv="employee_out.csv"

conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset="utf8mb4")
cur = conn.cursor()
cur.execute("SELECT * FROM `{}`".format(table))
rows = cur.fetchall()
cols = [d[0] for d in cur.description]
cur.close(); conn.close()

pd.DataFrame(rows, columns=cols).to_csv(out_csv, index=False)
print("Exported:", len(rows))
