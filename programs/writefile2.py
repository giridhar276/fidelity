# pythonic way # modern way
# context manager
# file is closed automatically when it is out of context

with open("info.txt","w") as fobj:
    # fobj.write(string)
    fobj.write("python\n")
    fobj.write("unix\n")
    # fobj.writlines(list)
    fobj.writelines(["unix","java","oracle\n"])
    for val in range(1,10):
        fobj.write( str(val) + "\n")
    print(fobj.closed )

print(fobj.closed )

