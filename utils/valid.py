
def pedir_entero(mensaje):

    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("It might be a number. try again.")

def pedir_plan():

    valid_program = ["math","spanish","english"]

    while True:
        program = input("Enter your name program (Math/Spanish/English): ")
        if program in valid_program:
            return program
        else:
            print("Enter a correct program.")

def pedir_estado():

    valid_status = ["active", "inactive"]
    while True:
        status = input("Enter your status(active/inactive): ").lower()
        if status in valid_status:
            return status
        else:
            print("Enter a correct status.")

