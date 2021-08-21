#random game guess 
import random
Wining_Number = random.randint(10,99) #use to generate random number between the given range
number1 = int(input("please  guess the number:"))

if Wining_Number == number1:
    print(f"you have won the game {Wining_number}")
else:
    if Wining_Number < number1:
        print(" please enter the larger  number")
    else:
        print("please enter the smaller number")
