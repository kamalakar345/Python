# define a function which take input as  a list and return a list of even and odd 
list1 = input("enter the sequence with space separetd").split(",")
print(list1)

def odd_and_even(list1):
    even = []
    odd = []
    for i in list1:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    #return (even.append(odd)) #return none
    #return even + odd  # ['2', '6', '8', '7', '9']
    return [odd, even]
    


print(odd_and_even(list1))