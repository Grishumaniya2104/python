#Question-1

numbers=[1,2,3,4,5,6,7,8,9,10]

numbers.append(11)

print("updated list:",numbers)


#question-2

num1=int(input(how many numbers do you want to add in the list))

numberList=[]

for i in range (total number):
    num=int(input(f"enter number{i+1}:"))
    numberList.append(num)

    maxnumber = max(numberList)

    minnumber=min(numberList)

    maxnumber=

#question-3

numbers=(1,2,2,3,4,4,5)
unique_value = set(numbers)

print("tuple:",numbers)
print("unique_value:",unique_value)



#Question-4

numbers=[10,20,30,40,50]
numbers[2]=35
print(numbers)

#Question-5


my_list = [1, [2, 3], 4]

print("Original List:", my_list)


my_list[1][0] = 20
my_list[1].append(30)


print("Updated List:", my_list)



#Question-6

numbers = [10, 20, 30, 40]

print("Original list:", numbers)

numbers.append(50)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

numbers[1] = 100
print("After replacing:", numbers)

#Question-7

data=([1,2],[3,4],[5,6])

print("orignal Tuple:",data)

data[0].append(10)

print("updated Tuple:",data)

#Question-8

a= 10
b= 20
c=""

print("before a:",a)
print("before b:",b)

c=a #c=10
a=b #a=20
b=c #b=10

print("after a:",a)
print("after b:",b)

#Question-9

a=10
b=20

print("before a:",a)
print("before b:",b)

a=a+b  #a=30
b=a-b  #b=10

a=a-b  #a=20

print("after a:",a)
print("after b:",b)