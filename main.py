'''
#Take input from user and print float upto 4 decimals using formal specifier.
num = float(input("Enter a number: "))
print("decimal upto 4 is: ", "% .4f" %num)
'''

#Write a program to append and extend the list and take input of the list seperated by commas

# creating an empty list
lst = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
a = int(input("Enter the number to append: ")) # number to be append in the list
# iterating till the range
for i in range(0, n):
            ele = int(input())
            lst.append(ele) # adding the element
lst.append(a)
print(lst)

lst1 = []
m = int(input("Enter the number of elements: "))
for i in range(0,m):
        ele1 = int(input())
        lst1.append(ele1)
lst.extend(lst1)
print(lst)