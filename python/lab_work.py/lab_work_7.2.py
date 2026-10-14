#Question-1

numbers={1,2,3,4,4,5}

print("original set numbers:",numbers)

numbers.add(6)
print("set after adding:",numbers)

numbers.remove(2)
print("set after removing:",numbers)

#Question-2

person={
    "name":"Alice",
    "age":25,
    "city":"New york"
}

print("Persnol info:",person)

person["height"]=5.9
print("After adding:",person)

person["age"]=26
print("after updating age:",person)

del person["city"]
print("After removing city:",person)


#Question-3

numbers=int(input("enter a number you want to do add:"))
numberList=[]

for i in range (numbers):
    num=int(input(f"enter number {i+1}:"))
    numbers,append(num)

print("number list",numberList)
uniquevalues=set(numberList)
uniquevalues=set(numberList)

print("unique values",uniquevalues)

#Question-4

products = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Headphones": 2000,
    "Tablet": 30000
}
highest_product = max(products, key=products.get)


print("Products:", products)
print("Highest Priced Product:", highest_product)
print("Price:", products[highest_product])

#Question-5
colors=["red","blue","green","pink","pink"]
print("List of colors:",colors)

print("set of colors:",set(colors))
print("tuple of colors:",tuple(colors))
print()

vegetables=("potato","tomato","onion","garlic")
print("Tuple of vegetables :",vegetables)

print("List of vegetables :",list(vegetables))
print()


subjects = {"maths","english","science","social","maths"}
print("Set of subjects :",subjects)

print("List of subjects :",list(subjects))
print("Tuple of subjects :",tuple(subjects))
print()

#Question-6



#Question-7