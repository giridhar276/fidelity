

with open("C:\\new\\info.txt") as fobj:
    print(fobj.read())

with open("C:/new/info.txt") as fobj:
    print(fobj.read())

# raw string : 
with open(r"C:\new\info.txt") as fobj:
    print(fobj.read())