"""
    Integrantes:
    
    Nicolás Fossati
    Matias Miguel Angel Rego
    Marcos Banducci
    Tomas Agusti
    
    comisión: ISI 101
"""


# importamos los modulos que usamos

from datetime import datetime
import os
from random import randint
from consola import * 


    
#type:
#   M_8x8_str = array[0..7,0..7] of String
#   M_2x4_str   = array[0..1,0..4] of String
#   M_8x8_int    = array[0..7,0..7] of int
#   M_6_int = array [0...6] of int
        
# var:
# enteros: id 
# String: opc
# M_8x8_str: estudiantes, reportes_m
# M_2x4_str: moderadores
# M_8x8_int: likes, reportes_s

# datos 



estudiantes = [[""]*8 for _ in range(0,8)]

moderadores = [[""]*2 for _ in range(0,4)]

likes = [[0]*8 for _ in range(0,8)]

reportes_s = [[0]*8 for _ in range(0,8)]
reportes_m  = [[""]*8 for _ in range(0,8)]



# funciones de datos
def inicialización(likes, estudiantes, moderadores):
    #(likes: M_8x8_int, estudiantes: M_8x8_str, moderadores: M_8x8_str)
    # Var
    # Entero:i,j
    # String: opc
    
    
    
    for i in range(0,8):
        for j in range(0,8):
            if i != j:
                likes[i][j] = randint(0,1)
            else:
                likes[i][j] = 0

    for i in range(0,4):
        menu_registrarse(moderadores, estudiantes,"   Ingrese el "+str(i+1)+"° usuario inicial:   ",False) 
        
    opc = "si"
    i = 0
    
    clear()
    
    while opc != "no" and i<4:
        
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m\033[1;37m Ingrese los datos del "+str(i+1)+"° moderador:\033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        
        email = input("Ingrese el email del moderador: \n\033[1;34m>>> \033[0;m")

        while busca_estud(estudiantes,email,0)>=0 or busca_mod(moderadores,email)>=0 :
            invalido()
            email = input("\n\033[1;34m>>> \033[0;m")
        moderadores[i][0] = email
        moderadores[i][1] = input("\nIngrese la contraseña del moderador: \n\033[1;34m>>> \033[0;m")
        if i < 3:
            opc = input("Desea ingresar otro moderador?\n(si/no): \033[1;34m>>> \033[0;m")
            clear()
            while opc != "si" and opc != "no":
                invalido()
                opc = input("Desea ingresar otro moderador?\n(si/no): \033[1;34m>>> \033[0;m")
        
            
        i += 1
    clear()


def validar_fecha():
    # Var:
    # String: fecha_nacimiento
    # Bool: ok
    ok = True
    while ok:
        try:
            print("\033[1;34m--------------------------------------")     
            print("|\033[0;m \033[1;37mIntroduzca su fecha de nacimiento  \033[1;34m|")
            print("|\033[0;m       \033[1;37mEn formato YYYY/MM/DD        \033[1;34m|")
            print("--------------------------------------\033[0;m\n")
            fecha_nacimiento = input("\n\033[1;34m>>> \033[0;m")
            
            if datetime.strptime(fecha_nacimiento, "%Y/%m/%d") < datetime.now():
                clear()
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
    # (fecha_macimiento: str)
    # Var:
    # Datatime: fecha_actual ; fecha_actual.year ; fecha_nacimiento.year ;fecha_actual.month ; fecha_nacimiento.month ; fecha_actual.day ; fecha_nacimiento.day
    # Entero: edad

    
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
        edad -= 1
    return edad

def busca_estud(estud,dato,tipo):#YA PASADA
    # (estudiantes: M_8x8_str, dato: str, tipo: int)
    # Var
    # Entero:i
    
    i = 0
    while estud[i][tipo] != dato and i < 7:
        i = i + 1
      
    if estud [i][tipo] == dato:
        return i
    else: 
        return -1
     
def busca_mod(mod,dato):#YA PASADA
    # (mod: M_2x4_str, dato: str)
    # Var
    # Entero:i
    
    i = 0
    while mod[i][0] != dato and i < 3:
        i = i + 1
      
    if mod [i][0] == dato:
        return i
    else: 
        return -1
    
def is_login(email,password,user1,user2):
    # (email:str, password:str, user1: M_8x8_str, user2: M_2x4_str)
    # Var
    # Entero:i
    
    if email != "" and password != "":
        i = 0
        while not (user1[i][0] == email and user1[i][1] == password and user1[i][2] == "ACTIVO") and i != 7: 
            i += 1
            
        if user1[i][0] == email and user1[i][1] == password:
            return i
        
        else:
            i = 0
            while not (user2[i][0] == email and user2[i][1] == password) and i != 3: 
                i += 1
                
            if user2[i][0] == email and user2[i][1] == password:
                return i + 8
            else:
                return -1
    else:
        return -1

def deshabilitar_estud(estudiantes,id,text= "      ¿Desea eliminar su perfil?    "):
    #(estudiantes: M_8x8_str, id: int, text: srt)
    # Var
    # String: Respuesta
    print("\033[1;34m--------------------------------------")     #
    print("|\033[0;m\033[1;37m"+str(text)+"\033[1;34m|")
    print("|\033[0;m            \033[1;37mSI o NO                 \033[1;34m|")
    print("--------------------------------------\033[0;m")  
    
    opc = input("\n\033[1;34m>>> \033[0;m")
    while opc != "si" and opc != "no":
        invalido()
        opc = input("\n\033[1;34m>>> \033[0;m")
    
    if opc == "si" :
        estudiantes[id][2] = "INACTIVO"
        print("Perfil desactivado.")

    else :
        print("Perfil no desactivado.")
    getpass("oprima enter para volver al menu anterior\n", '')
    clear()
    

# menus prinsipales de nivel 1

def menu_logueo(estudiantes,moderadores):
    # (estudiantes: M_8x8_str, moderadores: M_2x4_str,)
    # Var
    # Entero: login_e, intentos
    # String: email, password
    login_e = -1 
    intentos = 3
    
    while login_e == -1 and intentos > 0:
        clear()
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m           \033[1;37mInicio de sesion         \033[1;34m|")
        print("--------------------------------------\033[0;m")
        
        if intentos == 3:
            print("Ingrese sus credenciales.\n")
            
        else:
            print("\033[1;31mCredenciales incorrectas\033[0;m")
            print("Te quedan ",intentos," intentos restantes")
            print("Intente nuevamente\n")
    
        email = input("email:\n\033[1;34m>>> \033[0;m")
        print("\nIngrese su contraseña:")
        password = getpass("\033[1;34m>>> \033[0;m","*")
        
        login_e = is_login(email,password,estudiantes,moderadores) 
    
        if login_e == -1:
            intentos -= 1
            
    clear()
    
    if intentos==0:
        
        print("\033[1;31m     Demasiados intentos incorrectos\033[0;m")
        
    return login_e

def menu_estudiante(estudiantes, id, likes, reportes_s, reportes_m):
    # (estudiantes: M_8x8_str, id: int,likes: M_8x8_int, reportes_s: M_8x8_int, reportes_m: M_8x8_str)
    # Var
    # String: opc 
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0" and estudiantes[id][2] == "ACTIVO":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mMenu principal              \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37m1\033[0;m. Gestionar mi perfil.")
        print("\033[1;37m2\033[0;m. Gestionar candidatos.")
        print("\033[1;37m3\033[0;m. Matcheos.")
        print("\033[1;37m4\033[0;m. Reportes estadísticos.")
        print("\033[1;37m0\033[0;m. Salir.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match (opc):  
            case "1": menu_perfil(estudiantes, id)
            case "2": menu_candidatos(estudiantes, id, likes, reportes_s, reportes_m)
            case "3": menu_Matcheos()
            case "4": menu_reportes_estadisticos(estudiantes, id, likes)
            case "0": pass
            case  _ : invalido()

def menu_moderadores(estudiantes, reportes_s, reportes_m):
    # (estudiantes: M_8x8_str, reportes_s: M_8x8_int, reportes_m: M_8x8_str)
    # Var
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m   \033[1;37mMenu principal de moderadores    \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37m1\033[0;m. Gestionar Usuarios.")
        print("\033[1;37m2\033[0;m. Gestionar Reportes.")
        print("\033[1;37m3\033[0;m. Reportes estadísticos.")
        print("\033[1;37m0\033[0;m. Salir.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match (opc):  
            case "1": menu_gest_usuario(estudiantes)
            case "2": menu_gest_reportes(estudiantes, reportes_s, reportes_m)
            case "3": construcción()
            case "0": pass
            case  _ : invalido()

def menu_registrarse(moderadores,estudiantes,text="         Registrar usuario          ",ispassword =True):
    # (moderadores: M_2x4_str, estudiantes: M_8x8_str, text: str, ispassword: bool)
    # Var
    # Entero: pos,
    # String:email, password1, password2
    clear()
    pos = busca_estud(estudiantes,"",2)

    if pos >=0:

        print("\033[1;34m--------------------------------------")
        print("|\033[0;m\033[1;37m"+text+"\033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        
        print("\033[1;37m Ingrese su email.")
        email = input("\n\033[1;34m>>> \033[0;m")
            
        print("\033[1;37m Ingrese su contraseña.")
        password1 = input("\n\033[1;34m>>> \033[0;m")
        if ispassword:
            print("\033[1;37m Repita su contraseña.")
            password2 = input("\n\033[1;34m>>> \033[0;m")
        else:
            password2 = password1

        while busca_estud(estudiantes,email,0)>=0 or email == "" or password1 == "" or password1 != password2 or busca_mod(moderadores,email)>=0:
            clear()
            print("\033[1;34m--------------------------------------")
            print("|\033[0;m\033[1;37m"+text+"\033[1;34m|")
            print("--------------------------------------\033[0;m\n")
            
            if email == "":
                print("Tiene que ingresar un email.")
            elif busca_estud(estudiantes,email,0)>=0 or busca_mod(moderadores,email)>=0:
                print("El email ingresado ya esta en uso")
            else: 
                print("")
            print("\033[1;37m Ingrese su email.")
            email = input("\n\033[1;34m>>> \033[0;m")

            if password1 != password1: 
                print("Las contraseñas no son identicas. Ingreselas nuevamente")
                
            print("\033[1;37m Ingrese su contraseña.")
            password1 = input("\n\033[1;34m>>> \033[0;m")
            
            if ispassword:
                print("\033[1;37m Repita su contraseña.")
                password2 = input("\n\033[1;34m>>> \033[0;m")
            else:
                password2 = password1
            
        estudiantes[pos][0] = email
        estudiantes[pos][1] = password1
        estudiantes[pos][2] = "ACTIVO"
        
        clear()
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m\033[1;37m"+text+"\033[1;34m|")
        print("--------------------------------------\033[0;m\n")
            
        print("Te has registrado exitosamente")
        print("a continuación, ingrese sus datos personales")
        
        print("Ingrese su nombre y apellido ")
        estudiantes [pos] [3] = input("\n\033[1;34m>>> \033[0;m")
        
        print("Ingrese su biografía  ")
        estudiantes [pos] [5] = input("\n\033[1;34m>>> \033[0;m")
        
        print("Ingrese sus hobbies ")
        estudiantes [pos] [6] = input("\n\033[1;34m>>> \033[0;m")
        
        opc = input("\nIngrese su sexo (m/f): \n\033[1;34m>>> \033[0;m")
        while opc != "m" and opc != "f":
            invalido()
            opc = input("\033[1;34m>>> \033[0;m")
        
        estudiantes [pos] [7] = opc
        
        clear()
        estudiantes [pos] [4] = validar_fecha()
    else:
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m\033[1;37m Error, se ha alcanzado la cantidad \033[1;34m|")
        print("|\033[0;m\033[1;37m   maxima de usuarios disponibles   \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        getpass("oprima enter para volver al menu anterior\n", '')
    clear()


# menu Gestionar mi perfil de nivel 2 dentro de menu estudiantes   
def menu_perfil(estudiantes, id):
    # (estudiantes: M_8X8_str, id: int)
    # Var:
    # String: opc

    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="c" and estudiantes[id][2] == "ACTIVO" :
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mGestionar mi perfil         \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37ma\033[0;m. Editar mis datos personales.")
        print("\033[1;37mb\033[0;m. Eliminar mi perfil.")
        print("\033[1;37mc\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match opc:
            case "a": menu_editar_datos(estudiantes, id)     
            case "b": deshabilitar_estud(estudiantes, id)            
            case "c": clear()
            case  _ : invalido()

def menu_editar_datos(estudiantes, id):
    # (estudiantes: M_8X8_str, id: int)
    # var:
    # String: opc
    

    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="f":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mEditar Mis Datos            \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("¿Cual de sus datos deseas editar?\n")
        print("\033[1;37ma\033[0;m. Fecha De Nacimiento.")
        print("\033[1;37mb\033[0;m. Hobbies.")
        print("\033[1;37mc\033[0;m. Biografia.")
        print("\033[1;37md\033[0;m. Nombre.")
        print("\033[1;37me\033[0;m. Sexo.")
        print("\033[1;37mf\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        if opc == "a":
            clear()
            print("Tu fecha de nacimiento actual es:",estudiantes[id][4])
            estudiantes[id][4] = validar_fecha()

            clear()
            print("Tu fecha de nacimiento ahora es: ",estudiantes[id][4])
            

        elif opc == "b": 
            clear()
            print("Tus hobbies actuales son:", estudiantes[id][6])
            estudiantes[id][6] = input("Escriba sus nuevos hobbies: \n")
            clear()
            print("Tus hobbies ahora seran:", estudiantes[id][6])
          
        elif opc == "c":
            clear()
            print("Tu biografia actual es:", estudiantes[id][5])
            estudiantes[id][5] = input("Escriba su nueva biografia: \n")
            clear()
            print("Tu biografia ahora sera:", estudiantes[id][5])
            
                 
        elif opc == "d":
            clear()
            print("Tu nombre actual es:", estudiantes[id][3])
            estudiantes[id][3] = input("Escriba su nombre: \n")
            clear()
            print("Tu nombre ahora sera:", estudiantes[id][3])
           
        elif opc == "e":
            clear()
            print("Tu sexo actual es:", estudiantes[id][7])
            
            sexo = input("Ingrese su sexo (m/f): \n\033[1;34m>>> \033[0;m")
            while sexo != "m" and sexo != "f":
                invalido()
                sexo = input("\033[1;34m>>> \033[0;m")
        
            estudiantes [id] [7] = sexo
            
            clear()
            print("Tu sexo ahora sera:", estudiantes[id][7])
        
        elif opc == "f":
            clear()
        
        else:
            invalido()

# menu Gestionar candidatos de nivel 2 dentro de menu estudiantes 
def menu_candidatos(estudiantes, id, likes, reportes_s, reportes_m):
    # (estudiantes: M_8X8_str, id: int, likes: M_8X8_int, reportes_s: M_8x8_int, reportes_m: M_8X8_str)
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
            case "a": menu_ver_candidatos(estudiantes, id, likes)
            case "b": menu_reportar(estudiantes, id, reportes_s, reportes_m)            
            case "c": clear()
            case  _ : invalido()      


def menu_ver_candidatos(estudiantes, id, likes):
    # (estudiantes: M_8x8_str, id: int, likes: M_8x8_int)
    # var:
    # String: me_gusta, opc
    # Entero: j, i, pos
    # Arreglo:poss, opcs, 
    poss = [-1]*8
    j = 0
    for i in range(0,8):
        if estudiantes[i][2] == "ACTIVO":
            poss[j] = i
            j += 1
    
    j -= 1
    opc = ""
    pos = 0
   
    clear()
    while opc != "r":
        
        opc = ""
        print("\033[1;34m--------------------------------------\033[0;m")
        print("\033[1;34m|\033[0;mEmail              : ",estudiantes[poss[pos]][0])
        print("\033[1;34m|\033[0;mNombre             : ",estudiantes[poss[pos]][3])
        print("\033[1;34m|\033[0;mFecha de nacimiento: ",estudiantes[poss[pos]][4])
        print("\033[1;34m|\033[0;mEdad               : ",calcular_edad(estudiantes[poss[pos]][4]))
        print("\033[1;34m|\033[0;mBiografia          : ",estudiantes[poss[pos]][5])
        print("\033[1;34m|\033[0;mHobbies            : ",estudiantes[poss[pos]][6])
        print("\033[1;34m|\033[0;msexo               : ",estudiantes[poss[pos]][7])
        print("\033[1;34m--------------------------------------\033[0;m")
        
        opcs = ["r"]*3
        
        if poss[pos] == id:
            print("Estos son tus datos actuales")
            
        me_gusta = ""    
        for i in range(0,j+1):
            if likes[id][poss[i]] == 1:
                if me_gusta != "":
                    me_gusta = me_gusta + ", " 
                me_gusta = me_gusta + str(estudiantes[poss[i]][3])
                
        if me_gusta != "":
            print("Le diste like a: ", me_gusta)        
        else:
            print("Aun no le diste like a nadie ")
    
    
        print("r. Para regresar al menu principal")
        if pos <= j and pos >0:
            print("a. Pagina anterior         ",end="")
            opcs[0] = "a"
        else:
            print("                           ",end="")
        
        if pos != id:
            if likes[id][pos] == 0:
                print("m. Dar Like         ",end="")
            else:
                print("m. Quitar Like      ",end="")
            opcs[1] = "m"
            
        else:
            print("                    ",end="")
            
        if pos >= 0 and pos < j:
            print("s. Pagina siguiente")
            opcs[2] = "s"
        else:
            print("                   ")
            
        opc = input("\033[1;34m>>> \033[0;m")
        clear()
        if opc == "r": clear()
        elif opc == opcs[0] : pos -= 1
        elif opc == opcs[1] : 
            if likes[id][poss[pos]] == 0:
                likes[id][poss[pos]] = 1
            else:
                likes[id][poss[pos]] = 0
        elif opc == opcs[2] : pos += 1
        else: invalido()

def menu_reportar(estudiantes, id_1, reportes_s, reportes_m):
    # (estudiantes: M_8X8_str, id_1: int, reportes_s: M_8x8_int, reportes__m: M_8X8_str) 
    # Var
    # String: email, motivo
    # Entero: id
    
    id_2= -1
    
    while id_2 == -1 or id_2 == id_1:
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m          \033[1;37mReportar usuario          \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("Ingrese el email del usuario a reportar")
        
        if id_2 == id_1:
            print("no te puedes reportar a ti mismo")

        email = input("\n\033[1;34m>>> \033[0;m")
        id_2 = busca_estud(estudiantes,email,0)
        
        clear()
        if id_2 == -1:
            invalido()
        
    print("\033[1;34m--------------------------------------")
    print("|\033[0;m          \033[1;37mReportar usuario          \033[1;34m|")
    print("--------------------------------------\033[0;m")
    
    if reportes_s[id_1][id_2] == 0:
        print("\nIngrese el motivo del reporte")               
        reportes_m[id_1][id_2] = input("\n\033[1;34m>>> \033[0;m")
        reportes_s[id_1][id_2] = 1
    
    print("\nUsuario ya reportado")
    print("El motivo fue: ",reportes_m[id_1][id_2])
    print("El reporte: ",end="")
    
    match reportes_s[id_1][id_2]:
        case 1: print("no ha sido visto")
        case 2: print("ha sido exitoso")
        case 3: print("ha sido ignorado")
        
    getpass("oprima enter para volver al menu anterior\n", '')
    clear()

# menu Gestionar candidatos de nivel 2 dentro de menu estudiantes
def menu_Matcheos():
    # var:
    # string: opc
    
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

# menu Reportes estadísticos de nivel 2 dentro de menu estudiantes
def menu_reportes_estadisticos(estudiantes,id, likes) :
    # (estudiantes: M_8x8_str, id: int, likes: M_8x8_int)
    # Var
    # Entero: cont_like, like_norec, like_nodev, c_est
    # float: por_match
    clear()
    cont_like = 0
    like_norec = 0
    like_nodev = 0
    por_match = 0.0
    c_est = 0
    
    while estudiantes[c_est][0] != "" and c_est < 7:
        c_est += 1
    
    if estudiantes[c_est][0] != "":
        c_est += 1

    for i in range(0,c_est):
        if likes [id] [i] == 1 and likes [i] [id] == 1:
            cont_like += 1

        if likes [id] [i] == 1 and likes [i] [id] == 0:
            like_norec += 1

        if likes [id] [i] == 0 and likes [i] [id] == 1:
            like_nodev += 1
            
    por_match = (cont_like * 100) / c_est

    print("\033[1;34m--------------------------------------")
    print("|\033[0;m        \033[1;37mReportes Estadísticos       \033[1;34m|")
    print("--------------------------------------\033[0;m\n")
    print("\033[1;37m*\033[0;m Matcheados sobre el % posible: ",por_match,"%" )
    print("\033[1;37m*\033[0;m Likes dados y no recibidos: ", like_norec)
    print("\033[1;37m*\033[0;m Likes recibidos y no repondidos: ", like_nodev)
    
    getpass("\nOprima enter para volver al menu anterior", '')
    clear()

# menu Gestionar usuarios de nivel 2 dentro de menu moderadores 
def menu_gest_usuario(estudiantes):
    # (estudiantes: M_8x8_str)
    # Var
    # String: opc
    opc= ""
    
    while opc!="b":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m          \033[1;37mGestionar usuarios        \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37ma\033[0;m. Desactivar usuario.")
        print("\033[1;37mb\033[0;m. Volver.")

        opc = input("\n\033[1;34m>>> \033[0;m")  

        clear()
        match opc:
            case "a": menu_desactivar_usuario(estudiantes)
            case "b": clear()

def menu_desactivar_usuario(estudiantes):
    # (estudiantes: M_8x8_str)
    # Var
    # Entero: id
    # String: opc

    opc = ""
    
    while opc!="1" and opc!="2":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m         \033[1;37mDesactivar usuario         \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37m1\033[0;m. con id.")
        print("\033[1;37m2\033[0;m. con email de usuario.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")
        clear()
        if opc!="1" and opc!="2":
            invalido()

    id = -1
    
    if opc == "1":
        while id < 0 or id > 7:
            print("\033[1;34m--------------------------------------")
            print("|\033[0;m        \033[1;37mDesactivar usuario          \033[1;34m|")
            print("--------------------------------------\033[0;m\n")
            print("Ingrese el id del usuario a desactivar")
            
            id = int(input("\n\033[1;34m>>> \033[0;m"))
            clear()
            if id < 0 or id > 7:
                invalido()

    else:
        while id == -1:
            print("\033[1;34m--------------------------------------")
            print("|\033[0;m        \033[1;37mDesactivar usuario          \033[1;34m|")
            print("--------------------------------------\033[0;m\n")
            print("Ingrese el email del usuario a desactivar")
    
            email = input("\n\033[1;34m>>> \033[0;m")
            id = busca_estud(estudiantes,email,0)
            clear()
            if id == -1:
                invalido()
                
    if estudiantes[id][2] == "ACTIVO":
        deshabilitar_estud(estudiantes,id,"   ¿Desea desactivar el perfil?     ")
    else:
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m\033[1;37m El usuario ya ha sido desactivado \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        getpass("oprima enter para volver al menu anterior\n", '')
    
    clear()

# menu Gestionar reportes de nivel 2 dentro de menu moderadores 
def menu_gest_reportes(estudiantes, reportes_s, reportes_m) :
    # (estudiantes: M_8x8_str, reportes_s: M_8x8_int, reportes_m: M_8x8_int)
    # Var
    # String: opc
    opc= ""

    while opc!="b":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m          \033[1;37mGestionar reportes        \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37ma\033[0;m. Ver reportes.")
        print("\033[1;37mb\033[0;m. Volver.")

        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()
        match opc:
            case "a": menu_reportes(estudiantes, reportes_s, reportes_m)
            case "b": clear()

def menu_reportes(estudiantes, reportes_s, reportes_m):
    # (moderadores: M_2x4_str, estudiantes: M_8x8_str, repreportes_s: M_8x8_int, reportes_m: M_8x8_str)
    #Var
    #Entero:j, i, n
    #String: rta
    rta = ""
    while rta != "no":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mGestionar reportes          \033[1;34m|")
        print("--------------------------------------")
        
        i = 0
        j = 0
        while reportes_s[i][j] != 1 and not(i == 7 and j == 7):
            if j == 7:
                j = 0
                i += 1
            else:
                j += 1
            
        if reportes_s[i][j] == 1:
            print("|\033[0;m N° \033[1;34m|\033[0;m Id-Reportante \033[1;34m|\033[0;m Id-reportado \033[1;34m|\033[0;m Motivo del reporte")
            print("\033[1;34m-----------------------------------------------------------------------\033[0;m")
            
            for i in range(0,8):
                for j in range(0,8):
                    if reportes_s[i][j] == 1:
                        
                        print(f"\033[1;34m|\033[0;m {i*8+j}  \033[1;34m|\033[0;m {i} \033[1;34m|\033[0;m {j} \033[1;34m|\033[0;m {reportes_m[i][j]}")
            
            print("Ingrese el N° de reporte que desea modificar")
            
            i = 0
            j = 0
            while reportes_s[i][j] != 1:
                n = -1
                while n <= 0 or n >63:
                    n = int(input("\n\033[1;34m>>> \033[0;m"))
                i = n // 8 
                j = n % 8
            
            clear()
            
            print("\033[1;34m--------------------------------------")
            print("|\033[0;m        \033[1;37mGestionar reportes         \033[1;34m|")
            print("--------------------------------------\033[0;m\n")
            
            print(f"el reporte del usuario ({i}) {estudiantes[i][3]} hacia ({j}) {estudiantes[j][3]} con el motivo: {reportes_m[i][j]}") 
            
            print("\nDesea desactivar a este usuario? si/no")
            rta = input("\n\033[1;34m>>> \033[0;m")
            
            while rta != "si" and rta != "no":
                invalido()
                rta = input("\n\033[1;34m>>> \033[0;m")
            
            if rta == "si":
                estudiantes[j][2] = "INACTIVO"
                reportes_s[i][j] = 2  
            else : 
                reportes_s[i][j] = 3 
                
            print("\nDesea ver otros reportes? si/no")
            rta = input("\n\033[1;34m>>> \033[0;m")
            
            while rta != "si" and rta != "no":
                invalido()
                rta = input("\n\033[1;34m>>> \033[0;m")
            clear()
                
        else:
            rta = "no"
            print("\033[1;37mActualmente no hay reportes para ver\033[0;m\n")
            getpass("oprima enter para volver al menu anterior\n", '')
    clear()

def bonus(estudiantes):
    # (estudiantes: M_8x8_str)
    # var: 
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mBonus Tracks                \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37m1\033[0;m. Bonus Track 1")
        print("\033[1;37m2\033[0;m. Bonus Track 2")
        print("\033[1;37m0\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()  
        match opc:
            case "1": track_1()            
            case "2": track_2(estudiantes)            
            case "0": clear()
            case  _ : invalido()

def ordenamiento(x):
    # (x: M_6_int)
    # var:
    # enteros: i, j, aux 
    
    aux = 0
    for i in range(0,5):
        for j in range(i+1, 6):
            if x[i] > x[j]:
                aux = x[i]
                x[i] = x[j]
                x[j] = aux
            
def track_1():
    # var:
    # enteros: i
    # array: edades, edades2
    
    edades = [0]*6
    edades[0] = 21
    edades[1] = 18
    edades[2] = 20
    edades[3] = 19
    edades[4] = 23
    edades[5] = 24
    
    print("Las edades desordenadas son:")
    for i in range(0,6):
        print(edades[i], end=", ")

    ordenamiento(edades)
    
    print("\nLas edades ordenadas serian:")
    for i in range(0,6):
        print(edades[i], end=", ")
        
    for i in range(0,5):
        if edades[i + 1] != edades[i] + 1:
            print("\ny los huecos estan entre la posicion", i, "y la posicion", i+1, "y el numero faltante es", edades[i] + 1)
            
    getpass("\noprima enter para volver al menu anterior\n", '')
    clear()

def track_2(estudiantes):
    # (estudiantes: M_8x8_str)
    # var:
    # enteros: c_est, matcheos, i  

    c_est = 0
    for i in range(0,8):
        if estudiantes[i][2] == "ACTIVO":
            c_est += 1
         
    matcheos = c_est * c_est - c_est

    if matcheos == 0:
        print("No hay match debido a que todos los usuarios estan inactivos.")
    
    else:
        print(f"Existen {matcheos} matcheos posibles")   
    
    getpass("oprima enter para volver al menu anterior\n", '')
    clear()

inicialización(likes,estudiantes,moderadores)
clear()

opc = ""
while opc!="0":
        
    # Mostramos el menu de login
    print("\033[1;34m--------------------------------------")     
    print("|\033[0;m            \033[1;37mMenu Loguearse           \033[1;34m|")
    print("--------------------------------------\033[0;m\n")
    print("\033[1;37m1\033[0;m. Loguearse.")
    print("\033[1;37m2\033[0;m. Registrarse.")
    print("\033[1;37m3\033[0;m. Bonus tracks.")
    print("\033[1;37m0\033[0;m. Salir.")
    
    opc = input("\n\033[1;34m>>> \033[0;m")

    clear()
    match opc:
        
        case "1":
            id = menu_logueo(estudiantes,moderadores)
            if id == -1: opc = "0"
            
            elif id >= 0 and id < 8: menu_estudiante(estudiantes, id, likes, reportes_s, reportes_m)
            
            else: menu_moderadores(estudiantes, reportes_s, reportes_m)
                
        case "2": menu_registrarse(moderadores,estudiantes)
        case "3": bonus(estudiantes)
        case "0": clear()
        case  _ : invalido()



