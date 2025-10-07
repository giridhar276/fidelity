try:
    fobj = open("customers.txt","r")
    print(fobj.read())
    fobj.close()
except Exception as e:      # Default exception or base class Exception
    print(e)
    print("file is not found")
########################################################
try:
    fobj = open("customers.txt","r")
    print(fobj.read())
    fobj.close()
except TypeError as err:
    print("Invalid operation")
except ValueError as err:
    print("Invalid input")
except (IndexError,KeyError) as err:
    print("Invalid key or invalid index")
except Exception as err:
    print(err)
    print("file is not found")