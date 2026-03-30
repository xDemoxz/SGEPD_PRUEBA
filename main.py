from functions import show_menu,save_students,add_student,delete_student,find_student,load_students,show_student_list,update_student,register_student
from utils.valid import pedir_plan,pedir_entero,pedir_estado

clientes = load_students()

show_menu()