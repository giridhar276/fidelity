book = {"chap1":10 ,"chap2":20 , "chap3":30, "chap1":100}
print(book)
# add new key-value to the dictionary
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display individual value
print(book["chap1"]) # 100
print(book["chap2"]) # 20

## display keys
print(book.keys())

# display keys line by line
for k in book.keys():
    print(k)

for k in book:
    print(k)      # key
    print(book[k]) # value

##### display values
print(book.values())


for v in book.values():
    print(v)

#### dislay key,value at a time

print(book.items())

for item in book.items():
    print(item)

for k,v in book.items():
    print(k,v)


# remove key-value from dictionary
book.pop("chap1")  # chap1-10 will be removed from dictionary
print("After pop operation:", book)
book.pop("chap2")
print("After pop operation:", book)
book.popitem()   # remove last inserted key-value from dictionary
print(book)

# combining two dictionaries
book = {"chap1":10, "chap2":20}
newbook = {"chap3":30 , "chap4":40}
# method1
finalbook = {**book,**newbook}
print(finalbook)
#method2
book.update(newbook)   # book is getting updated
print(book)
print(newbook)



