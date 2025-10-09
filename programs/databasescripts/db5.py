

# csv_to_mysql_min.py
import pandas as pd
import pymysql

host="localhost"; port=3306
user="root"; password="admin@123"
database="empdb1"; table="employee"
csv_path="employee.csv"

df = pd.read_csv(csv_path, dtype=str)
df = df.where(df.notna(), None)

# simple placeholders part
values_part = ",".join(["%s"] * df.shape[1])

conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset="utf8mb4")
cur = conn.cursor()

sql = "INSERT INTO `{}` VALUES ({})".format(table, values_part)
cur.executemany(sql, df.values.tolist())
conn.commit()

print("Inserted:", cur.rowcount)
cur.close(); conn.close()
