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