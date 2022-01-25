#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nalin Gupta
#
# Created:     25-01-2022
# Copyright:   (c) Nalin Gupta 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#assignment question 1
s1 = ("Python is a case sensitive language")
print("the length of the string is " + str(len(s1))) #a part
print("the reverse order of the string is ",(s1[::-1]))#b part
s2 = s1[10:26] #c part
s2.replace("a case sensitive","object oriented") #d part
print("the index of a in the string is " + str(s1.find('a'))) #e part
print("the original string without whitespaces is " + s1.replace(" ","")) #f part

#assignment question 2
name = ("Nalin kumar gupta")
sid = 21103027
department = ("CSE")
cg = 9.9
print("Hey, " + name +" here!")
print("My SID is " + str(sid))
print("I am from " + department + " department and my CGPA is " + str(cg))

#assignment question 3
a = 56
b = 10
print("a.",a&b)
print("b.",a/b)
print("c.",a^b)
print("left shift both a and b with 2 bits: ",a<<2,b<<2)
print("right shift a and b with 2 and 4 bits respectively: ",a>>2,b>>4)

#assignment question 4
a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

if (a >=b) and (a >=c):
    g = a
elif (b >=a) and (b >=c):
    g = b
else:
    g = c

print("the largest number is: " + str(g))

#assignment question 5
a = input("enter string: ")
if "name" in a:
    print("yes")
else:
    print("No")

#assignment question 6
a = float(input("enter first side length: "))
b = float(input("enter second side length: "))
c = float(input("enter third side lenth: "))
if (b+c<=a) or (a+b<=c) or (a+c<=b):
    print("No")
else:
    print("Yes")

