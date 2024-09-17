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

def calculate_average(student):
    grades = student[2]
    return sum(grades)/len(grades)

        
def menu():
    print("/n student managment system")        
    print("1,Add student:")        
    print("2, Display all student")        
    print("3, Calculate student averege gardes ")        
    print("4, Remove")        
    print("5, exit") 

 
while True:
    menu()

    choise = int(input("Enter your choise:"))

    if choise == 1:
        add_student()

    elif choise == 2:
        display_student()

    elif choise == 3:
        student_name = input("Enter student name ")
        for student in students:
            if student[0] == student_name:
                avg = calculate_average(student)
                print(f"Average garade for {student_name}: {avg}/n")
                break
            else:
                print(f"student{student} not found/n")\

    elif choise == 4:
        student_name = input("Enter student name to remove")
        students = [student for studet in students if student[0]!= student_name]
        print(f"{student_name} has been removed/n")
    elif choise == 5:
        print("Exiting....")  
    else:
        print(f"invailid choise,try again. /n")   
          
      