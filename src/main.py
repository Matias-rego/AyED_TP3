"""
    Integrantes:
    
    Nicolás Fossati
    Matias Miguel Angel Rego
    Marcos Banducci
    Tomas Agusti
    
    comisión: ISI 101
"""

# importamos los modulos que usamos
import pickle
from consola import * 
from bonus import bonus
import random
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

def calcular_edad(fecha):
    # (fecha: str)
    # Var:
    # Datatime: fecha_actual ; fecha_nacimiento
    # Entero: edad
    
    fecha_nacimiento = datetime.strptime(fecha, "%Y/%m/%d")
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
            if random.randint(0,3)==1: # si el random devuelve 1, se da like, si es que no se trata del mismo estudiante
                if vr.id !=vr2.id:
                    vl.destinatario=vr2.id #se asigna el destinatario del like
                    l_likes.seek(0,2)#posicionamiento del puntero
                    #desde aca es el guardado del like en cuestion
                    format_likes(vl)
                    pickle.dump(vl,l_likes)
                    l_likes.flush()    

#----------------------------------------------------------------------------------------------------------------------------# 
#BUSQUEDAS DE ARCHIVOS, DE MODERADORES Y DE ESTUDIANTES. LOS ESTUDIANTES PUEDEN SER BUSCADOS POR ID Y POR MAIL. LOS MODERADORES SOLO POR MAIL.      
def busca_estud_id(id):
    global estudiante
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    
    id = str(id).ljust(4," ")
    pp=0
    estudiante=pickle.load(l_estudiantes)
    while l_estudiantes.tell()<t and id!=estudiante.id:
        pp=l_estudiantes.tell()
        estudiante=pickle.load(l_estudiantes)
    if id==estudiante.id:
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
    global moderador
    t=os.path.getsize(r_moderadores)
    email = email.ljust(32," ")
    
    l_moderadores.seek(0,0)
    pp=0
    moderador=pickle.load(l_moderadores)
    while l_moderadores.tell()<t and email!=moderador.email:
        pp=l_moderadores.tell()
        moderador=pickle.load(l_moderadores)
    if email==moderador.email:
        pos=pp
    else:
        pos=-1

    return pos

def busca_admin(email):
    global administrador
    t=os.path.getsize(r_administradores)
    email = email.ljust(32," ")

    l_administradores.seek(0)
    pp=0
    administrador=pickle.load(l_administradores)
    while l_administradores.tell()<t and email!=administrador.email:
        pp=l_administradores.tell()
        administrador=pickle.load(l_administradores)
    if email==administrador.email:
        pos=pp
    else:
        pos=-1

    return pos

def cant_likes(id: int) -> int:
    t=os.path.getsize(r_likes)
    l_likes.seek(0,0)
    pickle.load(l_likes)
    t1=l_likes.tell()
    cant=t//t1
    
    n_likes = 0
    for i in range(0,cant):
        l_likes.seek(i * t1,0)
        like=pickle.load(l_likes)
        if like.destinatario == id:
            n_likes += 1
    
    return n_likes  

def is_like(estudiante1:Estudiantes,estudiante2:Estudiantes) -> int:
    t=os.path.getsize(r_likes)

    l_likes.seek(0,0)
    pp=0
    like=pickle.load(l_likes)
    while l_likes.tell()<t and (estudiante1.id != like.remitente or estudiante2.id != like.destinatario):
        pp=l_likes.tell()
        like=pickle.load(l_likes)
    if (estudiante1.id == like.remitente and estudiante2.id == like.destinatario):
        pos=pp
    else:
        pos=-1

    return pos

def quitar_Like(pos) -> None:
    t=os.path.getsize(r_likes)
    l_likes.seek(0,0)
    pickle.load(l_likes)
    t1=l_likes.tell()
    
    l_likes.seek(t-t1,0)
    like_u=pickle.load(l_likes)
    
    l_likes.seek(pos,0)
    pickle.dump(like_u,l_likes)
    
    l_likes.truncate(t-t1)
    l_likes.flush()
    
