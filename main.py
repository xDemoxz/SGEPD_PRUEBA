from functions import *
from utils.valid import *

clientes = load_students()

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
show_menu()