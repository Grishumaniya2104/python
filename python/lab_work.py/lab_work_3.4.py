#Question-1

#          1
#        2 1
#      3 2 1 
#    4 3 2 1 
#  5 4 3 2 1

for i in range(1,6):
    for s in range(i,5):
        print(" ", end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#Question-2

#         5
#       4 5
#     3 4 5 
#   2 3 4 5
# 1 2 3 4 5


for i in range(5, 0, -1):
    for s in range(i - 1):
        print("  ", end="")
        
    for j in range(i, 6):
        print(j, end=" ")
        
    print()




