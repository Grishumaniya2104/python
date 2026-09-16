# AND OR NOT

#and= both condition have to be true then and then code will be execute

age=18

drivingLicense = True

if age>=18 and drivingLicense == True:
    print("you can drive vehical")
else:
    print("you can't drive vehical")

#exampal-1

age = 20
id_card = True

if age >= 18 and id_card == True:
    print("You can enter the exam")
else:
    print("You cannot enter the exam")

#example-2

age=20
time = True

if age >= 20 and time == True:
    print("you can enter the school")
else:
    print("you can not enter the school")

#example-3

age=10
play = True

if age >= 10 and play == True:
    print("you can play in the school")
else:
    print("you can not play in the school")

#or oprator= if one condition is true then you the block of code will be execute

driving=True
seatbelt=False

if driving==True or seatbelt==False:
    print("you can drive vehical but it's not safe")
else:
    print("you can't drive vehical")

#example-1

drive=True
car=False

if drive==True  or car==False:
    print("you can drive car but not safe")
else:
    print("you can't drive car")



#example-2
house=True
play=False

if house==True or play==False:
    print("you can play in house")
else:
    print("you can't play in house")


#example-3
school=True
cricket=False

if school==True or cricket==False:
    print("you can play the cricket")
else:
    print("you can't play the cricket")


#not

print("not driving") 