l1=["man","woman","tiger","lion"]#list with given elements
print(l1[0],l1[1])#prints items in order if continued in the same pattern .But can be tedious so
l2=l1.append("cow")
for item in l1:
    print(item)#prints entire list
  #for  list of list
l3=[["May","summer"],["December","winter"],["June","Rainy"],["January","Fall"]]

for item,season in l3:
      print("the month :",item,"is in the season",season)

#as a dict
d1=dict(l3)
for item in d1:
    print(item)#only prints the items of the dict
    #segregating items in a list
    listex=["ram",34,3,"cow"]
listex.append(input("enter anything"))
for item in listex:
        if str(item).isnumeric() and int(item)>6 :#can also use type(item)==int and item>6:
            print(item)
            #using while loops:


while(True):
    itn = float(input("enter any number\n"))
    if(itn>100):
        print(itn,"is greater than 100\n" )
        break#comes out of loop
    else:
        print("enter again\n")
        continue#repeats loop
        #new project:game to guess my number
n=18
nguess=0
print("you have 10 guesses to find my number\n")
while(nguess<=10):
    guessnum=int(input("enter your number\n"))
    nguess=nguess+1
    if guessnum<n :
        print("Your number is smaller than mine\n")
    elif guessnum>n:
        print("Your number is greater than mine\n")
    else:
        print("You won\n")
        print("you took ",nguess," guesses to finish")
        break
print("You have",11-nguess,"guesses left")
if nguess>10:
    print ("game over")
##Using for loops with else
lstex=["name1","name2","name3"]
#for loop can end when:1-iterable reaches end
#or when its meets a break statement;
for i in lstex:
    print(i)
else:
    print("this for loop ended properly")












