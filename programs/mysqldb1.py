



# pip install pymysql  ( if libary not installed)
import pymysql
import csv
import os
# step1

hostname = os.environ('hostname')

conn = pymysql.connect(host=hostname,port=3306,user="root",password="admin@123")
print(conn)
# step2
cursor = conn.cursor()
# step3
filename = "employee.csv"
if os.path.isfile(filename) and os.path.getsize(filename) > 0 :
    try:
        with open(filename,"r") as fobj:
            header = fobj.readline()  # reading 1st line which is header
            reader = csv.reader(fobj)
            for line in reader:
                print(line)
                # step4
                query = "insert into empdb.employee values({},'{}',{},'{}',{},'{}','{}','{}','{}','{}',{},{},{},'{}','{}')".format(*line)
                # step 5
                cursor.execute(query)
            conn.commit()
    except Exception as err:
        print(err)
    # step6
    conn.close()
else:
    print("file is nottt found")







