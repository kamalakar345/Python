#define a function that takes list of words  as argument and
# return the list rverse of the every element of list

list1 = input("enter the sequence with space separetd").split(",")
print(list1)

def reverse_every_element(l):
    liste = []
    for i in l:
        liste.append(i[::-1])
    return liste
        
            
    

print(reverse_every_element(list1))