def dar_Like(estudiante1:Estudiantes,estudiante2:Estudiantes) -> None:
    like = Likes()
    like.remitente = estudiante1.id 
    like.destinatario = estudiante2.id
    
    format_likes(like)
    l_likes.seek(0,2)
    pickle.dump(like,l_likes)
    l_likes.flush()
    
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

def is_login(email:str, password:str)-> str:
    # Var
    # Entero:i
    global estudiante, moderador, administrador
    email = email.ljust(32," ")

    pos = busca_estud_email(email)
    if pos != -1:
        l_estudiantes.seek(pos,0)
        estudiante = pickle.load(l_estudiantes)
        if estudiante.email == email and estudiante.contraseña == password and estudiante.estado == True:
            return "estud"
        
    else:
        pos = busca_mod_email(email)
        if pos != -1:
            l_moderadores.seek(pos,0)
            moderadore = pickle.load(l_moderadores)
            if moderadore.email == email and moderadore.contraseña == password and moderadore.estado == True:
                return "mod"
            
        else:
            pos = busca_admin(email)
            if pos != -1:
                l_administradores.seek(pos,0)
                administrador = pickle.load(l_administradores)
                if administrador.email == email and administrador.contraseña == password:
                    return "admin"
            
    return "inválido"

def deshabilitar_estud(pos,text= "¿Desea eliminar tu perfil?",color = AZUL)-> bool:
    
    opc = menu(text,"",
       ["s. Si",
        "n. No.",
        "","","","","","","",""],color)
    
    if opc == "s":
        l_estudiantes.seek(pos,0)
        vr=pickle.load(l_estudiantes)
    
        vr.estado = False
        l_estudiantes.seek(pos,0)
        pickle.dump(vr,l_estudiantes)
        l_estudiantes.flush()
        return True
    else:
        return False
    
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
    
    print("""########       ########       ########
 #######       ########       #######
  ########     ########     ########
   #########   ########   #########         
      ##########################            Programa hecho por:
          ##################               
######################################        -Nicolás Fossati
######################################        -Matias Miguel Angel Rego.
######################################        -Marcos Banducci
         ####################                 -Tomas Agusti
     ############################
   #########   ########   #########
  ########     ########     ########
 #######       ########       #######
 #######       ########       #######""")

 
def menu_estudiante(estudiante:Estudiantes):
    # Var
    # String: opc 
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0" and estudiante.estado:
        clear()
        opc = menu("Menu principal","",[
        "1. Gestionar mi perfil.",
        "2. Gestionar candidatos.",
        "3. Matcheos.",
        "4. Reportes estadísticos.",
        "0. Salir.",
        "","","","",""],
        AZUL)

        match (opc):  
            case "1": menu_perfil(estudiante)
            case "2": menu_candidatos(estudiante)
            case "3": menu_Matcheos(estudiante)
            case "4": menu_reportes_estadisticos(estudiante)

def menu_moderadore(mods:Moderadores):
    # Var
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0":
        clear()
        opc = menu("Menu Moderadores","",[
        "1. Gestionar usuarios.",
        "2. Gestionar reportes.",
        "3. Reportes estadísticos.",
        "0. Salir.",
        "","","","","",""],
        CIAN)

        match (opc):  
            case "1": menu_gest_usuario()
            case "2": menu_gest_reportes()
            case "3": construcción()
            
def menu_administradore(administradore:Administradores):
    # Var
    # String: opc 
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0":
        clear()
        opc = menu("Menu administradores","",[
        "1. Gestionar usuarios.",
        "2. Gestionar reportes.",
        "3. Reportes estadísticos.",
        "0. Salir.",
        "","","","","",""],
        AZUL)

        match (opc):  
            case "1": menu_gest_usuarios()
            case "2": menu_gest_reportes()
            case "3": menu_reportes_estadisticos()


