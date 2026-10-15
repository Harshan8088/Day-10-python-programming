import random

secret=random.randint(1,20)
attempts=0

print("guess a number between 1 and 20")

while True:
    try:
        guess=int(input("enter guess:"))
        if not 1<=guess<=20:
            raise ValueError("enter 1 to 20")
        attempts +=1

        if guess == secret:
            print("correct guess!")
            print("attempts:",attempts)
            break
        elif guess<secret:
            print("too low")
        else:
            print("too hig")

    except ValueError as error:
        print("invalid input:",error)