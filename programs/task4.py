
#Write a program to print all product names and prices.

products = [
    {"id": 101, "name": "Laptop", "price": 75000},
    {"id": 102, "name": "Mobile", "price": 25000},
    {"id": 103, "name": "Tablet", "price": 15000}
]

print(type(products))

for item in products:
    print(item['name'] , item['price'])