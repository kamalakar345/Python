num1 , num2 , num3 = input("Enter two number comma seperated").split(",")
a = int(num1)
b = int(num2)
c = int(num3)

def greater1( a, b):
    if a > b:
        return a 
    return b 



def greater2(num1,num2,num3):
    bigger = greater1(num1, num2)
    return greater1(bigger, num3)
print(greater2(num1,num2,num3), "is greater")

