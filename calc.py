#--------------------------------Modules and Packages-------------------------------

def add(a, b):
    return(a+b)
def sub(a, b):
    return(a-b)

#now when you made these functions you have to make a new py file where you need to 
#use this file name as "import <file_name> and print(<file_name>.<function_name>)"
#Here calc is a module which I've created and I imported this module in module.py file.

#in order to call a particular function or keyword you have to write command as:
# from <file_name> import <keyword/function_name>

#while importing if want to change the name the command is:
#import <file_name> as <short_name>

# we can use built-in functions also such as math or pandas etc.
#nothing will change just in place of <file_name> write the name of the built-in function.

def mult(a, b):
    return(a*b)
def div(a, b):
    return(a/b)
def expo(a,b):
    return(a**b)