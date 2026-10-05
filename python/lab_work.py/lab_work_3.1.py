#Question-1

num1=int(input("Enter a number:"))

if num1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Question-2

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if num1<=num2:
    print("The minimum number is first number.")
else:
    print("The minimum number is second number.")


#Question-3

num1=int(input("Enter a number:"))

if num1>0:
    print("The number is positive")
elif num1<0:
    print("The number is negative")
else:
    print("The number is neutral")

#Question-4

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))


if num1>num2 and num2>num3:
    print(num1,"The first number is the largest")
elif num3>num1 and num3>num2:
    print(num3,"The third number is the largest")
else:
    print(num2,"The second number is largest")


#second type

if num1>num2:
    if num1>num3:
        print("The first number is the largest")
    else:
        print("The third number is the largest")
else:
    if num2>num3:
        print("The second number is largest")
    else:
        print("The third number is the largest")

#Question-5

num1=int(input("Enter first number:"))
num2-int(input("Enter second number:"))

operator=input("Enter an operator(+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    print("Result =", num1 / num2)
    
else:
    print("Invalid operator")






    


