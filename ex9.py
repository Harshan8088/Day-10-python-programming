# raise an exception

age=int(input("enter yourage:"))

try:
    if age<18:
        raise ValueError("age must be 18 or above")
    print("elligible")
except ValueError as error:
    print(error)