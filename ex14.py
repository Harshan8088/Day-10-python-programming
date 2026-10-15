# safe calculation

try:
    a=float(input("first number:"))
    b=float(input("enter secound number:"))
    operator=input("operator(+,-,*,/):")

    if operator=="+":
        result =a+b
    elif operator=="-":
        result = a-b
    elif operator=="*":
        result = a*b
    elif operator=="/":
        result=a/b
    else:
        raise ValueError("invalid operator")

    print("result:",result)

except ValueError as e:
    print("input error:".e)
except ZeroDivisionError:
    print("cannot divsion by zero")