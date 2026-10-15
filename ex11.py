# atm withdrawal vaidation

balance=1000

try:
    amount=float(input("withdrawal amount:"))

    if amount<=0:
        raise ValueError("invalid amount")
    if amount>balance:
        raise ValueError("insufficient balance")

    balance-=amount
    print("withdrawal succesful")
    print("remaining balance:",balance)

except ValueError as error:
    print("transaction failed",error)