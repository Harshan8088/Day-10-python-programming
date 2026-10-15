# try except else

try:
    number=int(input("enter number:"))
except ValueError:
    print("invalid input")
else:
    print("square:",number*number)