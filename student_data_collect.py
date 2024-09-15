students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = tuple(map(int,input("Enter student grades (separated with space):").split()))

    student = name,age,grades
    students.append(student)
    print(f"{name} has been added.")

def display_student():
    if not students:
        print("No student display ")
        return
    
    for student in students:
        print(f"name : {student[0]} age : {student[1]},grades: {student[2]} ")
        
def menu():
    print()        