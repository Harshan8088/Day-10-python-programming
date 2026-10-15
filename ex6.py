# ultiple except block

try:
    a=int(input("entr first number:"))
    b=int(input("enter secound number:"))
    print("result:",a/b)
except ValueError:
    print("invalidnumber enter")
except ZeroDivisionError:
    print("division by zero is not allowed")