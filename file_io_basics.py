# Files IO Basics

'''
"r" = open file for reading - Default 
"w" = open file for writing
"x" = create file if not existed
"a" = add more content to a file (append)
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

# Even to write in the file we have to open the file and then write it.
d = open("file_basics.txt", "w") # Here putting writing mode <"w"> is mandetory and and the if you put the file name which already exists then it would over write it and all the stuff which was written before will be ddeleted, if you put new name of file it will create the file by itself in this case it made <"file_basics.txt">
d.write("This is written from the python code using write function") # It will write the content in the file
d.close() # Close the file whenever not in need
d = open("function.txt", "a") # It will add/append the content in existing file without over writing it
d.write("This is appended content added by python code using write and append function")
d.close() # You can take same variable and repeat the process and it will work properly this is the benifit of the close function.

# If you store d.write() in a variable then it will print the number of characters written in a file example code is given below:
d = open("file_basics.txt", "w")
c = open("file_basics.txt", "a") # This will append the content of the file
b = c.write("\n This is appended using code and stored in a variable and now it will show the number of characters entered and i will append it multiple times just to check if it works\n")
print(b)
# New thing that if you append and run the command again and again it will append in the terminal again and again not in the .txt file it will only add the content once whenever you run it for the first time.
a = d.write("This will print the number of characters and spaces that are added/written in the .txt file")
print(a) # This will print the number of characters that are added in the file.
d.close()

# Handle read and write both, if you want to read the file and also want to add something in that file only. we can do that by:
