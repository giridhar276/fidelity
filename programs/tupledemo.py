

alist = [10,20,30]
alist[0] = 100
print("After changing:",alist)


atup = (10,20,30,40)
#atup[0] = 100
print("AFter changing:", atup)
# converting tuple to list 
# typecasting - converting from one object to another object
alist = list(atup)
# now modifying list
alist[0] = 100
# reconverting back to tuple
atup = tuple(alist)
print("with changes :",atup)