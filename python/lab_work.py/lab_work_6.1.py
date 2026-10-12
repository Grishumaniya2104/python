#Question-1

firstname=input("Enter your first name : ")
lastname=input("Enter your last name : ")

print(f"Hello {firstname} {lastname}!")

#Question-2

item ="Apple"
price = 5.500

print(f"The price of {item} is {price :.3f} dollars.")

#Question-3

name=input("Enter your name : ")

print(f"Entered name : {name}")

palindrome= name[::-1]

if palindrome==name:
    print("Given name is palindrome.")
else:
    print("Given name is not palindrome.")

#Question-4

text = input("Enter some text : ")

print(text.upper())

print(text.lower())

print(text.title())

#Question-5

charecters='abcdefghijklmnop'

print(len(charecters))

name=input("Enter your name : ")

print(len(name))