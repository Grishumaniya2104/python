#Question-1

#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

#Question-2

#5
#4 5
#3 4 5
#2 3 4 5
#1 2 3 4 5

for i in range(5,0,-1):
    for j in range(i,6):
        print(j, end=" ")
    print()

#Question-3

#5
#4 4
#3 3 3 
#2 2 2 2
#1 1 1 1 1
 
for i in range(5,0,-1):
    for j in range(i,6):
        print(i, end=" ")
    print()

#Question-4

#1 2 3 4 5
#2 3 4 5
#3 4 5 
#4 5
#5

for i in range(1,6):
    for j in range(i,6):
        print(j, end=" ")
    print()


#Question-5

#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5


for i in range(1,6):
    for j in range(i,6):
        print(i, end=" ")
    print()

#1
#2 3 
#4 5 6
#7 8 9 10
#11 12 13 14 15


letters=['A','B','C','D','E']
for i in range(1,6):
    for j in range(i):
          print(letters[j], end=" ")
    print()



