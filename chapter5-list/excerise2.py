# take the input as a list and print the list in reverse order

string1 = input("enter the sequence with space separetd").split()

print(string1)

#method 1
def reverse_1(string1):
    reverse1 = string1[-1::-1]
    return reverse1

#method2 
def reverse_2(string1):
    reverse2 = []
    reverse2 = string1.reverse()
    return string1



#using pop()  and append3
def reverse_3(string1):
    reverse3 = []
    for i in range(len(string1)):
        var1 = string1.pop()
        reverse3.append(var1)
    return reverse3

print(reverse_1(string1))
print(reverse_2(string1))
print(reverse_2(string1))
print(reverse_3(string1))
