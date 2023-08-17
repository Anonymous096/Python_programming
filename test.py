'''
n = int(input())
if (n>=0 & n<100):
    if n<50:
        print("FAIL")
    else:
        print("PASS ")
else:
    print("INVALID INPUT")
    '''

'''
n = list(input("Enter number to list: ").split())
a = int(input("Enter the number to append: "))
n.append(a)
print(n)
e = list(input("Enter the number to extend: ").split())
n.extend(e)
print(n)
'''

def al(lon):
    n = int(input("Enter a"))
    lon.append(n)
    return lon

def el(lon):
    ol = list(map(int, input("enter e: ").split()))
    lon.extend(ol)
    return lon

lon = list(map(int, input("enter: ").split()))
lon = al(lon)
lon = el(lon)
print(lon)
