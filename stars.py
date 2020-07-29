a=int(input("enter no of required rows"))
b=int(input("enter 1 or 0"))
c=bool(b)
d=0
while(True):
    if a!=0 and c==True:
        print("your number was 1\n")
        while(d!=a+1):
            print(d*"*")
            d=d+1
    elif a!=0 and c==False:
        print("your number was false in boolean")
        while(d!=a):
            print(a*"*")
            a=a-1
    else:
         print("error:number of rows cannot be 0")
         break



