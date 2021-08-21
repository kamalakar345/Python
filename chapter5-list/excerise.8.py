#define a funtion which will take a list as input and count the number of list present in given input list
list1 = input("enter the sequence with space separetd").split()
print(list1)
def list_count(list1):
    count = 0
    for i in list1:
        if type(i) == list:
            count = count + 1
    return count
print(list_count(list1))
mixed = [1,2,3, [4,5], [7,8]]
print(list_count(mixed))