def menu_registrarse(text="<          Registro          >"):
    clear()
    cartel(text,AZUL)
    ve=Estudiantes()
    #----------------Validacion de <@> del email------------------#
    print("Ingrese su email:")
    email=input(AZUL+"\n>>> \033[0;m")
    val=0
    for i in range(len(email)):
        if email[i]=="@":
            val += 1 
    while val!=1:
        clear()
        cartel(text,AZUL)
        if val>1:
            print("No existen emails con mas de un <@>.\nIntente nuevamente.")
        else:   
            print("No existen emails sin <@>.\nIntente nuevamente.")
        print("Ingrese su email:")
        email=input(AZUL+"\n>>> \033[0;m")
        val=0
        for i in range(len(email)):
            if email[i]=="@":
                val += 1   
    #-----------Validacion de existencia unica de email--------------#
    
    while busca_estud_email(email) !=-1 and busca_mod_email(email) !=-1:
        clear()
        cartel(text,AZUL)
        print("Email ya utlizado.\nIntente con uno nuevo.")
        print("Ingrese su email:")
        email=input(AZUL+"\n>>> \033[0;m")
        #------------Validacion de <@> del email---------------------#
        val=0
        for i in range(len(email)):
            if email[i]=="@":
                val += 1 
        while val!=1:
            clear()
            cartel(text,AZUL)
            if val>1:
                print("No existen emails con mas de un <@>.\nIntente nuevamente.")
            else:   
                print("No existen emails sin <@>.\nIntente nuevamente.")
            print("Ingrese su email:")
            email=input(AZUL+"\n>>> \033[0;m")
            val=0
            for i in range(len(email)):
                if email[i]=="@":
                    val += 1   
    
    ve.email=email
    #------------------------Contraseña-------------------------#
    clear()
    cartel(text,AZUL)
    ve.contraseña = getpass()
    #----------------------Nombre y sexo--------------------------#
    clear()
    cartel(text,AZUL)
    print("Ingrese su nombre:")
    ve.name = input(AZUL+"\n>>> "+VACIO)
    
    clear()
    cartel(text,AZUL)
    print("Ingrese su sexo <M> <F>:")
    sexo=input(AZUL+"\n>>> "+VACIO).lower()
    while sexo!="m" and sexo!="f":
        clear()
        cartel(text,AZUL)
        print("Sexo invalido.\nIntente nuevamente.")
        print("Ingrese su sexo <M> <F>:")
        sexo=input(AZUL+"\n>>> "+VACIO).lower()
    ve.sexo=sexo
    #-------------------Fecha nacimiento----------------------------#
    clear()
    cartel(text,AZUL)
    ve.fecha = validar_fecha()
    
    #------------------Demas datos--------------------------------# 
    clear()
    cartel("¿Desea terminar de completar tus datos personales ahora?(<Si> <No>)",AZUL)
    seguir=input(AZUL+"\n>>> "+VACIO).lower()
    while seguir!="si" and seguir!="no":
        clear()
        cartel("¿Desea terminar de completar sus datos personales ahora?(<Si> <No>)",AZUL)
        print("Opcion invalida.\nIntente nuevamente.")
        seguir=input(AZUL+"\n>>> "+VACIO).lower()
    if seguir=="si":
        clear()
        cartel(text,AZUL)
        print("Ingrese su materia favorita:")
        ve.materia_fav = input(AZUL+"\n>>> "+VACIO)
        
        clear()
        cartel(text,AZUL)
        print("Ingrese su país:")
        ve.pais = input(AZUL+"\n>>> "+VACIO)
        
        clear()
        cartel(text,AZUL)
        print("Ingrese su ciudad:")
        ve.ciudad = input(AZUL+"\n>>> "+VACIO)
        clear()
        
        cartel(text,AZUL)
        print("Ingrese su biografia:")
        ve.bio=input(AZUL+"\n>>> "+VACIO)
        
    #---------------Elementos de asignacion automatica------------------#    
    ve.estado=True
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    aux=pickle.load(l_estudiantes)
    x=l_estudiantes.tell()
    cant=t//x
    l_estudiantes.seek((cant-1)*x,0)
    vr=pickle.load(l_estudiantes)
    id_siguiente=int(vr.id)+1
    ve.id=id_siguiente
    #------------Archivar el estudiante cargado-----------------------#
    Format_Estudiante(ve)
    l_estudiantes.seek(0,2)
    pickle.dump(ve,l_estudiantes)
    l_estudiantes.flush()

