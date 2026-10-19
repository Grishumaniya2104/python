# #Question-1

 students=[
   {"id":1, "name":"Alice","marks":85},
     {"id":2, "name":"Bob", "marks":78}
     ]



 print("student details:")

 for student in students:
     print("name:",student["name"])
     print("marks", student["marks"])
    

#Question-2


 students = [
     {"id": 1, "name": "Alice", "marks": 85},
     {"id": 2, "name": "Bob", "marks": 78}
 ]

 student_id = int(input("Enter student ID: "))
 name = input("Enter student name: ")
 marks = int(input("Enter student marks: "))

 new_student = {
     "id": student_id,
     "name": name,
     "marks": marks
 }

 students.append(new_student)

 print("Updated Student List:")

 for student in students:
     print(student)


#Question-3

 students = [
     {"id": 1, "name": "Alice", "marks": 85},
     {"id": 2, "name": "Bob", "marks": 78}
 ]


# search_id=int(input("enter student id to search"))

 found=False

 for student in students:
     if student["id"]==search_id:
         print("student found")
         print(student["id"])
         print(student["name"])
         print(student["marks"])

         found=True

 if not found:
     print("student with this id not found")


#Question-4


students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

student_id = int(input("Enter student ID to update: "))

found = False

for student in students:
    if student["id"] == student_id:
        new_marks = int(input("Enter new marks: "))
        student["marks"] = new_marks
        found = True
        print("Marks updated successfully!")
        break

if not found:
    print("Student not found.")

print("Updated Student List:")

for student in students:
    print(student)


#Question-5



students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

student_id = int(input("Enter student ID to delete: "))

found = False

for student in students:
    if student["id"] == student_id:
        students.remove(student)
        found = True
        print("Student deleted successfully!")
        break

if not found:
    print("Student not found.")

print("Updated Student List:")

for student in students:
    print(student)

#Question-6

#Question-7
students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78},
    {"id": 3, "name": "Rahul", "marks": 92},
    {"id": 4, "name": "Priya", "marks": 80}
]

print("Students who scored more than 80 marks:")

for student in students:
    if student["marks"] > 80:
        print(student)

