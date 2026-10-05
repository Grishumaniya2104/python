#Question-1

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1<num2:
    if num1<num3:
        print("num1 is the minimum number")
    else:
        print("num3 is the minimum number")
else:
    if num2<num3:
        print("num2 is the minimum number")
    else:
        print("num3 is the minimum number")

#Question-2

A=10
B=30
C=20
D=5

if A>B:
    if A>C:
        if A>D:
            print("A is the maximum number.")
        else:
            print("D is the maximum number.")
    else:
        if C>D:
            print("C is the maximum number.")
        else:
            print("D is the maximum number.")
else:
    if B>C:
        if B>D:
            print("B is the maximum number.")
        else:
            print("D is the maximum number.")
    else:
        if C>D:
            print("C is the maximum number.")
        else:
            print("D is the maximum number.")

        
#Question-3

num1=int(input("Enter the number"))

print("the number is positive") if num1>0 else print("the number is negative")

#Question-4

mark=int(input("Enter your mark"))
 
print("you have passed this examination") if mark>40 else ("you have failed this examination")


#Question-5

num1=int(input("Enter a number"))

print("The number is even") if num1 %2 == 0 else print("The number is odd")
