#typeCasting function

#int()
#float()
#string()
#bool()
#set()
#list()
#tuple()
#dict()







#num1=int(input("enter first value:-"))
#num2=int(input("enter second value:-"))

#print("total",num1+num2);

#num1= input("enter first value:-")
#num2= input("enter second value:-")

#print("total",int(num1)+int(num2))

#implicit=> compiler will automatically convert one data types to another data type

num1 = 100

num2 = 24.24

print("result2",num1+num2)

#explicit

print("result2",int(num1+num2))
# explicit => we have to forcefully convert one data types to another datatypes


num1= input("enter  first value:- ")


num2=input("enter second value:- ")

#print("total",int(num1)+int(num2))


#example-1
# str covert int

num1="10"
num2="20"

print("result2",int(num1)+int(num2))

#int convert flot
#example-2

num1=10
num2=10

print("result2",float(num1)+float(num2))

#flot convert str
#example-3

num1=10.5
num2=20.5

print("result2",str(num1)+str(num2))

#str covert bool
#example-4

name="Grishma"
name="maniya"

print("result2",bool(name))

#bool convert list
#example-5

num1=[True]
num1+[False]
print("result2",list(num1))


#list convert tuple
#example-6

num1=[20, 30, 40, 50]
num2=[40, 30, 20, 10]
print("result2",tuple(num1))

#tuple convert set
#example-7

num1=(20, 30, 40, 50)
num2=(60, 70, 80, 90)

print("result",set(num1))


#set convert dict
#example-8

num1=("name","grishma"),("age","18")
print("result2",dict(num1))

#dict conver none
#example-9
num1=("name":"grishma")
print("result2",none(num1))









