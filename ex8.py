# finally block
try:
    print("open application")
    result=10/5
    print(result)
except ZeroDivisionError:
    print("calculation error")
finally:
    print("application finished")