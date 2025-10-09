# pip install pymysql
import pymysql, os

# If you set these in your environment, use .get(); otherwise hardcode.
host = "localhost"

conn = pymysql.connect(
    host=host, port=3306, user="root", password="admin@123",
    local_infile=True  # <-- required for LOCAL INFILE
)
cur = conn.cursor()

csv_path = r"employee.csv"   # absolute path is safest
sql = f"""
LOAD DATA LOCAL INFILE '{csv_path}'
INTO TABLE empdb.employee
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
"""
cur.execute(sql)
conn.commit()
conn.close()
print("Loaded!")
