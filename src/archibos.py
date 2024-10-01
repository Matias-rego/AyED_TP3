import os
import pickle
import random
from consola import * 
from registros import * 
#------------------------------------------------------------------------------------------------------------------------------#
#DEFINICION DE RUTAS GENERICAS
r_estudiantes     = "src/archivos/estudiantes.dat"
r_moderadores     = "src/archivos/moderadores.dat"
r_administradores = "src/archivos/administradores.dat"
r_likes           = "src/archivos/likes.dat"
r_reportes        = "src/archivos/reportes.dat"


#APERTURA DE ARCHIVOS AL COMIENZO DEL PROGRAMA, O SU CREACION RESPECTIVAMENTE
def abrir_archivos():
    
    global estudiante, moderadore, administradore, like, reporte, l_estudiantes, l_moderadores, l_administradores, l_likes, l_reportes

    estudiante = Estudiantes()
    moderadore = Moderadores()
    administradore = Administradores()
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
        pre_likes()
        
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
def pre_likes():
    
    pass

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
    global l_moderadores, r_moderadores, moderadore
    t=os.path.getsize(r_moderadores)
    
    l_moderadores.seek(0,0)
    pp=0
    moderadore=pickle.load(l_moderadores)
    while l_moderadores.tell()<t and id!=moderadore.email:
        pp=l_moderadores.tell()
        moderadore=pickle.load(l_moderadores)
    if id==moderadore.email:
        pos=pp
    else:
        pos=-1

    return pos
#-------------------------------------------------------------------------------------------------------------------------------------------------#
#BAJA LOGICA
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
        pickle.dump(l_estudiantes,vr)
        l_estudiantes.flush()
    else :
        print("Perfil no desactivado.")
    getpass("oprima enter para volver al menu anterior\n", '')
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
    
    print(busca_estud_email("estudiante3@ayed.com"))
    
    cerrar_programa()