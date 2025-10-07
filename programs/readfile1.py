# fobj acts like cursor
# method1  ---> reading line by line
with open("info.txt","r") as fobj:
    for line in fobj:
        print(line.strip())
    
# method2 ----> output in list
with open("info.txt","r") as fobj:
    print(fobj.readlines())   # output in list

# method3   ----> output in string
with open("info.txt","r") as fobj:
    print(fobj.read())

# method4
import csv
with open("info.txt","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)

# method5
import pandas
df = pandas.read_csv("info.txt")
print(df)