import os
import pickle
import random
from consola import * 
from registros import * 
from main import menu_estudiante, menu_moderadore ,menu_administradore

#------------------------------------------------------------------------------------------------------------------------------#
#DEFINICION DE RUTAS GENERICAS
r_estudiantes     = "src/archivos/estudiantes.dat"
r_moderadores     = "src/archivos/moderadores.dat"
r_administradores = "src/archivos/administradores.dat"
r_likes           = "src/archivos/likes.dat"
r_reportes        = "src/archivos/reportes.dat"


#APERTURA DE ARCHIVOS AL COMIENZO DEL PROGRAMA, O SU CREACION RESPECTIVAMENTE
def abrir_archivos():
    
    global estudiante, moderador, administrador, like, reporte, l_estudiantes, l_moderadores, l_administradores, l_likes, l_reportes

    estudiante = Estudiantes()
    moderador = Moderadores()
    administrador = Administradores()
    like = Likes()
    reporte = Reportes()
    
    if os.path.exists (r_estudiantes):
        l_estudiantes = open(r_estudiantes, "r+b")
    else:
        l_estudiantes = open(r_estudiantes, "w+b")
        pre_usuario()
        
    if os.path.exists (r_moderadores):
        l_moderadores = open(r_moderadores, "r+b")
    else:
        l_moderadores = open(r_moderadores, "w+b")
        pre_mod()
        
    if os.path.exists (r_administradores):
        l_administradores = open(r_administradores, "r+b")
    else:
        l_administradores = open(r_administradores, "w+b")
        pre_admin()
        
    if os.path.exists (r_likes):
        l_likes = open(r_likes, "r+b")
    else:
        l_likes = open(r_likes, "w+b")
        pre_random_likes()
        
    if os.path.exists (r_reportes):
        l_reportes = open(r_reportes, "r+b")
    else:
        l_reportes = open(r_reportes, "w+b")
        
#----------------------------------------------------------------------------------------------------------------------------#  
# USUARIOS PRECARGADOS 
def pre_usuario():
    usuariogenerico = Estudiantes() # type: ignore
    for i in range(4):
        usuariogenerico.id = i
        usuariogenerico.email = f"estudiante{i+1}@ayed.com"
        usuariogenerico.contraseña = str(i)*3+str(i+1)*3
        usuariogenerico.name = f"estudiante{i+1}"
        usuariogenerico.sexo = "m" if random.randint(0,1) else "s"
        usuariogenerico.estado = True
        usuariogenerico.materia_fav = "Algoritmos y Estructuras de Datos"
        usuariogenerico.bio = ""
        usuariogenerico.pais = "Argentina"
        usuariogenerico.ciudad = "Rosario"
        usuariogenerico.fecha = str(random.randint(1990,2006))+"/"+str(random.randint(1,12)).rjust(2,"0")+"/"+str(random.randint(1,28)).rjust(2,"0")
        Format_Estudiante(usuariogenerico)
        l_estudiantes.seek(0,2)
        pickle.dump(usuariogenerico, l_estudiantes)
        l_estudiantes.flush()

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


#MODERADOR PRECARGADO
def pre_mod():
    mods = Moderadores()
    mods.id = 0
    mods.email = "Modpre@ayed.com"
    mods.contraseña = "111111"
    mods.name = "Moderador_1"
    mods.estado = True
    Format_Mods(mods)
    l_moderadores.seek(0,2)
    pickle.dump(mods, l_moderadores)
    l_moderadores.flush()

#ADMIN PRECARGADO
def pre_admin():
    admin = Administradores()
    admin.id = 0
    admin.email = "Adminpre@ayed.com"
    admin.contraseña = "000000"
    Format_Admins(admin)
    l_administradores.seek(0,2)
    pickle.dump(admin, l_administradores)
    l_administradores.flush()
    
#LIKES ALEATORIOS PRECARGADOS
def pre_random_likes():
    # calcular tamaño del registro estudiante
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    pickle.load(l_estudiantes)
    x=l_estudiantes.tell()
    cant=t//x
    # Dos for para que se carguen (o no) los likes randoms
    for i in range (cant):
        vl=Likes()
        l_estudiantes.seek(x*i)#posicionamoiento del puntero para el emisor del like
        vr=pickle.load(l_estudiantes)# se recorren los emisores
        vl.remitente=vr.id# se asigna el id del emisor
        
        for j in range(cant):
            l_estudiantes.seek(x*j,0)# posicionamiento del puntero
            vr2=pickle.load(l_estudiantes)# se van recorriendo los estudiantes destinatarios(por eso se usa otra variable:"vr2")
            if random.randint(0,1): # si el random devuelve 1, se da like, si es que no se trata del mismo estudiante
                if vr.id !=vr2.id:
                    vl.destinatario=vr2.id #se asigna el destinatario del like
                    l_likes.seek(0,2)#posicionamiento del puntero
                    #desde aca se guarda el like en cuestion
                    format_likes(vl)
                    pickle.dump(vl,l_likes)
                    l_likes.flush()    

def cambio_dato_estudiante(dato:str,x:int,estudiante:Estudiantes,opcion:str):
    print(f"Su {opcion} ya establecida es: ",estudiante.__dict__[dato],"\n ¿Desea cambiarlo?<Si><No>")
    cambiar=input(">>>").lower()
    while cambiar!="si" and cambiar!="no":
        clear()
        print("Opcion invalida.\nIntrente nuevamente.")
        print(f"Su {opcion} ya establecida es: ",estudiante.__dict__[dato],"\n ¿Desea cambiarlo?<Si><No>")
        cambiar=input(">>>").lower()

    if cambiar=="si":
        aux=input(f"Ingrese su nuevo/a {opcion}:")
        estudiante.__dict__[dato]=aux
        pos=busca_estud_id(estudiante.id)
        l_estudiantes.seek(0,0)
        vr=pickle.load(l_estudiantes)
        cant=l_estudiantes.tell()
        l_estudiantes.seek(cant*pos,0)
        Format_Estudiante(estudiante)
        pickle.dump(estudiante,l_estudiantes)
        l_estudiantes.flush()



