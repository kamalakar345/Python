#Concepts of Strings
from typing import FrozenSet


First_name = "Malugula"
Last_Name = "Kamal"

#concatenate 
Name = First_name + Last_Name

print(Name)

Name = First_name + " " + Last_Name
print(Name)

# we cannot add number with the string 

#print(Name + 3 )  #throws an error
print(Name + "3")  #this will works
print(Name + str(3))  # this will work

#### input function
""" inout function is used take the user input and assigned to variable ,
  By default input functions return string"""

name = input("Enter the name:")
print(" My name is {name}")
