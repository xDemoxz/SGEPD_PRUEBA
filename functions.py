import json
import os
from utils.valid import pedir_entero,pedir_estado,pedir_plan


def show_menu():

    while True:
        print("\n STUDENTS MANAGMENT SYSTEM")

        print("1. Register Student")
        print("2. Show Students")
        print("3. Find Student")
        print("4. Update Student")
        print("5. Delete Student")
        
        print("6. EXIT")
            
        option = input("Enter a option: ")

        if option == "1":
            id = pedir_entero("Enter your ID: ")
            if find_student(students,id) is not None:
                print("\n ID already exists.")
            else:
                name = input("Enter your name: ")
                age = pedir_entero("Enter your age: ")
                program = pedir_plan()
                status = pedir_estado()
            
                student = register_student(students, id, name, age, program, status)
                add_student(students, student)
                save_students(students)

        elif option == "2":
            show_student_list(students)

        elif option =="3":
            id = pedir_entero("Enter your ID: ")
            result = find_student(students,id)
            if result is not None:
                print(f"ID: {result['id']} | name: {result['name']} | Edad: {result['age']} | Program: {result['program']} | Status: {result['status']} ")
            else:
                print("El ID no ha sido registrado antes.")

        elif option =="4":
            id = pedir_entero("Digite el ID a actualizar: ")
            result= find_student(students, id)
            if result is None:
                print("ID no encontrado.")
                continue
            new_name = input("Digite su nuevo nombre: ")
            new_age = pedir_entero("Digite su nueva edad: ")
            new_program = pedir_plan()
            new_status = pedir_estado()


            update_student(students, id, new_name, new_age, new_program, new_status)
            save_students(students)

        elif option =="5":
            id = pedir_entero("Digite ID del cliente a eliminar: ")
            delete_student(students,id)
        elif option =="6":
            print("\nHASTA LUEGO!!!")
            break
    else:
        print("\nIngrese una opcion valida, por favor.")


def register_student(students, id, name, age, program,status):

    student = {
            'id':id,
            'name':name,
            'age': age,
            'program': program,
            'status':status,
    }

    print("Student added succesfully.")
    return student


def add_student(students,student):
    students.append(student)


def show_student_list(students):

    if len(students) ==0:
        print("\nNo students registered yet.")
    else:
        for student in students:
            print(f"ID: {student['id']} | Name:{student['name']} | Age:{student['age']} | Program:{student['program']} | Status:{student['status']} ")        


def find_student(students, id, ):

    for student in students:
        if student['id'] == id:
            return student
    else:
        return None        


def update_student(students,id, new_name, new_age, new_program, new_status):
    student = find_student(students, id)

    if student is not None:
        student['name'] = new_name
        student['age'] = new_age
        student['program'] = new_program
        student['status'] = new_status
        print("Student updated.")


def delete_student(students, id):

    student = find_student(students,id)

    if student is not None:
        students.remove(student)
        print(f"Student '{student['name']}' of '{student['id']}' ID have been deleted.")  
    else:
        print("Student have not found.")  


def save_students(students):
    with open("students.json", "w") as f:
        json.dump(students,f, indent=4)


def load_students():
    if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            return json.load(f)
    return []           

students = load_students()
