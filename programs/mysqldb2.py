





# pip install pymysql  ( if libary not installed)
import pymysql
import csv
import os
# pip install python-dotenv
from dotenv import load_dotenv

# 1) load .env from current folder
load_dotenv()

# 2) read values
hostname = os.getenv("hostname")        # e.g., localhost
port = int(os.getenv("port") )          # e.g., 3306
username = os.getenv("user")            # e.g., root
password = os.getenv("password") 


conn = pymysql.connect(host=hostname,port=port,user=username,password=password)
# step2
cursor = conn.cursor()
# step3

query = "select count(*) from empdb.employee"
cursor.execute(query)
for record  in cursor.fetchall():
    print(record)

# step6
conn.close()







