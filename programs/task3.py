#Write a program to display all employee names and their departments.
employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


for item in employees.values():
    print(item['name'], item['department'])


for key,value in employees.items():
    print(value['name'], value['department'])


for key in employees:
    print(employees[key]["name"] , employees[key]["department"])