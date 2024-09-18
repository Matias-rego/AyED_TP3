# Funciones esteticas

from math import inf
import os

from glm import length


# https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered/52636454#52636454
# encontramos en stackoverflow este codigo que soluciona el tema de los asterisco

try:
    from msvcrt import getch 
    def getpass(prompt,char="*"):
        print(prompt, end='', flush=True)
        buf = b''
        ch = ""
        while not ch in {b'\n', b'\r', b'\r\n', b'\x03'}:
            ch = getch()
            
            if ch == b'\x08' or ch == b'\x7f': # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{char * len(buf)}', end='', flush=True)
            else:
                buf += ch
                print(char, end='', flush=True)
        return buf.decode(encoding='utf-8')

except ImportError:
    from getpass import getpass  # type: ignore

VACIO    = "\033[0;m"
ROJO     = "\033[1;31m"
VERDE    = "\033[1;32m" 
AMARILLO = "\033[1;33m" 
AZUL     = "\033[1;34m" #Estudiante y logueo
VIOLTEA  = "\033[1;35m" #Administrador
CIAN     = "\033[1;36m" #Moderador
BLANCO   = "\033[1;37m"

 
def clear():
    # funcion para limpiar la consola
    # dependiendo del sistema operativo mandamos se usa el comando corespondiente 
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def invalido():
    clear()
    print("\033[1;31mDato Invalido, ingreselo de nuevo\033[0;m")

def construcción():
    # clear()
    cartel("En Construcción... ", AMARILLO)
    getpass("Oprima enter para volver al menu anterior\n", '')
    # clear()
    
def cartel(text = "", color = VACIO):
    
    print(color+"╔"+"═"*48+"╗")
 
    inf = 0
    while len(text) > inf + 46:
        med = inf + 46
        while text[med] != " ":
            med -= 1
        
        print("║ "+BLANCO+text[inf:med].center(46)+color+" ║")
        inf = med + 1

    print("║ "+BLANCO+text[inf:len(text)].center(46)+color+" ║")
    
    print(color+"╚"+"═"*48+"╝"+VACIO)
