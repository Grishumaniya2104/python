print("welcome to the data")


students = [
    {"id": 1, "name": "Rahul", "marks": 85},
    {"id": 2, "name": "Priya", "marks": 92},
    {"id": 3, "name": "Amit", "marks": 76},
    {"id": 4, "name": "Neha", "marks": 88}
]

print("1.add a new student")
print("2. Display all students' name and marks")
print("3. Remove a student")
print("4. Update student mark")
print("5. Search student by ID")
print("6. sort student by marks")
print("7. Diplay students scoring more than 80")
print("8. End")

choice=int(input("Enter your choice from the above options:-"))

if choice == 1:
    student_id=int(input("Enter student ID:-"))
    name=input("Enter student name:-")
    marks=int(input("Enter student marks:-"))

    new_student={
        "id":student_id,
        "name":name,
        "marks":marks

    }

    students.append(new_student)
    print("student added successfully")
    print(students)

elif choice == 2:
    for student in students:
        print("Name:",student["name"])
        print("Marks:",student["marks"])

elif choice == 3:
    student_id=int(input("Enter student ID to remove"))
    found=False

    for student in students:
        if student ["id"] == student_id:
            students.remove(student)
            print("students remove successfully")
            found=True
            break

        if not found:
            print("student not found")


elif choice == 4:
    student_id=int(input("Enter students ID:-"))
    found=False


    for student in students:
        if student["id"] == student_id:
            student["marks"]=int(input("Enter new marks:-"))
            print("marks updated successfully")
            found=True
            break

        if not found:
            print("Student not found")
            print("Updated list:",students)

elif choice == 5:
    student_id=int(input("Enter student ID to search:-"))
    found=False 

    for student in students:
        if student["id"]== student_id:
            print("ID:",student["id"])
            print("Name:",student["name"])
            print("Marks:",student["marks"]) 
            found=True
            break
    if not found:
        print("student not found") 

elif choice == 6:
    students.sort(key=lambda student: student["marks"],reverse=True)
    print("Student sorted by marks:-")
    for student in students:
        print(student)

elif choice == 7:
    print("student scoring more than 80 marks:")
    found=False

    for student in students:
        if student["marks"]>80:
            print(student)
            found=True

    if not found:
        print("No students scored more than 80 marks.")


elif choice == 8:
    print("Thank you for using the program")
    
    
else:
    print("end program")