#data structure
#  ordered collections of items

number = [1,2,3,4]
print(number)
print(number[0])


words = ['words', "words2", """words3"""]
print(words)
print(words[:2])

mixed = [ 1,2,3,4,"five", "six", 2.3, None]
print(mixed)
print(mixed[-1])
mixed[1] = "five"
print(mixed)

mixed[1:] = "five"
print(mixed)
mixed [1:3] = ["two", "three"]
print(mixed)
