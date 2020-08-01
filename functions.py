a=int(input("enter a"))
b=int(input("enter b"))#asks for input from user in integer form
#function sum (builtin):
c=sum(    (a,b))
print(c)
#writing user defined functions
def function1():#defines a function
    print("function 1 is this")#function 1 can be used to expresses the same piece of command multiple times
function1()#executes the function.This is the syntax of executing a function
def function2(a,b):#values of a,b are given when the function is used
    """"This is not a comment but a docstring.Used to tell what the function does.Can be printed """
    avg=(a+b)/2#what the function does
    return avg#return the value after code in function has been executed
x=function2(5,6)   #sets input as 5 and 6 and executes piece of code in function and assigns to x
print(x)
print(function2.__doc__)#prints the doc string of function2
#try and except:
num1=input()
num2=input()
try:
    print("Sum:",int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line still stays if you entered something with e")
#file io basics:
#modes in file io like read and write
"""
"r":Open file for reading-default
"w"-Open file for writing
"x"-Creates file if not existing
"a"-Add more content to a file
"t"-text mode-default
"b"binary mode
"+"-read and write

"""


#lambda function:
#minus=lambda x,y:x-y#same as: def minus(a,b):
                       #contd-return(a-b)
#print(minus(9,4))#outputs 9-4
#def a_ascend(a):
   # return a[1]
#as lambda:

a=[[1,4],[5,6],[45,90]]
a.sort(key=lambda x:x[1])#'key' takes a function as argument
print(a)
#enumerate functiom:
l1=["blah1","blah2","blah3","blah4"]
for index,item in enumerate(l1):#item:list item,#index=number
    if index%2==0:#index starts from 0
        print(f"Hello read only:"[item])
#join functions:
lis=["hello","world","this ","is ","me"]
a=" , ".join(lis)#adds a comma between every element in lis
print(a)
#decorators:
def func1():
    print("something")
fun2=func1
del func1#deletes func1
fun2()#fun2 carries the code of func1 as it is previously defined
#function in function
def funcret(num3):
    if num3==0:
        return print#print is  a function
    elif num3==1:
        return int#note both print and int are functions
a=funcret(1)#call funcret ,num3=1,assign it to a
print(a)#prints(class int for 1 and 'built in function print'for 0
def funcst(func):
    func("this ")
funcst(print)#prints this (function in function)
def functi(func):
    def nowexec():
        print("print executing now")#before execution
        func()#executes func (input of functi)
        print("done ")#after execution
    return nowexec()#returns nowexec code to funcst
@functi
def some_silly_function():
    print("some thing in the silly function")
#some_silly_function=functi(some_silly_function)#some_silly_function goes in code of funcst Same can
#be written with the @symbol before the definition is given.(up)
some_silly_function()#calling the function
#function caching:
"""saves time when needed.if running a function takes 3 sec, we don't want it to repeat
so, we can assign the value to a variable, which returns its value whenever the function is called"""
import time
from functools import lru_cache#decorator from functools for caching
#before:
def delay_func(n):
    time.sleep(n)
    return n
if __name__=="__main__"#checks if program is run in this file only
    print("calling delay func")
    delay_func(3)#value
    print("done,calling again" )
    delay_func(3)
    print("called again")#totally takes 6 sec. so,
#after using iru_cache:
@lru_cache(maxsize=3)#store a max of n values, latest ones
def delay_func1(n):
    time.sleep(n)
    return n
if __name__=="__main__":   #checks if program is run in this file only
    print("calling delay func")
    delay_func1(3)#value
    print("done,calling again" )
    delay_func1(3)
    print("called again")







