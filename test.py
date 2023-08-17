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

l = []
n = int(input("Enter number of elements: "))
for i in range(0,n):
    ele = int(input("Enter the elements: "))
    l.append(ele)
a = int(input("Enter the number to append: "))
l.append(a)
print(l)
l1 = []
n1 = int(input("Enter list to extend in existing: "))
for i in range(0,n1):
    e = int(input("Enter the list: "))
    l1.append(e)
l.extend(l1)
print(l)

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
'''