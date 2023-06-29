# Files IO Basics

'''
"r" = open file for reading - Default 
"w" = open file for writing
"x" = create file if not existed
"a" = add more content to a file
"t" = text mode - Default
"b" = binary mode
"+" = read and write

so for a sample we have already made a .txt file named as "function.txt" from where we will
read and open the file.
'''

f = open("function.txt") # used to read a file but will now return anything but if we made a file pointer(variable) it will return when we print that variable. In this case f is the variable.
# explaination of command is: open("<file_name>", "<mode>"), inverted commas are mandatory, modes are generally:
# r = which is default, rt = default(it will return the content of file in text mode), rb = it will return the content of the file in binary mode.
content = f.read()
print(content)
print(f.readline()) # this will only read a line from the content of the file, starts from the first line.
print(f.readlines()) # This will stores the lines of content of file in a list format


f.close() # This will close the file and it is good to close a file after reading because it will free the resources which had been used to make it open and read and if any other program needs to read this file it can do it easily
