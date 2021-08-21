name , ini = input("enter the name and initail comma seperated").split(",")

print( f"the length of the name is {len(name)}")
print(f"the charcter {ini} count insenstive is {(name.upper()).count(ini.upper())}")
print(f"the charcter {ini} count insenstive is {name.count(ini)}")
