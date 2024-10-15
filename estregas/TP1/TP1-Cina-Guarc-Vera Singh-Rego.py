"""
    integrantes:

    Joaquin Ismael Guarc
    Matias Miguel Angel Rego
    Lucca Tiziano Vera Singh
    Sebastian Ezequiel Cina 

"""

# importamos los modulos que usamos

from datetime import datetime
import os
from random import randint
from time import sleep

# https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered/52636454#52636454
#
# encontramos en stackoverflow este codigo que soluciona el tema de los asterisco

try:
    from msvcrt import getch 
    def getpass(prompt,char="*"):
        print(prompt, end='', flush=True)
        buf = b''
        while True:
            ch = getch()
            if ch in {b'\n', b'\r', b'\r\n'}:
                print('')
                break
            elif ch == b'\x03': # Ctrl+C
                # raise KeyboardInterrupt
                return ''
            elif ch in {b'\x08', b'\x7f'}: # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{char * len(buf)}', end='', flush=True)
            else:
                buf += ch
                print(char, end='', flush=True)

        return buf.decode(encoding='utf-8')
except ImportError:
    from getpass import getpass  # type: ignore

def clear():
    # funcion para limpiar la consola
    # dependiendo del sistema operativo mandamos se usa el comando corespondiente 
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
# var:
# enteros: intentos    
# String: me_gusta, gmail, user1_birthdate, user2_birthdate, user3_birthdate, user1_Biography, user2_Biography, user3_Biography, user1_hobbies, user2_hobbies, user3_hobbies, user1_name, user2_name, user3_name 
#
# Constantes: 
# String: USER1_EMAIL, USER1_PASSWORD, USER2_EMAIL, USER2_PASSWORD, USER3_EMAIL, USER3_PASSWORD
 

# Datos de usuarios pre-cargados
USER1_EMAIL = "estudiante1@ayed.com"
USER1_PASSWORD = "111222"

user1_name = "Pepito Nutriales"
user1_birthdate = "2000/01/01"
user1_Biography = "Me llamo Pepito pero me pueden decir Pepe"
user1_hobbies = "Programar, leer"


USER2_EMAIL = "estudiante2@ayed.com"
USER2_PASSWORD = "333444"

user2_name = "Rayo Mcqueen"
user2_birthdate = "1998/05/15"
user2_Biography = "Me gustan las carreras"
user2_hobbies = "Pintar, viajar"


USER3_EMAIL = "estudiante3@ayed.com"
USER3_PASSWORD = "555666"

user3_name = "Myke Wazowski"
user3_birthdate = "2001/09/30"
user3_Biography = "Aguante asustar gente"
user3_hobbies = "Bailar, cocinar"


def dibujar(p1,p2,p3,pos):
    # var: 
    # enteros: p1, p2, p3, pos, is
    # String: barra
    barra = " "+"\033[1;31m"+"#"*p1+"\033[1;32m"+"#"*p2+"\033[1;34m"+"#"*p3
    
    if pos == 0:
        pos = 100

    for i in range(pos):
        clear()
        print(barra+"\n"+" "*i+"\033[1;37m-^-")
        sleep(0.01) # modificando este parametro modificas la velocidad de la animación  
          
