# #function is called by def
# def  add(x,y):
#     return x+y

# print( "the addition of two values is ", add(4,5))

#lets define a function which will take the name as string as argument and return last char

def last_char(name):
    return name[-1]

print(last_char("Kamalakar"))

#function to define odd or even number

def  odd_or_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
num = int(input("please enter the number"))
print(odd_or_even(num))

def  odd_or_even1(num):
    if num%2 == 0:
        return "even"
    return "odd"