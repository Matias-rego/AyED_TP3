# Funciones esteticas

import os
import time
from msvcrt import getch 

VACIO    = "\033[0;m"
ROJO     = "\033[1;31m"
VERDE    = "\033[1;32m" 
AMARILLO = "\033[1;33m" 
AZUL     = "\033[1;34m" #Estudiante y logueo
VIOLTEA  = "\033[1;35m" #Administrador
CIAN     = "\033[1;36m" #Moderador
BLANCO   = "\033[1;37m"
DELAY    = 0.025

# # https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered/52636454#52636454
# # encontramos en stackoverflow este codigo que soluciona el tema de los asterisco

# try:
#     from msvcrt import getch 
#     def getpass(prompt,char="*"):
#         print(prompt, end='', flush=True)
#         buf = b''
#         ch = ""
#         while ch != b'\n' and ch != b'\r' and ch != b'\r\n' and ch != b'\x03':
#             ch = getch()
#             if ch == b'\n' or ch == b'\r' or ch == b'\r\n' or ch == b'\x03':
#                 print('')
#             elif ch == b'\x08' or ch == b'\x7f': # Backspace
#                 buf = buf[:-1]
#                 print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{char * len(buf)}', end='', flush=True)
#             else:
#                 buf += ch
#                 print(char, end='', flush=True)
#         return buf.decode(encoding='iso8859-1')

# except ImportError:
#     from getpass import getpass  


def menu(text = "menu",suptext="Ingrese la opcion:", opcs=[""]*10, color = VACIO):
    
    copc = 0
    cartel(text,color)
    print(suptext)
    while opcs[copc] != "" and copc < 9:
        copc += 1
    
    for i in range(0,copc+1):
        print("\n"+BLANCO +opcs[i][0:2]+VACIO, end="")

        for j in range(2,len(opcs[i])):
            print(opcs[i][j], end="",flush= True)
            time.sleep(DELAY)
    if opcs[copc] == "": copc -= 1
        
    print("\n"+" "*100)
    preopc = ""
    opc = ""
    print(VERDE+" >>> ", end="\r")
    ispreopc = False
    while opc != "\r":
        preopc = opc
        opc = getch().decode(encoding='iso8859-1').lower() #iso8859-1
        
        # me fijo si lo que el usuario ingreso es una opcion valida.
        i = 0
        while i < copc and opc != opcs[i][0] :
            i += 1
      
        
        # si en una opcion valida le muestro la opcion. 
        if opc == opcs[i][0]:
            ispreopc = True
            print("\r"+VERDE+" >>> "+VACIO+opc+VERDE+" <<<"+" "+VACIO+opcs[i][3:].ljust(50), end="\r",flush= True)
        
        # si es un enter 
        elif opc == "\r":
            if ispreopc:
                print("\r"+VERDE+" --- "+VACIO+preopc+VERDE+" ---"+" "+VERDE+"Opcion seleccionada."+" "*31, end="\r",flush= True)
                time.sleep(DELAY*10)
                print("\r"+VERDE+" >>> "+VACIO+preopc+VERDE+" <<<", end="\r",flush= True)
            else:
                print("\r"+VERDE+" --- "+ROJO+preopc+VERDE+" ---"+" "+ROJO+preopc+": No es una opcion valida!!!"+" "*22, end="\r",flush= True)
                time.sleep(DELAY*5)
                print("\r"+VERDE+" >>> "+ROJO+preopc+VERDE+" <<<", end="\r",flush= True)
                opc = " "
                
        elif opc == "\t" or opc == "\b":
            ispreopc = False
            print("\r"+VERDE+" >>> "+AMARILLO+" "+VERDE+" <<<"+" "+AMARILLO+"Opcion invalida."+" "*36, end="\r",flush= True)
            
        # si no es ninguno de los casos anteriores muestro una advertencia. 
        else:
            ispreopc = False
            print("\r"+VERDE+" >>> "+AMARILLO+opc+VERDE+" <<<"+" "+AMARILLO+"Opcion invalida."+" "*36, end="\r",flush= True) 
    print(VACIO)
    clear()
    return preopc

def getpass(ver = 1):
    print("ingrese su contraseña de 6 a 16 caracteres:\n(con tap haces visible la contraseña)")
    ojo= ["(---)","(<o>)"]
    password = b''
    men = " m"
    print(" "+ojo[ver]+" >>>", end="\r", flush=True)
    ch = ""
    while ch != b"\r":
        ch = getch()
        
        if ch == b"\r":
            men = "enter"
            
        elif ch == b"\t":
            men = "tap"
            
        elif ch == b"\b":
            men = "borrar"
        
        else:
            men = ch.decode(encoding='iso8859-1') + " " + str(ch) 
                      
        
        print(" "+ojo[ver]+" >>> "+password.ljust(16,b" ").decode(encoding='iso8859-1')+ " " +men.ljust(50," "), end="\r", flush=True)


def clear():
    # funcion para limpiar la consola
    # dependiendo del sistema operativo se usa el comando corespondiente 
    
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

    

if __name__ == "__main__":
    getpass()
    # opc = menu("Menu principal", opcs=[
    # "1. Gestionar mi perfil.",
    # "2. Gestionar candidatos.",
    # "3. Matcheos.",
    # "4. Reportes estadísticos.",
    # "5. Opcion5",
    # "6. Opcion6",
    # "7. Opcion7",
    # "8. Opcion8",
    # "9. Opcion9",
    # "0. Salir."]) 