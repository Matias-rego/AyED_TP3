import os
import pickle
import random
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
        pre_usuario()
        
    if os.path.exists (ruta_moderadores):
        logico_moderadores = open(ruta_moderadores, "r+b")
    else:
        logico_moderadores = open(ruta_moderadores, "w+b")

        
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

#BUSQUEDAS DE ARCHIVOS, DE MODERADORES Y DE ESTUDIANTES. LOS ESTUDIANTES PUEDEN SER BUSCADOS POR ID Y POR MAIL. LOS MODERADORES SOLO POR MAIL.      
def busca_estud(id):
    if int(id)==True:
        t=os.path.getsize(ruta_estudiantes)
        if t!=0:
            logico_estudiantes.seek(0,0)
            pp=0
            vr=pickle.load(logico_estudiantes)
            while logico_estudiantes.tell()<t and id!=vr.id:
                pp=logico_estudiantes.tell()
                vr=pickle.load(logico_estudiantes)
            if id==vr.id:
                pos=pp
            else:
                pos=-1
        else:
            pos=-1
    if int(id)==False:
        t=os.path.getsize(ruta_estudiantes)
        if t!=0:
            logico_estudiantes.seek(0,0)
            pp=0
            vr=pickle.load(logico_estudiantes)
            while logico_estudiantes.tell()<t and id!=vr.email:
                pp=logico_estudiantes.tell()
                vr=pickle.load(logico_estudiantes)
            if id==vr.email:
                pos=pp
            else:
                pos=-1
        else:
            pos=-1
        
    return pos

def busca_mod(email):
    t=os.path.getsize(ruta_moderadores)
    if t!=0:
        ruta_moderadores.seek(0,0)
        pp=0
        vr=pickle.load(logico_moderadores)
        while logico_moderadores.tell()<t and id!=vr.email:
            pp=logico_moderadores.tell()
            vr=pickle.load(logico_moderadores)
        if id==vr.email:
            pos=pp
        else:
            pos=-1
    else:
        pos=-1  
    return pos
#-------------------------------------------------------------------------------------------------------------------------------------------------

def deshabilitar_estud(id,text= "      ¿Desea eliminar su perfil?    "):
    cartel(text,BLANCO)
    opc = input(BLANCO)
    while opc != "si" and opc != "no":
        invalido()
        cartel(text,BLANCO)
        opc = input(BLANCO)

    x=busca_estud(id)
    vr=pickle.load(logico_estudiantes)
    ruta_estudiantes.seek(0,x)
    if opc == "si" :
        vr.estado = "INACTIVO"
        print("Perfil desactivado.")
        pickle.dump(logico_estudiantes,x)
    else :
        print("Perfil no desactivado.")
    getpass("oprima enter para volver al menu anterior\n", '')
    clear()

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
        logico_estudiantes.seek(0,2)
        pickle.dump(usuariogenerico, logico_estudiantes)
        logico_estudiantes.flush()
        

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

if  "__main__" == __name__:
    abrir_archivos()
    cerrar_programa()