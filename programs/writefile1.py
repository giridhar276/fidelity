# traditional way # regular way

#fobj = open("C:\\info.txt","w")
fobj = open("info.txt","w")
# fobj.write(string)
fobj.write("python\n")
fobj.write("unix\n")
# fobj.writlines(list)
fobj.writelines(["unix","java","oracle\n"])
for val in range(1,10):
    fobj.write( str(val) + "\n")
fobj.close()