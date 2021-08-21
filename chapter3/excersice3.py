#Ticket price based on given age 
#Show ticket priceing
# 1 to 3 (free)
# 4 to 10 (150)
#11 to 60 (250)
# abov 61 (250)

age = int(input( "Enter the age:" ))

if  1 < age < 3:
    print("tiket price is :FREE")
elif  4 < age < 10:
    print("ticket price is :250")
elif 11 < age < 60:
    print("ticket price is :250")
else:
    print("ticket price is :250")