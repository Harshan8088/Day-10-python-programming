# list index error

marks=[80,90,40]

try:
    print(marks[5])
except IndexError:
    print("invalid list index")