#-----------------------------------------------------------#
# menu Gestionar mi perfil de nivel 2 dentro de menu estudiantes   
def menu_perfil(estudiante:Estudiantes):
    # Var:
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0" and estudiante.estado:
        clear()
        opc = menu("Gestionar mi Perfil","",[
        "1. Editar Datos Personales.",
        "2. Eliminar perfil.",
        "0. Volver.",
        "","","","","","",""],
        AZUL)

        match opc:
            case "1": menu_editar_datos(estudiante)     
            case "2":
                if deshabilitar_estud(busca_estud_id(estudiante.id)):
                    estudiante.estado = False

def menu_editar_datos(estudiante:Estudiantes):
    # (estudiantes: M_8X8_str, id: int)
    # var:
    # String: opc
    
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0" and estudiante.estado:
        clear()
        opc = menu("Editar mis Datos","",[
        "1. Fecha de Nacimiento.",
        "2. Biografia.",
        "3. Nombre.",
        "4. Sexo.",
        "5. Materia Favorita",
        "6. País.",
        "7. Ciudad.",
        "0. Volver.",
        "",""],
        AZUL)
        match opc:
            case "1":
                fecha=validar_fecha()
                cambio_dato_estudiante(fecha,10,estudiante,"Fecha de Nacimiento")  
            case "2": cambio_dato_estudiante("bio",255,estudiante,"Biografia") 
            case "3": cambio_dato_estudiante("name",32,estudiante,"Nombre") 
            case "4": cambio_dato_estudiante("sexo",1,estudiante,"Sexo")
            case "5": cambio_dato_estudiante("materia_fav",13,estudiante,"Materia Favorita")
            case "6": cambio_dato_estudiante("pais",32,estudiante,"País")
            case "7": cambio_dato_estudiante("ciudad",32,estudiante,"Ciudad")

def cambio_dato_estudiante(dato:str,x:int,estudiante:Estudiantes,opcion:str):
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


# menu Gestionar candidatos de nivel 2 dentro de menu estudiantes 
def menu_candidatos(estudiante:Estudiantes):
    # var:
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0" and estudiante.estado:
        clear()
        opc = menu("Gestionar candidatos","",[
            "1. Ver candidatos.",
            "2. Reportar un candidato.",
            "0. Volver.",
            "","","","","","",""],
            AZUL)

        match opc:
            case "1": menu_ver_candidatos(estudiante)
            case "2": menu_reportar(estudiante)       

