import os
import time
ROJO    = "\033[91m"
VERDE   = "\033[92m"
AMARILLO= "\033[93m"
AZUL    = "\033[94m"
CYAN    = "\033[96m"
RESET   = "\033[0m"
NEGRITA = "\033[1m"

def clean():
    os.system("cls" if os.name == "nt" else "clear")

def loading(text_message):
    print(CYAN + text_message, end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print(RESET)

def mensaje(text, color=RESET, negrita=False):
    estilo = ""
    
    if negrita:
        estilo += NEGRITA
    
    estilo += color
    
    print(f"{estilo}{text}{RESET}")
