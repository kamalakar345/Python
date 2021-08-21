fruits1 =['ornage', 'apple', 'peer', 'banana', 'kiwi']
fruits2 =['ornage', 'apple', 'peer', 'banana', 'kiwi']
fruits3 =['ornage', 'apple', 'banana', 'kiwi']
 
print(fruits1 == fruits2)  # values are same
print(fruits1 == fruits3)
print(fruits1 is fruits2) # is used to check whether given list uses same memory locations are not

#Split method -- convert string into List
user_info = 'kamalakar 33'.split()
print(user_info)
user_info = 'kamalakar,33'.split(",")
print(user_info)

name , age = 'kamalakar,33'.split(",")
print(name," ",age)

#join method -- convert list to string

user_info1 = [ "kamalakar", "25"]

print(','.join(user_info1))