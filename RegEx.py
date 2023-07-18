import re

# findall() function
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# search() function
txt1 = "The rain in Spain"
x1 = re.search("\s", txt1)

print("The first white-space character is located in position:", x1.start())

# split() function
txt2 = "The rain in Spain"
x2 = re.split("\s", txt2)
print(x2)

# sub() function
txt3 = "The rain in Spain"
x3 = re.sub("\s", "9", txt3)
print(x3)

# To check if the string starts with "The" and ends with "Spain"
txt4 = "The rain in Spain"
x4 = re.search("^The.*Spain$", txt4)

if x4:
    print("YES! We have a match!")
else:
    print("No match.")
