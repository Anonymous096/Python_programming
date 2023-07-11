'''
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a / b
    print(c)

except ZeroDivisionError:       # This will handle the error "ZeroDivisionError" is the type of error like "ValueError" we can use except as it is. If the try code will generate error then except statement will work
    print("Can't divide by zero")
else:       # This will print if and only if try code will not generate error
    print("else block")
finally:    # This will print in every condition no matter what
    print("This will print no matter what")
'''

def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)
        interest = (amount * year * rate) / 100
        print("The simple interest is: ", interest)
        return interest
    except:
        print("Interest rate is out of range", rate)

print("Case 1")
simple_interest(800, 6, 8)

print("Case 2")
simple_interest(800, 6, 800)