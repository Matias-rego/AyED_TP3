# Funciones esteticas

from datetime import datetime
import os
import time
from msvcrt import getch 

def clear(): ...

if os.name == "nt":
    def clear():
        os.system("cls")
    from msvcrt import getch
    
else:
    def clear():
        os.system("clear")

    try:
        from getch import getch

    except ImportError:
        print("error de importacion de la libreria getch")
        os.system("pip install getch")
        from getch import getch
#------------------------------------------------------COLORES----------------------------------------------------------#  
#COLORES PARA CONSOLA
VACIO    = "\033[0;m"
ROJO     = "\033[1;31m"
VERDE    = "\033[1;32m" 
AMARILLO = "\033[1;33m" 
AZUL     = "\033[1;34m" #Estudiante y logueo
VIOLTEA  = "\033[1;35m" #Administrador
CIAN     = "\033[1;36m" #Moderador
BLANCO   = "\033[1;37m"
DELAY    = 0.025        #DELAY UTILIZADO PARA LAS ANIMACIONES DE PRESENTACION DE MENUS
#--------------------------------------------FUNCIONES VARIAS--------------------------------------------------#
#FUNCION PARA VALIDAR LA FECHA DE NACIMIENTO
def validar_fecha():
    # Var:
    # String: fecha_nacimiento
    # Bool: ok
    valida = False      
    cartel("      Introduzca su fecha de nacimiento          En formato YYYY/MM/DD", AZUL)
    while not valida:
        
        try:
            fecha_nacimiento = input("\n\033[1;34m>>> \033[0;m")
            
            if datetime.strptime(fecha_nacimiento, "%Y/%m/%d") < datetime.now():
                clear()
                print("Fecha válida")
                valida = False
            else:
                clear() 
                print("Fecha inválida") 
        except:
            clear()
            print("Fecha inválida")
    return fecha_nacimiento
#FUNCION QUE AUTOGENERA MENUS, PASANDOLE EL TEXTO REQUERIDO
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
#FUNCION PARA VALIDAR CONTRASEÑA, SEGUN LOS PARAMETROS DADOS
def getpass(ver = False, cartel =True):
    if cartel: 
        print("ingrese su contraseña de 6 a 16 caracteres:\n(con tab haces visible la contraseña)\n")
    password = b''
    print(BLANCO+" (---) "+VERDE+">>"+" "*18+"<<", end="\r", flush=True)
    ch = ""
    while ch != b"\r":
        ch = getch()
        men = " "
        
        if ch == b"\r":
            if len(password) < 6:
                men = "El minimo de la contraseña es de 6 caracteres"
                ch = b""

        elif ch == b" ":
            men = "La contraseña no puede contener espacios"
            
        elif ch == b"\t":
            ver = not ver
            
        elif ch == b"\b":
            p = b""
            for i in range(0,len(password)-1):
                p += bytes([password[i]])
            password = p
            men = " "
        
        else:
            if len(password) != 16:
                password += ch
            else:
                men = "El maximo de la contraseña es de 16 caracteres"
                      
        if ver:
            print(BLANCO+" (<o>) "+VERDE+">> "+VACIO+password.ljust(16,b" ").decode(encoding='iso8859-1') +VERDE+ " << " +AMARILLO+men.ljust(50," "), end="\r", flush=True)
        
        else:
            l = len(password)
            print(BLANCO+" (---) "+VERDE+">> "+VACIO+l*"*"+(16-l)*" "+VERDE+ " << " +AMARILLO+men.ljust(50," "), end="\r", flush=True)
    print(VACIO)
    return password.ljust(16,b" ").decode(encoding='iso8859-1')

def invalido():
    clear()
    print("\033[1;31mDato Invalido, ingreselo de nuevo\033[0;m")
#FUNCION PARA LOS APARTADOS EN CONSTRUCCION(GENERA EL CARTEL Y EL MENSAJE)
def construcción():
    clear()
    cartel("En Construcción... ", AMARILLO)
    print("Oprima enter para volver al menu anterior\n", end="")
    getch()
    clear()
#FUNCION QUE CREA UN CARTEL AL REDEDOR DEL NOMBRE DEL MENU
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
    # print(getpass())
    
    validar_fecha()