#function to define which number is greater

num1 , num2  = input("Enter two number comma seperated").split(",")
a = int(num1)
b = int(num2)

def greater1( a, b):
    if a > b:
        return a 
    return b 

print(greater1(num1,num2), "is greater")