# variable assignment
name , age = "kamal" , 30

x = y =z = 30

print(name, " ", age)
print(f"x = {x} = y = {y} = z = {z}")

# enter multiple inputs on same line

name , age = input("Enter the  name and age").split() # by default split func has "space"
print(name,age)

name , age = input("Enter the  name and age by comma seperated").split(",") # split func has ",""
print(name,age)