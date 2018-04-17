# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:37:53 2018

@author: krishna.i

Assignment 2.3: Write a Python program to reverse a word after accepting the
input from the user.

Sample Output:
    Input word: AcadGild
    Output: dilGdacA

"""

aname= str(input("Enter a word: "))     # Accepting an input from user
print("Input given: {} \n".format(aname))         # Printing the input as is

# Method 1: by using slicing
print("Method #1")
revname = aname[::-1]               # Method 1 to store input string in reverse order in another string
print("Output: ",revname)           #Printing the reversed string stored in second variable

# Method 2: through loop in combination with slicing
print("\nMethod #2\nOutput: ",end='')
for a in aname[::-1]:
    print(a,sep='',end='')

# Method 3: through loop in combination with the help of length-value of the string
a= (aname.__len__())-1
print("\n\nMethod #3\nOutput: ",end='')
while a >= 0:
    print(aname[a],sep='',end='')
    a = a - 1

# End of the code
