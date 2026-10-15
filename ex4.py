# dictionary key error

student={"name":"rahul","age":25}

try:
    print(student["marks"])
except KeyError:
    print("key not found")