def ruleta():
    # var: 
    # enteros: p1, p2, p3, num
    clear()
    print("\033[1;34m---------------------------------------------")
    print("|\033[0;m  \033[1;37m ingrese las probabilidades de matcheo   \033[1;34m|")
    print("|\033[0;m     \033[1;37m el valor sera valido solo cuando     \033[1;34m|")
    print("|\033[0;m  \033[1;37m las sumas de las probabilidades es 100  \033[1;34m|")
    print("---------------------------------------------\033[0;m")
    
    input("\noprima enter para empezar...")

    clear()
    p1 = int(input("\n\n\033[1;31mpersona 1: "))
    while not( p1 >= 0 and p1 <= 98):
        clear() 
        p1 = int(input("\n\n\033[1;31mpersona 1: "))
        
    clear()
    print(" "+"\033[1;31m"+"#"*p1)

    p2 = int(input("\n\033[1;31mpersona 1: "+str(p1)+"         \033[1;32mpersona 2: "))
    while not( p2 >= 0 and p2 <= 99 - p1): 
        clear()
        print(" "+"\033[1;31m"+"#"*p1)
        p2 = int(input("\n\033[1;31mpersona 1: "+str(p1)+"         \033[1;32mpersona 2: "))

    clear()
    print(" "+"\033[1;31m"+"#"*p1+"\033[1;32m"+"#"*p2) 

    p3 = int(input("\n\033[1;31mpersona 1: "+str(p1)+"          \033[1;32mpersona 2: "+str(p2)+"          \033[1;34mpersona 3: "))
    while not(p1 + p2 + p3 == 100): 
        clear()
        print(" "+"\033[1;31m"+"#"*p1+"\033[1;32m"+"#"*p2) 
        p3 = int(input("\n\033[1;31mpersona 1: "+str(p1)+"          \033[1;32mpersona 2: "+str(p2)+"          \033[1;34mpersona 3: "))

    clear()
    print(" "+"\033[1;31m"+"#"*p1+"\033[1;32m"+"#"*p2+"\033[1;34m"+"#"*p3) 
    print("\n\033[1;31mpersona 1: "+str(p1)+"          \033[1;32mpersona 2: "+str(p2)+"          \033[1;34mpersona 3: "+str(p3))

    input("\n\033[0;mlos datos son correctos, presione enter para iniciar la ruleta...")
    num = randint(1,100)

    for i in range(0,randint(3,5)):        
        dibujar(p1,p2,p3,0)

    dibujar(p1,p2,p3,num)

    print("\033[1;31mpersona 1: "+str(p1)+"          \033[1;32mpersona 2: "+str(p2)+"          \033[1;34mpersona 3: "+str(p3))

    print("\n\033[1;37m")
    if num <= p1:
        print("la persona elegida es la \033[1;31mnumero 1")
    elif num > p1 and num <=p1+p2:
        print("la persona elegida es la \033[1;32mnumero 2")
    elif num > p1+p2:
        print("la persona elegida es la \033[1;34mnumero 3")
    print("\033[0;m")

    getpass("oprima enter para volver al menu anterior\n", '')
    clear()  

def login(gmail,password):
    #var:
    #String: USER1_EMAIL, USER2_EMAIL, USER3_EMAIL, gmail
    #Entero: USER1_PASSWORD, USER2_PASSWORD, USER3_PASSWORD, password
    
    if USER1_EMAIL == gmail and USER1_PASSWORD == password:
        gmail = USER1_EMAIL
        return True
    
    if USER2_EMAIL == gmail and USER2_PASSWORD == password:
        gmail = USER2_EMAIL
        return True
    
    if USER3_EMAIL == gmail and USER3_PASSWORD == password:
        gmail = USER3_EMAIL
        return True
    
    return False

def validar_fecha():
    # var:
    # datetime: fecha_nacimiento
    
    ok = True
    while ok:
        try:
            fecha_nacimiento = input("escriba su fecha de nacimiento en formato aaaa/mm/dd\n")

            
            if datetime.strptime(fecha_nacimiento, "%Y/%m/%d") < datetime.now():
                
                print("Fecha válida")
                ok = False
            else:
                clear() 
                print("Fecha inválida") 
        except:
            clear()
            print("Fecha inválida")
    return fecha_nacimiento

def calcular_edad(fecha_nacimiento):
    #var:
    #Datatime: fecha_nacimiento ; fecha_actual ; fecha_actual.year ; fecha_nacimiento.year ;fecha_actual.month ; fecha_nacimiento.month ; fecha_actual.day ; fecha_nacimiento.day
    #Entero: edad
    
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
        edad -= 1
    return edad

def invalido():
    clear()
    print("\033[1;31mDato Invalido, ingreselo de nuevo\033[0;m")

def construcción():
    clear()
    print("\033[1;34m--------------------------------------")
    print("|\033[0;m        \033[1;37mEn Construcción...          \033[1;34m|")
    print("--------------------------------------\033[0;m\n")
    getpass("oprima enter para volver al menu anterior\n", '')
    clear()
 
