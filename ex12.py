# student marks validation

try:
    marks=int(input("enter student marks:"))
    if marks<0 or marks>100:
        raise ValueError("marks must be 0 to 100")

    if marks>=35:
        print("pass")
    else:
        print("fail")
except ValueError as error:
    print("error:",error)