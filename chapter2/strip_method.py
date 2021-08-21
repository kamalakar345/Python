name = "    kamalakar    "
dots = "..............."
print(name + dots)
# lstrip() to remove left side spaces
print(name.lstrip() + dots)
# rstrip()  to remove right side spaces

print(name.rstrip() + dots)

#  strip() to remove both left and right spaces

print( name.strip() + dots)

# replace method  in string
name1 = "kamal    akar"
print(name1.replace(" ",""))

#replace()  and find()  methods

string = " she is the beautiful  lady is lady"
print(string.replace("is", "was"))
print(string.replace("is", "was"))
print(string.replace("is", "was", 1)) #last paramter will take the occurance
print(string.find("is", 1)) #last paramter will take the occurance

# to find the second occurance we must floow the below procedure
ipos1 = string.find("is")
print(string.find("is", ipos1 + 1)) # this will start find the is from (ipos1+1) occurance

#center mathod
##write a program to take input from user and add 2 ** towrads left and ** towrads right
name11 = input("enter the user name:")
print(name11.center(len(name11) +  4, "*"))

