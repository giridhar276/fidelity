
# Every OS contains set of processses that keep runing
# Every process contains system calls.

# regular way # traditionl way
# function body
def display(a,b):
    c = a + b
    return c

# calling function
total = display(10,20)
print(total)






## #lambda function
# lambda is the repalcement of single liner function
#functioname = lambda variables : expression
display = lambda a,b: a + b
total = display(10,20)
print(total)

toupper = lambda name : name.upper()
output = toupper("python")
print(output)

exam = lambda marks : "fail" if marks < 35 else "pass"
test = exam(30)
print(test)



# c style of programming
alist = [10,20,30]
blist = []
#[15,25,35]
for val in alist:
    blist.append(val + 5)
print(blist)


#map(function,iterable)
def increment(x):
    return x + 5
print(list(map(increment,alist)))

# using lambda 
print(list(map(lambda x: x + 5,alist)))





#Convert to strings
nums = [1, 2, 3, 4, 5]
to_str = list(map(lambda x: str(x), nums))
print(to_str)  # ['1', '2', '3', '4', '5']


#Convert floats to ints
floats = [2.5, 3.6, 4.1]
ints = list(map(lambda x: int(x), floats))
print(ints)  # [2, 3, 4]



#Uppercase names
names = ["alice", "bob", "carol"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)  # ['ALICE', 'BOB', 'CAROL']



#Extract domain from email
emails = ["user1@gmail.com", "user2@yahoo.com"]
domains = list(map(lambda x: x.split("@")[1], emails))
print(domains)


names = ["Alice", "Bob"]
greeted = list(map(lambda x: "Mr./Ms. " + x, names))
print(greeted)

