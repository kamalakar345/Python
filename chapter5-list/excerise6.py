#define a function which will take input as 2 list and return a list of common elements in these 2 lists

list1 = input("enter the sequence with space separetd").split()
print(list1)

list2 = input("enter the sequence with space separetd").split(",")
print(list2)

def common_list(l,m):
    k = []
    if len(l) < len(m):
        for mn in m:
            if mn in l:
                k.append(mn)
    else:
        for mn in l:
            if mn in m:
                k.append(mn)
    return k
print("###########")
print(common_list(list1,list2))