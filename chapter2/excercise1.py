# take the three inputs from user with single input fumction \
# and take the average and display the output in string format

num1, num2, num3 = input("Enter the three number with comma seperated").split(",")
print(f"The average of 3 numbers are :{str((int(num1)+int(num2)+int(num3))/3)}")
print(f"The average of 3 numbers are :{str(round((int(num1)+int(num2)+int(num3))/3, 2))}")
