# Funciones esteticas

from math import inf
import os
import time

from glm import length
from sympy import true


# https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered/52636454#52636454
# encontramos en stackoverflow este codigo que soluciona el tema de los asterisco

try:
    from msvcrt import getch 
    def getpass(prompt,char="*"):
        print(prompt, end='', flush=True)
        buf = b''
        ch = ""
        while ch != b'\n' and ch != b'\r' and ch != b'\r\n' and ch != b'\x03':
            ch = getch()
            if ch == b'\n' or ch == b'\r' or ch == b'\r\n' or ch == b'\x03':
                print('')
            elif ch == b'\x08' or ch == b'\x7f': # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{char * len(buf)}', end='', flush=True)
            else:
                buf += ch
                print(char, end='', flush=True)
        return buf.decode(encoding='iso8859-1')

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
DELAY    = 0.025

 
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
    clear()
    cartel("En Construcción... ", AMARILLO)
    getpass("Oprima enter para volver al menu anterior\n", '')
    clear()
    
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


def menu(text = "menu",suptext="Ingrese la opcion:", opcs=[""]*10, color = VACIO):
    
    copc = 0
    cartel(text,color)
    print(suptext)
    while opcs[copc] != "" and copc < 10:
        print("\n"+BLANCO +opcs[copc][0:2]+VACIO, end="")

        for j in range(2,len(opcs[copc])):
            print(opcs[copc][j], end="",flush= True)
            time.sleep(DELAY)

        copc += 1
    print("\n")
    while True:
        print("\r"+VERDE+">>> \t", end="")
        opc = getch().decode(encoding='iso8859-1').lower()
        print(opc+VACIO, end="")
        i = 0
        while opc != opcs[i][0] and i < copc-1:
            i += 1
        
        if opc == opcs[i][0]:
            print(" "*10,opcs[i].ljust(50)[2:], end="")
        else:
            print(" "*10,ROJO+"Error, valor fuera de rango                       "+VACIO, end="")
        
    # opc == opcs[i][0]  
    # while invalido:
    #     print("\n\n"+VERDE+">>> "+VACIO, end="")
    #     opc = getch().decode(encoding='utf-8').lower()
    #     print(opc, end="")
    #     i = 0
    #     while opc != opcs[i][0] and i < copc-1:
    #         i += 1
            
    #     if opc == opcs[i][0]:
    #         invalido = False
    #     else:
    #         pass
    #         # for j in range(0,len(opc)):
    #         #     print("\b", end="",flush= True)
    #         #     time.sleep(DELAY)
                
    #         # t = "Opcion incorecta"
    #         # print(ROJO ,end="")
    #         # for j in range(0,16):
    #         #     print(t[j], end="",flush= True)
    #         #     time.sleep(DELAY)
    #         # time.sleep(1)
            
                
    #         # for j in range(0,16):
    #         #     print("\b", end="",flush= True)
    #         #     time.sleep(DELAY)
            
    clear()
    return opc
    
input()
opc = menu("Menu principal",
           
           opcs=["1. Gestionar mi perfil.",
                             "2. Gestionar candidatos.",
                             "3. Matcheos.",
                             "4. Reportes estadísticos.",
                             "0. Salir.","","",""]) 

match (opc):  
    case "1": print("Opcion 1")
    case "2": print("Opcion 2")
    case "3": print("Opcion 3")
    case "4": print("Opcion 4")
    case "0": print("Opcion 0")
