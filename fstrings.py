#fstrings:
#string formatting
import math
mename="Raaj"
a="This is %s"%mename#joins both strings:string formatting
a1=21
#print(a)
#another method to perform string formatting
b="This is {} {}"
b1=a.format(mename,a1)#formats and adds the variables to string a
print(b1)
ak=f"thidwfueon {a1}{mename} {4*45}{math.cos(63)}"#adds variables and statements in curly braces to the
# string. f is needed before the string to enable fstrings.fuction from modules can also be used
print(ak)
