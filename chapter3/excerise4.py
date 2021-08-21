# Ask user to input a number containing more than one digit 
#and add them example -1245 calculate 1+2+4+5

number = input("enter the number to add :")
sum = 0
mul = 1

if len(number)==1:
    print("Sum of number is:", number)
elif len(number) > 1:
    i = 0
    while i <= (len(number)- 1) :
        sum  = sum + int(number[i])
        i+=1
        print(i)
    
    
else:
    print("please enter the valid number")

print(sum)
print(mul)