def editar_datos():
    # var:
    # String: user1_birthdate, user2_birthdate, user3_birthdate, user1_Biography, user2_Biography, user3_Biography, user1_hobbies, user2_hobbies, user3_hobbies, gmail, USER1_EMAIL, USER2_EMAIL, USER3_EMAIL
    # Caracter: opc

    global user1_name, user2_name, user3_name, user1_birthdate, user1_hobbies, user1_Biography, user2_birthdate, user2_hobbies, user2_Biography, user3_birthdate, user3_hobbies, user3_Biography
    if gmail == USER1_EMAIL:
        
        name = user1_name
        birthdate = user1_birthdate
        hobbies = user1_hobbies
        Biography = user1_Biography

    elif gmail == USER2_EMAIL:
        name = user2_name
        birthdate = user2_birthdate
        hobbies = user2_hobbies
        Biography = user2_Biography

    elif gmail == USER3_EMAIL:
        name = user3_name
        birthdate = user3_birthdate
        hobbies = user3_hobbies
        Biography = user3_Biography

    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="e":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mEditar Mis Datos            \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("¿Cual de sus datos deseas editar?\n")
        print("\033[1;37ma\033[0;m. Fecha De Nacimiento.")
        print("\033[1;37mb\033[0;m. Hobbies.")
        print("\033[1;37mc\033[0;m. Biografia.")
        print("\033[1;37md\033[0;m. Nombre.")
        print("\033[1;37me\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        if opc == "a":
            clear()
            print("tu fecha de nacimiento actual es:",birthdate)
            birthdate = validar_fecha()

            clear()
            print("tu fecha de nacimiento ahora es: ",birthdate)
            if gmail == USER1_EMAIL:
                user1_birthdate = birthdate

            elif gmail == USER2_EMAIL:
                user2_birthdate = birthdate    
            
            elif gmail == USER3_EMAIL:
                user3_birthdate = birthdate 

        elif opc == "b": 
            clear()
            print("tus hobbies actuales son:", hobbies)
            hobbies = input("escriba sus hobbies\n")
            clear()
            print("tus hobbies ahora seran:", hobbies)
            if gmail == USER1_EMAIL:
                user1_hobbies = hobbies 

            elif gmail == USER2_EMAIL:
                user2_hobbies = hobbies  
            
            elif gmail == USER3_EMAIL:
                user3_hobbies = hobbies
            
        elif opc == "c":
            clear()
            print("tu biografia actual es:", Biography)
            Biography = input("escriba su biografia\n")
            clear()
            print("tu biografia ahora sera:", Biography)
            if gmail == USER1_EMAIL:
                user1_Biography = Biography 

            elif gmail == USER2_EMAIL:
                user2_Biography = Biography     
            
            elif gmail == USER3_EMAIL:
                user3_Biography = Biography
                 
        elif opc == "d":
            clear()
            print("tu nombre actual es:", name)
            name = input("escriba su nombre\n")
            clear()
            print("tu nombre ahora sera:", name)
            if gmail == USER1_EMAIL:
                user1_name = name 

            elif gmail == USER2_EMAIL:
                user2_name = name     
            
            elif gmail == USER3_EMAIL:
                user3_name = name 
        
        elif opc == "e":
            clear()
        
        else:
            invalido()

def menu_perfil():
    # Var:
    # Caracter: opc

    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="c":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mGestionar mi perfil         \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37ma\033[0;m. Editar mis datos personales.")
        print("\033[1;37mb\033[0;m. Eliminar mi perfil.")
        print("\033[1;37mc\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match opc:
            case "a": editar_datos()     
            case "b": construcción()            
            case "c": clear()
            case  _ : invalido()

def menu_candidatos():
    # var:
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="c":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mGestionar candidatos        \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37ma\033[0;m. Ver candidatos.")
        print("\033[1;37mb\033[0;m. Reportar un candidato.")
        print("\033[1;37mc\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match opc:
            case "a": menu_ver_candidatos()
            case "b": construcción()            
            case "c": clear()
            case  _ : invalido()      
        
def menu_ver_candidatos():
    # var:
    # String: user1_birthdate, user2_birthdate, user3_birthdate, user1_hobbies, user2_hobbies, user3_hobbies, user1_Biography, user2_Biography, user3_Biography, gmail, USER1_EMAIL, USER2_EMAIL, USER3_EMAIL, me_gusta
    # Caracter: opc

    global me_gusta, gmail
    
    opc = ""
    
    pos = 1
   
    while opc != "r":
        clear()
        opc = ""
        match pos:
            case 1: 
                print("\033[1;34m--------------------------------------\033[0;m")
                print("\033[1;34m|\033[0;mNombre             : ",user1_name)
                print("\033[1;34m|\033[0;mFecha de nacimiento: ",user1_birthdate)
                print("\033[1;34m|\033[0;mEdad               : ",calcular_edad(user1_birthdate))
                print("\033[1;34m|\033[0;mHobbies            : ",user1_hobbies)
                print("\033[1;34m|\033[0;mBiografia          : ",user1_Biography)
                print("\033[1;34m--------------------------------------\033[0;m")
                
                if gmail == USER1_EMAIL:
                    print("Estos son tus datos actuales")
                    
                    if me_gusta != "":
                        print("Le diste me gusta a: ",me_gusta)
                    else:
                        print("Aun no le diste me gusta a nadie ")
                    
                    print("r. Para regresar al menu principal")
                    print("                                s.siguiente")
                    
                    while opc != "r" and opc != "s":
                        opc = input("\033[1;34m>>> \033[0;m")
                        
                    if opc == "s":
                        pos += 1
                
                else:  
                    if me_gusta != "":
                        print("Le diste me gusta a: ",me_gusta)
                    else:
                        print("Aun no le diste me gusta a nadie ")
                    
                    print("r. Para regresar al menu principal")
                    print("                           m. Me gusta                s. Pagina siguiente")
                   
                    while opc != "m" and opc != "r" and opc != "s":
                        opc = input("\033[1;34m>>> \033[0;m")
                    if opc == "m":
                        me_gusta = user1_name
                    elif opc == "s":
                        pos += 1
                        
            case 2: 
                print("\033[1;34m--------------------------------------\033[0;m")
                print("\033[1;34m|\033[0;mNombre             : ",user2_name)
                print("\033[1;34m|\033[0;mFecha de nacimiento: ",user2_birthdate)
                print("\033[1;34m|\033[0;mEdad               : ",calcular_edad(user2_birthdate))
                print("\033[1;34m|\033[0;mHobbies            : ",user2_hobbies)
                print("\033[1;34m|\033[0;mBiografia          : ",user2_Biography)
                print("\033[1;34m--------------------------------------\033[0;m")
                
                if gmail == USER2_EMAIL:
                    print("Estos son tus datos actuales")
                    
                    if me_gusta != "":
                        print("Le diste me gusta a: ",me_gusta)
                    else:
                        print("Aun no le diste me gusta a nadie ")
                        
                    print("r. Para regresar al menu principal")
                    print("a. Pagina anterior                                    s. Pagina siguiente")
                    
                    while opc != "a" and opc != "r" and opc != "s":
                        opc = input("\033[1;34m>>> \033[0;m")
                    if opc == "a":
                        pos -= 1
                    elif opc == "s":
                        pos += 1
                
                else:
                    if me_gusta != "":
                        print("Le diste me gusta a: ",me_gusta)
                    else:
                        print("Aun no le diste me gusta a nadie ")
                      
                    print("r. Para regresar al menu principal")
                    print("a. Pagina anterior         m. Me gusta                s. Pagina siguiente")
                    
                    while opc != "a" and opc != "m" and opc != "r" and opc != "s":
                        opc = input("\033[1;34m>>> \033[0;m")
                    if opc == "a":
                        pos -= 1
                    elif opc == "m":
                        me_gusta = user2_name
                    elif opc == "s":
                        pos += 1
            
                        
            case 3: 
                print("\033[1;34m--------------------------------------\033[0;m")
                print("\033[1;34m|\033[0;mNombre             : ",user3_name)
                print("\033[1;34m|\033[0;mFecha de nacimiento: ",user3_birthdate)
                print("\033[1;34m|\033[0;mEdad               : ",calcular_edad(user3_birthdate))
                print("\033[1;34m|\033[0;mHobbies            : ",user3_hobbies)
                print("\033[1;34m|\033[0;mBiografia          : ",user3_Biography)
                print("\033[1;34m--------------------------------------\033[0;m")
                
                if gmail == USER3_EMAIL:
                    print("Estos son tus datos actuales")
                    
                    if me_gusta != "":
                        print("Le diste me gusta a: ",me_gusta)
                    else:
                        print("Aun no le diste me gusta a nadie ")
                        
                    print("r. Para regresar al menu principal")
                    print("a. Pagina anterior")
                    
                    while opc != "a" and opc != "r":
                        opc = input("\033[1;34m>>> \033[0;m")
                    if opc == "a":
                        pos -= 1
                
                else: 
                    if me_gusta != "":
                        print("Le diste me gusta a: ",me_gusta)
                    else:
                        print("Aun no le diste me gusta a nadie ") 
                          
                    print("r. Para regresar al menu principal")
                    print("a. Pagina anterior         m. Me gusta")
                    
                    while opc != "a" and opc != "m" and opc != "r":
                        opc = input("\033[1;34m>>> \033[0;m")
                    if opc == "a":
                        pos -= 1
                    elif opc == "m":
                        me_gusta = user3_name
    
    clear()

def menu_Matcheos():
    # var:
    # Caracter: opc
    
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="c":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mMatcheos                    \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37ma\033[0;m. Ver matcheos.")
        print("\033[1;37mb\033[0;m. Eliminar un matcheo.")
        print("\033[1;37mc\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()  
        match opc:
            case "a": construcción()            
            case "b": construcción()            
            case "c": clear()
            case  _ : invalido() 


me_gusta = ""
gmail = ""
intentos = 3

clear()
print("\033[1;34m--------------------------------------")
print("|\033[0;m        \033[1;37minicio de sesion            \033[1;34m|")
print("--------------------------------------\033[0;m")
print("ingrese sus credenciales.\n")

gmail = input("Gmail:\n\033[1;34m>>> \033[0;m")
print("\nIngrese su contraseña:")
password = getpass("\033[1;34m>>> \033[0;m","*")
intentos -= 1
while not (login(gmail,password)) and intentos> 0:
    clear()
    print("\033[1;34m--------------------------------------")
    print("|\033[0;m        \033[1;37minicio de sesion            \033[1;34m|")
    print("--------------------------------------\033[0;m")
    print("\033[1;31mcredenciales incorrectas\033[0;m")
    print("le quedan ",intentos," intentos restantes")
    print("intente nuevamente\n")

    gmail = input("Gmail:\n\033[1;34m>>> \033[0;m")
    print("\nIngrese su contraseña:")
    password = getpass("\033[1;34m>>> \033[0;m","*")

    if not (login(gmail,password)):
        intentos -= 1
        
clear()

if intentos==0:
    
    print("\033[1;31m     Demasiados intentos incorrectos\033[0;m")
else:
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mMenu principal              \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37m1\033[0;m. Gestionar mi perfil.")
        print("\033[1;37m2\033[0;m. Gestionar candidatos.")
        print("\033[1;37m3\033[0;m. Matcheos.")
        print("\033[1;37m4\033[0;m. Reportes estadísticos.")
        print("\033[1;37m5\033[0;m. Ruleta.")
        print("\033[1;37m0\033[0;m. Salir.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match (opc):  
            case "1": menu_perfil()
            case "2": menu_candidatos()
            case "3": menu_Matcheos()
            case "4": construcción()
            case "5": ruleta()
            case "0": pass
            case  _ : invalido()

print("           \033[1;37mFin del programa           ")
print("       \033[1;37mGracias por visitarnos.         \n\033[0;m")

print("""########       ########       ########
 #######       ########       #######
  ########     ########     ########
   #########   ########   #########         
      ##########################            Progarma echo por:
          ##################               
######################################        -Joaquin Ismael Guarc.
######################################        -Matias Miguel Angel Rego.
######################################        -Lucca Tiziano Vera Singh.
         ####################                 -Sebastian Ezequiel Cina.
     ############################
   #########   ########   #########
  ########     ########     ########
 #######       ########       #######
 #######       ########       #######""")