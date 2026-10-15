# shopping quantity validation
price=250

try:
    quentity=int(input("enter quentity:"))
    if quentity<=0:
        raise ValueError("quentity must be positive")
    print("total:",price*quentity)
except ValueError as error:
    print("invalid quentity:",error)