#----------------------------------------------------------------------------------------------------------------------------# 
#BUSQUEDAS DE ARCHIVOS, DE MODERADORES Y DE ESTUDIANTES. LOS ESTUDIANTES PUEDEN SER BUSCADOS POR ID Y POR MAIL. LOS MODERADORES SOLO POR MAIL.      
def busca_estud_id(id):
    
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    pp=0
    vr=pickle.load(l_estudiantes)
    while l_estudiantes.tell()<t and id!=vr.id:
        pp=l_estudiantes.tell()
        vr=pickle.load(l_estudiantes)
    if id==vr.id:
        pos=pp
    else:
        pos=-1
    
    return pos

def busca_estud_email(email):
    global estudiante
    t=os.path.getsize(r_estudiantes)
    email = email.ljust(32," ")
    
    l_estudiantes.seek(0)
    pp=0
    estudiante=pickle.load(l_estudiantes)
    while l_estudiantes.tell()<t and email!=estudiante.email:
        pp=l_estudiantes.tell()
        estudiante=pickle.load(l_estudiantes)
    if email==estudiante.email:
        pos=pp
    else:
        pos=-1
    
    return pos

def busca_mod_email(email):
    global l_moderadores, r_moderadores, moderador
    t=os.path.getsize(r_moderadores)
    
    l_moderadores.seek(0,0)
    pp=0
    moderador=pickle.load(l_moderadores)
    while l_moderadores.tell()<t and id!=moderador.email:
        pp=l_moderadores.tell()
        moderador=pickle.load(l_moderadores)
    if id==moderador.email:
        pos=pp
    else:
        pos=-1

    return pos
#-------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCIONES COMO LOGUEO, BUSQUEDA DE ID Y BAJA LOGICA

def menu_logueo():
    # (estudiantes: M_8x8_str, moderadores: M_2x4_str,)
    # Var
    # Entero: login_e, intentos
    # String: email, password
    login_e = "inválido" 
    intentos = 3
    global estudiante, moderador, administrador
    
    while login_e == "inválido" and intentos > 0:
        clear()
        
        cartel("Inicio de sesion", AZUL)

        if intentos == 3:
            print("Ingrese sus credenciales.\n")
            
        else:
            print("\033[1;31mCredenciales incorrectas\033[0;m")
            print("Te quedan ",intentos," intentos")
            print("Intente nuevamente\n")
    
        email = input("email:\n\033[1;34m>>> \033[0;m")
        print()
        password = getpass()
        
        login_e = is_login(email,password) 

        match login_e:
            case "inválido": intentos -= 1
            case "estud": menu_estudiante(estudiante)
            case "mod": menu_moderadore(moderador)
            case "admin": menu_administradore(administrador)
            
    clear()
    return intentos

def is_login(email,password):
    # (email:str, password:str)
    # Var
    # Entero:i
    #Hacer busqueda en archivos.
    global estudiante, moderador, administrador
    
    email = email.ljust(32," ")

    pos = busca_estud_email(email)
    if pos != -1:
        l_estudiantes.seek(pos,0)
        estudiante = pickle.load(l_estudiantes)
        
        if estudiante.email == email and estudiante.contraseña == password and estudiante.estado == True:
            return "estud"
        else:
            return "inválido"
    else:
        
        pos = busca_mod_email(email)
        if pos != -1:
            l_moderadores.seek(pos,0)
            moderadore = pickle.load(l_moderadores)
            if moderadore.email == email and moderadore.contraseña == password and moderadore.estado == True:
                return "mod"
            else:
                return "inválido"
        else:
            t=os.path.getsize(r_administradores)

            l_administradores.seek(0)
            pp=0
            administrador=pickle.load(l_administradores)
            while l_administradores.tell()<t and email!=administrador.email:
                pp=l_administradores.tell()
                administrador=pickle.load(l_administradores)
            if administrador.email == email and administrador.contraseña == password:
                return "admin"
            else:
                return "inválido"

def deshabilitar_estud(id,text= "      ¿Desea eliminar su perfil?    "):
    cartel(text,BLANCO)
    opc = input(BLANCO)
    while opc != "si" and opc != "no":
        invalido()
        cartel(text,BLANCO)
        opc = input(BLANCO)

    x=busca_estud_id(id)
    vr=pickle.load(l_estudiantes)
    l_estudiantes.seek(x,0)
    if opc == "si" :
        vr.estado = "INACTIVO"
        print("Perfil desactivado.")
        pickle.dump(vr,l_estudiantes)
        l_estudiantes.flush()
    else :
        print("Perfil no desactivado.")
    getpass("Oprima enter para volver al menu anterior\n", '')
    clear()
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#CIERRE DE PROGRAMA
def cerrar_programa():
    
    global l_estudiantes, l_moderadores, l_administradores, l_likes, l_reportes
    
    l_estudiantes.close()
    l_moderadores.close()
    l_administradores.close()
    l_likes.close()
    l_reportes.close()
    
    print("           \033[1;37mFin del programa           ")
    print("       \033[1;37mGracias por visitarnos.         \n\033[0;m")

    #print("""########       ########       ########
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

if  "__main__" == __name__:
    abrir_archivos()
    
    
    
    cerrar_programa()
