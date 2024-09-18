import os
import pickle
from consola import * 
from registros import * 

ruta_estudiantes     = "src/archivos/estudiantes.dat"
ruta_moderadores     = "src/archivos/moderadores.dat"
ruta_administradores = "src/archivos/administradores.dat"
ruta_likes           = "src/archivos/likes.dat"
ruta_reportes        = "src/archivos/reportes.dat"

def abrir_archivos():
    
    global logico_estudiantes, logico_moderadores, logico_administradores, logico_likes, logico_reportes
     
    if os.path.exists (ruta_estudiantes):
        logico_estudiantes = open(ruta_estudiantes, "r+b")
    else:
        logico_estudiantes = open(ruta_estudiantes, "w+b") 
        
    if os.path.exists (ruta_moderadores):
        logico_moderadores = open(ruta_moderadores, "r+b")
    else:
        logico_moderadores = open(ruta_moderadores, "w+b")
        regis_mod()
        
    if os.path.exists (ruta_administradores):
        logico_administradores = open(ruta_administradores, "r+b")
    else:
        logico_administradores = open(ruta_administradores, "w+b")
        
    if os.path.exists (ruta_likes):
        logico_likes = open(ruta_likes, "r+b")
    else:
        logico_likes = open(ruta_likes, "w+b")
        
    if os.path.exists (ruta_reportes):
        logico_reportes = open(ruta_reportes, "r+b")
    else:
        logico_reportes = open(ruta_reportes, "w+b")
        
def busca_email(email) -> bool:
    pass
        
def regis_mod():
    print("\033[1;34m--------------------------------------")
    print("|\033[0;m\033[1;37m Ingrese los datos del moderador:\033[1;34m|")
    print("--------------------------------------\033[0;m\n")
    
    email = input("Ingrese el email del moderador: \n\033[1;34m>>> \033[0;m")

    while busca_email(email) :
        invalido()
        email = input("\n\033[1;34m>>> \033[0;m")
    moderadores[i][0] = email
    moderadores[i][1] = input("\nIngrese la contraseña del moderador: \n\033[1;34m>>> \033[0;m")
    
        
# def menu_registrarse(text="         Registrar usuario          ",ispassword =True):
#     # (moderadores: M_2x4_str, estudiantes: M_8x8_str, text: str, ispassword: bool)
#     # Var
#     # Entero: pos,
#     # String:email, password1, password2
#     clear()
#     pos = busca_estud(estudiantes,"",2)

#     if pos >=0:

#         print("\033[1;34m--------------------------------------")
#         print("|\033[0;m\033[1;37m"+text+"\033[1;34m|")
#         print("--------------------------------------\033[0;m\n")
        
#         print("\033[1;37m Ingrese su email.")
#         email = input("\n\033[1;34m>>> \033[0;m")
            
#         print("\033[1;37m Ingrese su contraseña.")
#         password1 = input("\n\033[1;34m>>> \033[0;m")
#         if ispassword:
#             print("\033[1;37m Repita su contraseña.")
#             password2 = input("\n\033[1;34m>>> \033[0;m")
#         else:
#             password2 = password1

#         while busca_estud(estudiantes,email,0)>=0 or email == "" or password1 == "" or password1 != password2 or busca_mod(moderadores,email)>=0:
#             clear()
#             print("\033[1;34m--------------------------------------")
#             print("|\033[0;m\033[1;37m"+text+"\033[1;34m|")
#             print("--------------------------------------\033[0;m\n")
            
#             if email == "":
#                 print("Tiene que ingresar un email.")
#             elif busca_estud(estudiantes,email,0)>=0 or busca_mod(moderadores,email)>=0:
#                 print("El email ingresado ya esta en uso")
#             else: 
#                 print("")
#             print("\033[1;37m Ingrese su email.")
#             email = input("\n\033[1;34m>>> \033[0;m")

#             if password1 != password1: 
#                 print("Las contraseñas no son identicas. Ingreselas nuevamente")
                
#             print("\033[1;37m Ingrese su contraseña.")
#             password1 = input("\n\033[1;34m>>> \033[0;m")
            
#             if ispassword:
#                 print("\033[1;37m Repita su contraseña.")
#                 password2 = input("\n\033[1;34m>>> \033[0;m")
#             else:
#                 password2 = password1
            
#         estudiantes[pos][0] = email
#         estudiantes[pos][1] = password1
#         estudiantes[pos][2] = "ACTIVO"
        
#         clear()
#         print("\033[1;34m--------------------------------------")
#         print("|\033[0;m\033[1;37m"+text+"\033[1;34m|")
#         print("--------------------------------------\033[0;m\n")
            
#         print("Te has registrado exitosamente")
#         print("a continuación, ingrese sus datos personales")
        
#         print("Ingrese su nombre y apellido ")
#         estudiantes [pos] [3] = input("\n\033[1;34m>>> \033[0;m")
        
#         print("Ingrese su biografía  ")
#         estudiantes [pos] [5] = input("\n\033[1;34m>>> \033[0;m")
        
#         print("Ingrese sus hobbies ")
#         estudiantes [pos] [6] = input("\n\033[1;34m>>> \033[0;m")
        
#         opc = input("\nIngrese su sexo (m/f): \n\033[1;34m>>> \033[0;m")
#         while opc != "m" and opc != "f":
#             invalido()
#             opc = input("\033[1;34m>>> \033[0;m")
        
#         estudiantes [pos] [7] = opc
        
#         clear()
#         estudiantes [pos] [4] = validar_fecha()
#     else:
#         print("\033[1;34m--------------------------------------")
#         print("|\033[0;m\033[1;37m Error, se ha alcanzado la cantidad \033[1;34m|")
#         print("|\033[0;m\033[1;37m   maxima de usuarios disponibles   \033[1;34m|")
#         print("--------------------------------------\033[0;m\n")
#         getpass("oprima enter para volver al menu anterior\n", '')
#     clear()
        
def cerrar_programa():
    
    global logico_estudiantes, logico_moderadores, logico_administradores, logico_likes, logico_reportes
    
    logico_estudiantes.close()
    logico_moderadores.close()
    logico_administradores.close()
    logico_likes.close()
    logico_reportes.close()
    
    print("           \033[1;37mFin del programa           ")
    print("       \033[1;37mGracias por visitarnos.         \n\033[0;m")

    print("""########       ########       ########
#######       ########       #######
########     ########     ########
#########   ########   #########         
    ##########################            Programa hecho por:
        ##################               
######################################        -Nicolás Fossati
######################################        -Matias Miguel Angel Rego
######################################        -Marcos Banducci
        ####################                 -Tomas Agusti
    ############################
#########   ########   #########
########     ########     ########
#######       ########       #######
#######       ########       #######""")
        
if __name__ == "__main__":
    abrir_archivos()
    cerrar_programa()