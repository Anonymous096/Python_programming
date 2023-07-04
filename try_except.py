try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a / b
    print(c)

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("else block")
finally:
    print("This will print no matter what")