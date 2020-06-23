"""creating array 
#importing the array module we have three ways
#without alias
import array
#example
a = array.array("i",[1,2,3,4,4,5,5,6,7])
print(a)
#first array is the array module
#second array is the constructor
#i is the type code
#with alias name
import array as arr
a = arr.array("i",[1,2,4,4,5])
print(a)
using * 
"""
from array import *
a = array("i",[1,2,3,4,5,6])
print(a)
#accessing array elements
print(a[1])
print(a[-2])
#length of an array
print(len(a))
#add a single element at the end of the array
a.append(45)
print(a)
#add multiple elements at the end of an array
#use the square brackets to specify values
a.extend([2,45,56,67])
print(a)
#add an element at a specific position
a.insert(2, 7889)
print(a)
#to remove a single element and return it use
#specify the index position
print(a.pop(2))
print(a)
#remove a specific element and not return it
#use the element as the paramater
a.remove(67)
print(a)
b = array("d", [2.3,4.5,6.7,2.3])
print(b)
d = array("d", [2.3,4.5,6.7,2.3])
c = array("d")
c = d + b
print(c)
#slicing
print(a[0:3])
for elements  in a:
    print(elements)