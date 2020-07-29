f1=open("king.txt")

try:
    f=open("name.txt","rt")#not a file
#except Exception as e:#if try has failed #of different types
   #commented print(e)
except EOFError as e:#end of file
    print(f"eof errror{e}")
except IOError as e:
    print("io error",e)



else:
    print("this will run only if except is not running")
finally:#executed even after else
    f1.close()
    #f.close()

#Coroutines in python:
#example:
def search():
    book="lengthy string"
    import time
    #while reading the book:
    time.sleep(4)
    #to stop the function here and deal with the rest of given values in the later code:
    while True:
        text=(yield)#generates on the flow
        if text in book:
            print("yes")
        else:
            print("no")
searcher=search()
print("search started")
next(searcher)
print("next mmethod run no need to wait anymore")
searcher.send("me")#goes in while loop
input("enter num")#exampple that it doesnt wait
searcher.send("string")
searcher.close()#ends
