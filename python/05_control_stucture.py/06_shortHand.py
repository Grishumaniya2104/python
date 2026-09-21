mark=80;
if(mark>=35):
    print("you have passed this examination")
else:
    print("you have failed this examination")


#short hand syntex

mark=35

print("you have pass this exam")if mark>=35 else print("you have fail this exam")


#example-1

age=18

print("you can give vote")if age>=18 else print("you can not give vote ")


#example-2

drivingLicense=17

print("you can drive this car")if drivingLicense>=20 else print("you can not drive this car")

#lab work-3 que 1

num1=int(input("enter num1:-"))
num2=int(input("enter num2:-"))
num3=int(input("enter num3:-"))


if a<=b:
    if a<=c:
        print(f"{a} is smallest")
    else: 
        print(f"{c} is smallest")
if b<=c:
    print(f"{b} is smallest")
else:
     print(f"{c} is smallest")


    #

num=int(input("enter numbers:-"))

if (num%2==0):
    print(f"{num}num is even number")
else:
    print(f"{num}num is odd number")