# file not found

try:
    with open("report.txt","r")as file:
        print(file.read())
except FileNotFoundError:
    print("file does not exits")