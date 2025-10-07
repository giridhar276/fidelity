alist = [10,3,56,2,63,82,47,84]
alist.append(49)
print("After appending:", alist)
# list.extend(iterable) - adding multiple values
alist.extend([58,29,43])
print("After extending:",alist)
# list.insert(where,what)  #l.insert(index,value)
alist.insert(1,200)
print("After inserting:",alist)
# list.pop(index)
alist.pop(0)  # 0 is the index
print("After pop operation:",alist)
# list.remove(value)
if 100 in alist:
    alist.remove(100)
    print("AFter removing :",alist)
else:
    print("value in not the list")


# list.reverse()
alist.reverse()
print("after reversing:",alist)
# list.sort()
alist.sort()
print("After sorting:",alist)
