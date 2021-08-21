#how to add  items to our list

fruits = ["grapes", "apple"]
fruits.append('mango')  # which will append in last

fruit1 = [1]
fruit1.append("ornage")
fruit1.append('kivi')

print(fruits,fruit1)

##some moe methods to add data in our list
# insert  method  to add a data at particular position
fruit1.insert(1, "grapes")
print(fruit1)

#join two list(concatenate)

fruit2 = ['grapes', 'ornage']

fruits11 = fruit1 + fruit2

print(fruits11)

#extend method it will extend the items in list
print(fruit1)
fruit1.extend(fruit2)
print(fruit1)

##to store list under list we can use append
fruit1.append(fruit2)
print(fruit1)

###methods to delete data from list

fruits =['ornage', 'apple', 'peer', 'banana', 'kiwi']
#pop method
fruits.pop()  #by default it will remove last append list
print(fruits)
fruits.pop(1)  # delete particular poistion data in list

print(fruits)

del fruits[1] ## delete particular poistion data in list

print(fruits)

# remove method to item in list which we do not know the position

fruits.remove('banana')
print(fruits)
