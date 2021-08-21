# sum of 10 number using for
# n = int(input("enter the number"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
    
# print(sum)

#Take the number from user and add all those digits

# num = input("enter the number")
# total = 0
# for i in range(0,len(num)):  # range function(0, n-1)
#     total = total + int(num[i])

# print(total)

#take the input from the user and display the count of the alphabets
name = input("Enter the name:")
temp = ""

for i in range(len(name)):
    if name[i] not in temp:
        print(f" {name[i]} : {name.count(name[i])}")
        temp +=name[i]