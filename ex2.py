# invalid index error

try:
    age=int(input("rnter age:"))
    print("your age:",age)
except ValueError:
    print("please enter a valid number")