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



#Question-6

#Question-7