def menu_ver_candidatos(estudiante:Estudiantes):
    # var:
    # String: me_gusta, opc
    # Entero: j, i, pos
    # Arreglo:poss, opcs, 
    
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    pickle.load(l_estudiantes)
    t1=l_estudiantes.tell()
    
    min = 0
    l_estudiantes.seek(0,0)
    Re=pickle.load(l_estudiantes)
    while Re.estado == False:
        min=l_estudiantes.tell()
        Re=pickle.load(l_estudiantes)
        
    max = t
    l_estudiantes.seek(t-t1)
    Re=pickle.load(l_estudiantes)
    while Re.estado == False:
        max=l_estudiantes.tell()-t1
        l_estudiantes.seek(max-t1)
        Re=pickle.load(l_estudiantes)
        
    # areglo donde guardo las opsiones que se van a mostrar 
    opcs = [" << A << ","  Q. salir   ","     L. Quitar Like      "," R. reportar "," >> S >> "]
    # areglo donde guardo las opsiones validas que tiene el usuario
    opcv = [ b'\r', b'q', b's', b'q', b'l', b'r'] 
    # areglo del los estado de los botones
    estado = [0,1,1,1,1]
    # 0 no se muestra
    # 1 se muestra normal
    # 2 se muestra verde

    ch = ""
    prech = ""
    pos = min

    l_estudiantes.seek(pos)
    estud = pickle.load(l_estudiantes)

    while prech != b'q' or (ch !=  b'\r' and ch != b'q'):
        
        estado[2] = 1
        opcv[4] = b'l'
        
        # dependiendo de lo que el usuari ingreso realiso la opsion corespondiente      
        if ch ==  b'\r':
            match prech:
                case b'a':
                    opcv[2] = b's'
                    estado[4] = 1
                    estado[0] = 1
                    
                    pos -= t1
                    l_estudiantes.seek(pos)
                    estud = pickle.load(l_estudiantes)
                    while estud.estado == False:
                        pos -= t1
                        l_estudiantes.seek(pos)
                        estud = pickle.load(l_estudiantes)
                        
                case b's':
                    opcv[1] = b'a'
                    estado[0] = 1
                    estado[4] = 1
                    
                    pos += t1
                    l_estudiantes.seek(pos)
                    estud = pickle.load(l_estudiantes)
                    while estud.estado == False:
                        pos += t1
                        l_estudiantes.seek(pos)
                        estud = pickle.load(l_estudiantes)
                    
                case b'l':
                    estado[2] = 1
                    pp = is_like(estudiante,estud)
                    if pp>0:
                        quitar_Like(pp)
                    else:
                        dar_Like(estudiante,estud)

            prech = b''
        elif ch ==  b'a':
            estado[0] = 2
            if prech == ch:
                opcv[2] = b's'
                estado[4] = 1
                
                pos -= t1
                l_estudiantes.seek(pos)
                estud = pickle.load(l_estudiantes)
                while estud.estado == False:
                    pos -= t1
                    l_estudiantes.seek(pos)
                    estud = pickle.load(l_estudiantes)
                prech = b''
                estado[0] = 1
            else:
                prech = b'a'
            
        elif ch ==  b's':
            estado[4] = 2
            if prech == ch:
                opcv[1] = b'a'
                estado[0] = 1
                
                pos += t1
                l_estudiantes.seek(pos)
                estud = pickle.load(l_estudiantes)
                while estud.estado == False:
                    pos += t1
                    l_estudiantes.seek(pos)
                    estud = pickle.load(l_estudiantes)
                prech = b''
                estado[4] = 1
            else:
                prech = b's'
            
        elif ch ==  b'q':
            estado[1] = 2
            if prech == ch:
                ch == b''
            else:
                prech = b'q'
                
        elif ch ==  b'l':
            estado[2] = 2
            if prech == ch:
                prech = b''
                estado[2] = 1
                pp = is_like(estudiante,estud)
                if pp>0:
                    quitar_Like(pp)
                else:
                    dar_Like(estudiante,estud)
            else:
                prech = b'l'

        elif ch ==  b'r':
            estado[3] = 2
            prech = b'r'
            
        # limito que no se pase de los limiten del archibo
        if min >= pos:
            opcv[1] = b'q'
            estado[0] = 0
        
        if pos >= max-t1:
            opcv[2] = b'q'
            estado[4] = 0
            
        if is_like(estudiante,estud)>0:
            opcs[2] = "     L. Quitar Like      "
        else:
            opcs[2] = "       L. Dar Like       "

        clear()
        # preparo lo que voy a mostrar y lo dibujo enpantalla 
        print(f"""{AZUL}╔════════════════════════════════════╦═════════════════╦══════════╦═══════╗
║{VACIO}""",end="")
        if estud.id != estudiante.id:
            print("   Nombre  ",end="")
        else:
            print(" Tu nombre ",end="")
            estado[2] = 0
            opcv[4] = b'q'
        print(f""": {estud.name[:22].ljust(22," ")} {AZUL}║{VACIO} Biografia:      {AZUL}║\033[4;34mlikes:{str(cant_likes(estud.id)).center(4)}║ID:{estud.id}{VACIO+AZUL}║
║{VACIO}   Email   : {estud.email[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[0:34]} {AZUL}║
║{VACIO}   Pais    : {estud.pais[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[34:68]} {AZUL}║
║{VACIO}   Ciudad  : {estud.ciudad[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[68:102]} {AZUL}║
║{VACIO}   Sexo    : """,end="")
        if estud.sexo == "m":
            print("Masculino             ",end="")
        else:
            print("Femenino              ",end="")
        
        print(f""" {AZUL}║{VACIO} {estud.bio[102:136]} {AZUL}║
║{VACIO}   Edad    : {str(calcular_edad(estud.fecha))[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[136:170]} {AZUL}║
║{VACIO} Nacimiento: {estud.fecha[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[170:204]} {AZUL}║
║{VACIO} MateriaFav: {estud.materia_fav[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[204:238]} {AZUL}║
╠═════════╦═════════════╦════════════╩════════════╦═════════════╦═════════╣\n║""",end="")
        
        for i in range(5):
            match estado[i]:
                case 0:
                    print(len(opcs[i])*" ",end="")
                case 1:
                    print(VACIO+opcs[i],end="")
                case 2:
                    print(VERDE+opcs[i],end="")
                    estado[i] = 1
            print(AZUL+"║",end="")
                    
        print("\n╚═════════╩═════════════╩═════════════════════════╩═════════════╩═════════╝")
        
        # leo y verifico lo que ingresa el usuario
        ch = "" 
        while ch !=  opcv[0] and ch !=  opcv[1] and ch !=  opcv[2] and ch !=  opcv[3] and ch !=  opcv[4] and ch !=  opcv[5] :
            ch = getch().lower()

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

        email = input(AZUL+"\n>>> "+VACIO)
        
        
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
def menu_gest_usuario():
    # Var
    # String: opc
    opc= ""
    
    while opc!="0":
        clear()
        opc = menu("Gestionar usuarios","",[
        "1. Desactivar usuario.",
        "0. Volver.",
        "","","","","","","",""],
        CIAN)

        if opc == "1": menu_desactivar_usuario()

