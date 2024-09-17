student = {}

def add_student(name,age,marks):
    student[name] = {"age": age,"marks":marks}



def update_student(name,age=None,marks=None):
    if name in student:
        if age:
            student[name][age] = "age"
            student[name][marks] = "marks" 
        else:
            print("student not found")    

def delete_student(name):
    student.pop(name, "student not found")


def print_student(name):
    student.get(name,"student not found")


add_student("amit", 28, 100)
update_student("amit", marks=80)
delete_student("amit")
print_student("amit")












