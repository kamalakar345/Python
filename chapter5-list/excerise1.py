# squre root of the list of number 

def squre(number):
    sq_num = []
    for i in number:
        sq_num.append(pow(int(i), 2))
    return sq_num

provided = input("enter the number to the list").split(",")
print(provided)
print(squre(provided))

numbers1 = list(range(1, 11))
print(squre(numbers1))
