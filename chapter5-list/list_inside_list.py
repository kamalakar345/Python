#list inside list

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[1])
print(matrix[2])
print(matrix[2])

for sublist in matrix:
    for i in sublist:
        print(i , end = "")

print(matrix[1][1])
print(matrix[2][1])

##type function 
#type function is used for which type of object

str1 = "123"
print(type(str1))

print(type(matrix))