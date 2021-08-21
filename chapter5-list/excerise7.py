#define a dunction which take the list as input and return the greatest diffrence in that list
list1 = input("enter the sequence with space separetd").split(",")
print(list1)

def diff_max_min(list1):
    max1 = new_func(list1)
    print(max1)
    min1 = min(list1)
    print(min1)
    return (int(max1) - int(min1))

def new_func(list1):
    max1 = max(list1)
    return max1

print(diff_max_min(list1))