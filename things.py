print("enter your  first number to be added")
num1in=input()
str1="this that these those"
print("enter your second number")
num2in=input()
print("the third number is: (default)")
print("the third number is 21")
num3in=len(str1)
print("the sum is:", int(num1in)+int(num2in)+int(num3in))
print(len(str1))
print(str1[0:21:2])
print(type(str1))
print(str1.isalnum()) #says if the variable str1 has alpha numerics only
print(str1.isalpha())#says if the variable has either alphabelts or numerals only
print(str1.endswith("those"))#says if the variable ends with the word "those"
print(str1.count("t"))#counts the number of ts in str1
print(str1.capitalize())#capitalizes the ts in str1
print(str1.find("those"))  #  outputs the positon of t in those ie, first letter in the string
print(str1.lower())#turns text in str1 to lowercase
print(str1.upper())#turns text to uppercase
print(str1.replace("this","tthhis"))#replaces 'this' in str1 with 'tthhis'
#there are many such functions for strings
"""lists:note that ()-tuple(Tuples are sequences, just like lists. 
The differences between tuples and lists are, the tuples cannot be changed unlike lists and 
tuples use parentheses, whereas lists use square brackets. Creating a tuple is as simple as 
putting different comma-separated values.; {}-dictionary(dict); []-list"""
listex=["value1","value2","value3","value4","value5","value6"]# list containing 5 values from 0 to 5
print(listex)#prints the list defined above
print(listex[2])#prints the third object(second, counting from 0)here,value3
numbers=[23,34,54,45,234,424,542,5678,95]
numbers.sort()#arranges numbers in ascending order
print(numbers)#prints them
numbers.reverse() ,"""arranges in reverse order; 
note the numbers wont be in the same order as entered after this and the sort function has been applied"""
print(numbers)#prints them
print(numbers[3])#prints the 4th number
print(numbers[ : ])#prints the list of numbers
print(numbers[1:5])#ignores the 0th and numbers after 5 in order
print(numbers[::2])#skips every second number in the order
print(numbers[::-1]),"""reverses the order of numbers, same as using the reverse() function,can also be
applied to strings"""
print(max(numbers))#prints the maximum value of the numbers;also min for minimum
numbers.append(45)#adds 45 to the end of the original list
d1={"Alvin":"tacos","Ben":{"Breakfast":"burger","Lunch":"paratha"}}#dict to tell what Alvin eats and what ben eats
#syntax for an element in  dict= {"key":"item"}
print(d1["Ben"]["Lunch"])#displays what ben eats for lunch
print(d1)#prints the whole list
d1 ["Tfue"]= "Junk Food"#updates dict d1 with what Tfue also eats
print(d1)#prints the updated list
d2=d1.copy()#any function executed in d2 won't change anything in d1, which can happen if we give d2=d1
print(d2)#prints out d2, which is similar to d1
del d2["Tfue"]#deletes Tfue and corresponding value from d2, but not d1
print("d1",d1)#proof of the above
print("d2",d2)#proof
print(d1.get("Alvin"))#gets corresponding value of alvin from d1
d1.update({"Tom":"falafel"})#updates values
print(d1)#prints them after update
print(d1.keys())#prints the keys in d1
print(d1.items())#prints the items of d1
#creating a dictionary of 6 words, taking input from the user
d5={"Anonymous":"An unknown person","Alliteration":"A sentence with a set of words which have similar sounds",
 "Asgard":"A place in the MCU, considered birthplace of thor",
    "RAM":"Random access memory","Hydrogen":"A chemical element , Atomic number:1",
    "Vintage":"Refering to the old times" }
i2= input("enter the word here")
print((i2),"means:",d5[i2])
#another method:
D={"cow":"milk"}#can add more items
key=input("Type key for meaning")
print(D[key])
#sets
s=set([23,34])
s.add(3 )#adds 3 to the set s
s.add(4)#adds 4
s.remove(4)#removes 4 from the set
s1=s.intersection({23,34,6})#considers the similar values in s and given values and displays only the similar ones
s1=s.union([234,32])#joins set s and also gives new values to s1
print(s,s1)
print(s.isdisjoint(s1))#checks if both are similar


