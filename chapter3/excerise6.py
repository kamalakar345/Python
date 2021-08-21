#take the string from user and count the alphabet repated with individual 

Str1 = input("Enter the String:")

# if Str1:
#     print("please enter valid string")
# /else:
i = 0
while i < len(Str1):
    print(Str1[i],":",Str1.count(Str1[i]))
    i+=1