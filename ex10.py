# repeted input until valid

while True:
    try:
        marks=int(input("enter marks(0-100):"))
        if not 0<=marks<= 100:
            raise ValueError("marks out of range")
        print("accept:",marks)
        break
    except ValueError as error:
        print("invalid input:",error)