

##### display all the builtin functions and exceptions
print(dir(__builtins__))
alist = [10,20,30]
print(len(alist))  # length of the list
print(max(alist))  # largest number
print(min(alist))  # smallest number
print(sum(alist))  # sum of the list
print(id(alist))   # unique reference
print(type(alist)) # type of the object
print(isinstance(alist,str))  # validate teh object
print(isinstance(alist,list))