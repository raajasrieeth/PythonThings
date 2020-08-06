f = open("king.txt",
         "rt")  # syntax for opening a file ,Assigning a file pointer to f.r and t are modes as previously dicussed
content = f.read()  # reads file and assigns to 'content'.Prints the whole file in absence of argument
print(content)
content = f.read(3)  # reads 3 characters in the file, spaces included
print(content)
content = f.read(3)  # reads nexts and assigns too 'content'
print(content)
# to print linewise:
"""for line in f:
    print(line,end="")"""  # the content shouldn't be defined (before)as the file pointer becomes empty
print(f.readline())  # prints first line
print(f.readline())  # prints second line.  its a function
print(f.readlines())  # prints like a list:file pointer is now at the end of the document
f.close()  # close file
# How to write a file:
f = open('king2.txt', 'w')#creates new or opens existing file.Write 'w' mode erases current data in the file,
# to be replaced by  added values.append'a' mode only updates the content in the file."""
f.write ("This is an addition to the content in the file")  # replaces the content in the file with given command
# append mode to add on instead of replacing the entire file:
f.close()
f = open("king.txt", "a")  # open existing file whose data needs to be appended
x = f.write("This text has been appended from Python\n")  # doesnt replace content aas in append mode
print(x)  # prints number of new cahracters added to the file.
f.close()
# for both reading and writing
f = open("king.txt", "r+")  # opens file for both reading and writing
print(f.read())  # prints content in the file
f.write("thank you ")  # adds to the file
print(f.read())
f.close()
x=open("king.txt")
print(x.readline())  # prints first line
print(x.readline())#prints second line
print(x.tell())#tells the position of file pointer in a file
x.seek(20)#resets file pointer and sets it to a position given in the argument
print(x.readline())#reads the line of the file pointer
x.close()#closes the file
with open("king.txt","rt")as f:#same as writing f=open... and f.close() both are executed in the same line
    q=f.read(34)
    print(q)#no need to close file