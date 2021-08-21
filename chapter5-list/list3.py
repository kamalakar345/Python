fruits =['ornage', 'apple', 'peer', 'banana', 'kiwi', 'apple', 'banana']

if "apple" in fruits:
    print("present")
else:
    print("not present")

# few more methods in list
#count , sort,  sorted function, reverse, clear, copy
# count method
print(fruits)
print(fruits.count("apple")) # used to check number of apperance of word apple in list
print(fruits.count("peer"))

#sort method
fruits.sort()
print(fruits)  # used for sorting in alphbetical order or numerical order

number = [3,5,1,9,10]
number.sort()
print(number)

##sorted fumction
#only used for sorting but not changing original list
number1 = [3,5,1,9,10,6 ]
print(number1)
print(sorted(number1))
print(number1)

#clear method
number.clear()
print(number)

#copy method
number1_copy = number1.copy()
print(number1)