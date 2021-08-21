#looping in tuple
mixed = (1,2,3,4,5.0)
for i in mixed:
    print(i)

#tuple with one element
num = (1)     
words = ('words')
print(type(num))
print(type(words))
num = (1,)     
words = ('words',)
print(type(num))
print(type(words))

#tuples without parenthesis

guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

#tuple un packing
guitarists = ('maneli Jamal', 'eddie van der meer', 'Andrey ')

guitarists1, guitarists2, guitarists3 = (guitarists)

print(guitarists1)

#list inside tuples
favorities = ('southern magnolia', ['tokua Ghoul theme', 'landscape'])
# we can apply all function on list which are present inside tuple
favorities[1].pop()
favorities[1].append("we made it")
print(favorities)

#tuple function 
#min
#max
#sum

#when ever u are returning two values in function the return will return tuple 

def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(func(2,3))  #  o/p is (5,6)