def menu_desactivar_usuario() -> None:
    # Var
    # Entero: id
    # String: opc

    clear()
    opc = menu("Desactivar usuario","Seleccione el metodo que utilizará.",[
    "1. Desde el id.",
    "2. Desde el email de usuario.",
    "0. Volver.",
    "","","","","","",""],
    CIAN)

    if opc != "0":
        
        pos = -1
        clear()
        while pos < 0:
            cartel("Desactivar usuario ", CIAN)
            
            if opc == "1":
                print("Ingrese el id del usuario que desea desactivar: ")
                try:
                    user = int(input("\n\033[1;34m>>> \033[0;m"))
                    pos = busca_estud_id(user)
                    if pos != -1:
                        l_estudiantes.seek(pos,0)
                        estudiante = pickle.load(l_estudiantes)
                        if estudiante.estado == False:
                            pos = -1 
                        
                except:
                    pos = -1
                    
            else:
                print("Ingrese el email del usuario que desea desactivar: ")
                user = input("\n\033[1;34m>>> \033[0;m")
                pos = busca_estud_email(user)
                if pos != -1:
                    l_estudiantes.seek(pos,0)
                    estudiante = pickle.load(l_estudiantes)
                    if estudiante.estado == False:
                        pos = -1 
                
            invalido()
        clear()

        if deshabilitar_estud(pos,"¿Desea desactivar este perfil?",CIAN):
            cartel("El usuario ha sido desactivado",CIAN)
        else:
            cartel("El usuario no ha sido desactivado",CIAN)
        print("oprima cualquier tecla para volver al menu anterior\n")
        getch()
    

def menu_gest_usuarios():
    pass
# menu Gestionar reportes de nivel 2 dentro de menu moderadores 
def menu_gest_reportes() :
    # Var
    # String: opc
    opc= ""
    
    while opc!="0":
        clear()
        opc = menu("Gestionar reportes","",[
        "1. Ver reportes.",
        "0. Volver.",
        "","","","","","","",""],
        CIAN)

        if opc == "1": menu_reportes()
  
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

abrir_archivos()
opc = ""

while opc!="0":
    clear()    
    # Mostramos el menu de login
    opc = menu("Menu Loguearse","",[
        "1. Loguearse.",
        "2. Registrarse.",
        "3. Bonus tracks.",
        "0. Salir.",
        "","","","","",""],
        AZUL)

    match opc:
        case "1": 
            if menu_logueo()==0: 
                print(ROJO+"    Demasiados intentos incorrectos.\n Intente mas tarde."+VACIO)
                opc = "0"
                
        case "2": menu_registrarse()
        case "3": bonus()

cerrar_programa()