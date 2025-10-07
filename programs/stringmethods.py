
name = "python programming"
print(name)
print("I love",name)
# slicing
# string[start:stop:step]
print(name[0])  #p
print(name[0:5]) #pytho
print(name[0:5:2]) #pto   # 2 is the step(incremental value)
print(name[-1])  #g
print(name[-2])  #n
print(name[::])  #python programming
print(name[::-1])# string reverse



name = "python programming"
print(name.capitalize())
print(name.isupper()) # only for validating
print(name.upper())   # displaying in uppercase
print(name)
print(name.startswith("p"))
print(name.endswith("z"))
print(name.split(" "))
print(name.replace("python","java"))

aname = " python  "
print(len(aname))
print(len(aname.strip()))
print(len(aname.lstrip()))
print(len(aname.rstrip()))

name = "\"python programming\""
print(name)


#
if 1 < 2 :
    print("condition is true")
    print("inside if")
    print("still inside if")


# simple if 
if name.islower():
    print("string is lower")
    print("inside if")

# if-else
if name.islower():
    print("string is lower")
else:
    print("string is  upper")


# if-elif-elif-else
lang = input("Enter any language :")
if lang == "python":
    print("python programming")
elif lang == "unix":
    print("unix programming")
elif lang == "java":
    print("java progarmming")
else:
    print("its something else")
################ 
lang = input("Enter any language")
if "python" in lang:
    print("its python")
elif "unix" in lang:
    print("its unix")
elif "java" in lang:
    print("its java")
else:
    print("its someother lang")






