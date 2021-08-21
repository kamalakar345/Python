#generate list from range function
#something more about pop method
#index method
#pass list to function

number = list(range(1, 11)) # to generate list from list function
print(number)

popped_item = number.pop()
print(number)

#index method is used to show thw index number in list

print(number.index(9))

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(number.index(1)) # it will display the frist index of frist occurance of element "1"

# to find the second occurance of element "1"
#print(number.index(1,3, 5)) # answer willbe 10, as again "1" is in 10 index , it will search from index 3 and stop at 5

#pass list to function
# we can also pass list argument as parameter to function
#example to convert list of number into negative number

numbers1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
def negative_1(numbers1):
    negative = []
    for i in numbers1:
        negative.append(-i)
    return negative
print(negative_1(numbers1))
