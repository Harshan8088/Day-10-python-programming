# divide by zero

try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")