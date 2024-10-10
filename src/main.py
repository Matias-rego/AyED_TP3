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
    #Variables fisicas de los archivos
    estudiante = Estudiantes()
    moderador = Moderadores()
    administrador = Administradores()
    like = Likes()
    reporte = Reportes()
    #Forma de apertura de los archivos
    #listo#
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
def pre_usuario():#listo#
    usuariogenerico = Estudiantes() # type: ignore
    for i in range(4):
        usuariogenerico.id = i
        usuariogenerico.email = f"estudiante{i+1}@ayed.com"
        usuariogenerico.contraseña = str(i)*3+str(i+1)*3
        usuariogenerico.name = f"estudiante{i+1}"
        usuariogenerico.sexo = "m" if random.randint(0,1) else "f"
        usuariogenerico.estado = True
        usuariogenerico.materia_fav = "Algoritmos y Estructuras de Datos"
        usuariogenerico.bio = ""
        usuariogenerico.pais = "Argentina"
        usuariogenerico.ciudad = "Rosario"
        usuariogenerico.fecha = str(random.randint(1,28)).rjust(2,"0")+"/"+str(random.randint(1,12)).rjust(2,"0")+"/"+str(random.randint(1990,2006))
        Format_Estudiante(usuariogenerico)
        l_estudiantes.seek(0,2)
        pickle.dump(usuariogenerico, l_estudiantes)
        l_estudiantes.flush()    

def calcular_edad(fecha):#listo#
    # (fecha: str)
    # Var:
    # Datatime: fecha_actual ; fecha_nacimiento
    # Entero: edad
    
    fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
        edad -= 1
    return edad

#MODERADOR PRECARGADO
def pre_mod():#listo#
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
def pre_admin():#listo#
    admin = Administradores()
    admin.id = 0
    admin.email = "Adminpre@ayed.com"
    admin.contraseña = "000000"
    Format_Admins(admin)
    l_administradores.seek(0,2)
    pickle.dump(admin, l_administradores)
    l_administradores.flush()
    
#LIKES ALEATORIOS PRECARGADOS
def pre_random_likes():#listo#
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
#BUSQUEDA DE ESTUDIANTE POR ID
def busca_estud_id(id):
    global estudiante
    t=os.path.getsize(r_estudiantes)#tamaño total del archivo
    l_estudiantes.seek(0,0)
    
    id = str(id).ljust(4," ")#variable que le pasamos como parametro. La ajustamos para que coincida con los usuarios formateados
    pp=0#variable que va guardando la posicion del puntero
    estudiante=pickle.load(l_estudiantes)
    while l_estudiantes.tell()<t and id!=estudiante.id:
        pp=l_estudiantes.tell()
        estudiante=pickle.load(l_estudiantes)
    if id==estudiante.id:
        pos=pp#Variable de control
    else:
        pos=-1#Variable de control
    
    return pos
#BUSQUEDA DE ESTUDIANTE POR EMAIL
def busca_estud_email(email):
    global estudiante
    t=os.path.getsize(r_estudiantes)#tamaño total del archivo
    email = email.ljust(32," ")#variable que le pasamos como parametro. La ajustamos para que coincida con los usuarios formateados
    
    l_estudiantes.seek(0)
    pp=0#variable que va guardando la posicion del puntero
    estudiante=pickle.load(l_estudiantes)
    while l_estudiantes.tell()<t and email!=estudiante.email:
        pp=l_estudiantes.tell()
        estudiante=pickle.load(l_estudiantes)
    if email==estudiante.email:
        pos=pp#Variable de control
    else:
        pos=-1#Variable de control
    
    return pos
#BUSQUEDA DE MODERADOR POR EMAIL
def busca_mod_email(email):
    global moderador
    t=os.path.getsize(r_moderadores)#tamaño total del archivo
    email = email.ljust(32," ")#variable que le pasamos como parametro. La ajustamos para que coincida con los usuarios formateados
    
    l_moderadores.seek(0,0)
    pp=0#variable que va guardando la posicion del puntero
    moderador=pickle.load(l_moderadores)
    while l_moderadores.tell()<t and email!=moderador.email:
        pp=l_moderadores.tell()
        moderador=pickle.load(l_moderadores)
    if email==moderador.email:
        pos=pp#Variable de control
    else:
        pos=-1#Variable de control

    return pos
#BUSQUEDA DE ADMIN(innecesaria, creada por las dudas)
def busca_admin(email):
    global administrador
    t=os.path.getsize(r_administradores)#tamaño total del archivo
    email = email.ljust(32," ")#variable que le pasamos como parametro. La ajustamos para que coincida con los usuarios formateados

    l_administradores.seek(0)
    pp=0#variable que va guardando la posicion del puntero
    administrador=pickle.load(l_administradores)
    while l_administradores.tell()<t and email!=administrador.email:
        pp=l_administradores.tell()
        administrador=pickle.load(l_administradores)
    if email==administrador.email:
        pos=pp#Variable de control
    else:
        pos=-1#Variable de control

    return pos
#BUSQUEDA DE REPORTES
def busca_reporte(id_reportante: int, id_reportado: int) -> int:
    global reporte
    t=os.path.getsize(r_reportes)#tamaño total del archivo
    
    pos=-1#Variable que retornamos. La iniciamos aca en -1 porque si no hay reportes nunca se define.
    if t >0:
        id_reportante = id_reportante.ljust(4," ")
        id_reportado = id_reportado.ljust(4," ")
        
        l_reportes.seek(0)
        pp = 0#variable que va guardando la posicion del puntero
        reporte = pickle.load(l_reportes)
        
        while l_reportes.tell()<t and (id_reportante != reporte.id_reportante or id_reportado != reporte.id_reportado):
            pp = l_reportes.tell()
            reporte = pickle.load(l_reportes)
        if (id_reportante == reporte.id_reportante and id_reportado == reporte.id_reportado):
            pos=pp

    return pos
#CANTIDAD DE LIKES DE UN USUARIO   
def cant_likes(id: int) -> int:
    t=os.path.getsize(r_likes)#tamaño total del archivo
    l_likes.seek(0,0)
    pickle.load(l_likes)
    t1=l_likes.tell()#Tamaño en bytes de un registro de likes
    cant=t//t1#Cantidad de likes del archivo
    
    n_likes = 0#Cantidad de likes del usuario
    for i in range(0,cant):
        l_likes.seek(i * t1,0)
        like=pickle.load(l_likes)
        if like.destinatario == id:
            n_likes += 1
    
    return n_likes  
#Funcion que verifica si el primer registro le dio like al segundo registro que se le pasa como parametro.
def is_like(estudiante1:Estudiantes,estudiante2:Estudiantes) -> int:
    t=os.path.getsize(r_likes)#tamaño total del archivo

    l_likes.seek(0,0)
    pp=0#variable que va guardando la posicion del puntero
    like=pickle.load(l_likes)
    while l_likes.tell()<t and (estudiante1.id != like.remitente or estudiante2.id != like.destinatario):
        pp=l_likes.tell()
        like=pickle.load(l_likes)
    if (estudiante1.id == like.remitente and estudiante2.id == like.destinatario):
        pos=pp#Variable de control
    else:
        pos=-1#Variable de control

    return pos
#Funcion que borra fisicamente del archivo un like
def quitar_Like(pos) -> None:
    t=os.path.getsize(r_likes)#Tamaño total del archivo
    l_likes.seek(0,0)
    pickle.load(l_likes)
    t1=l_likes.tell()#Tamaño de iun registro de likes
    
    l_likes.seek(t-t1,0)#nos ubicamos en el ultimo registro
    like_u=pickle.load(l_likes)#lo cargamos
    
    l_likes.seek(pos,0)#nos posicionamos en el like el cual pasamos su posicion para eliminar
    pickle.dump(like_u,l_likes)#lo pisamos con el que habiamos guardado
    
    l_likes.truncate(t-t1)#Truncamos el tamaño del archivo, eliminando el ultimo registro
    l_likes.flush()#Actualizamos

#Funcion dar like
def dar_Like(estudiante1:Estudiantes,estudiante2:Estudiantes) -> None:#pasamos dos estudiantes como parametro
    like = Likes()
    like.remitente = estudiante1.id #asignamos cada uno, segun el que emite el like
    like.destinatario = estudiante2.id
    #Guardamos
    format_likes(like)
    l_likes.seek(0,2)
    pickle.dump(like,l_likes)
    l_likes.flush()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#
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
    
        email = input("Email:\n\033[1;34m>>> \033[0;m")
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
    # Entero:i, pos
    # 
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

def deshabilitar_estud(pos:int,text= "¿Desea eliminar tu perfil?",color = AZUL)-> bool: #listo
    # Var:
    # String: opc
    # Estudiantes: estud
    
    opc = menu(text,"",
       ["s. Si",
        "n. No.",
        "","","","","","","",""],color)
    
    if opc == "s":
        l_estudiantes.seek(pos,0)
        estud=pickle.load(l_estudiantes)
    
        estud.estado = False
        l_estudiantes.seek(pos,0)
        pickle.dump(estud,l_estudiantes)
        l_estudiantes.flush()
        return True
    else:
        return False
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#
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
            case "3": menu_Matcheos()
            case "4": menu_reportes_estadisticos(estudiante)

def menu_moderadore(mod:Moderadores):
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
            case "2": menu_gest_reportes(mod.id, True)
            case "3": construcción()
            
def menu_administradore(admin:Administradores)-> None:                         #listo
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
        VIOLETA)

        match (opc):  
            case "1": menu_gest_usuarios_admin()
            case "2": menu_gest_reportes(admin.id,False)
            case "3": menu_reportes_estadisticos_admin()

def menu_gest_usuarios_admin():
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0":
        clear()
        opc = menu("Gestionar Usuarios","",[
        "1. Eliminar un usuario (Moderador o Estudiante).",
        "2. Dar de alta un moderador.",
        "0. Volver.",
        "","","","","","",""],
        VIOLETA)
        
        match (opc):
            case "1":
                clear()
                opc2=menu("Tipo a Eliminar","",[
                "1. Usuario.",
                "2. Moderador.",
                "","","","","","","",""],
                VIOLETA)
                match (opc2):
                    case "1":menu_desactivar_usuario(VIOLETA)
                    case "2":desactivar_mod()

            case"2": alta_mod()

def desactivar_mod():
    clear()
    opc10 = menu("Desactivar moderador","¿Esta seguro de que desea eliminar un moderador?",[
        "1. Si.",
        "2. No.",
        "","","","","","","",""],
        VIOLETA)
    if opc10=="si":
        clear()
        print("Ingrese el mail del moderador que quiere eliminar.")
        pos=input(VIOLETA+"\n>>> \033"+VACIO)
        while busca_mod_email(pos)==-1:
            clear()
            print("Email no valido.\nIntente Nuevamente.")
            print("Ingrese el mail del moderador que quiere eliminar.")
            pos=input(VIOLETA+"\n>>> \033"+VACIO)
        l_moderadores.seek(pos,0)
        vm=pickle.load(l_moderadores)
        vm.estado=False
        l_moderadores.seek(pos,0)
        pickle.dump(vm,l_moderadores)
        l_moderadores.flush()
        
def validacion_email(text: str,color = AZUL) -> str:                                        # listo
    # var
    # String: email
    # int: val, i 
    #----------------Validacion de <@> del email------------------#
    print("Ingrese su email:")
    email=input(AZUL+"\n>>> \033"+VACIO)
    val=0
    for i in range(len(email)):
        if email[i]=="@":
            val += 1 
    while val!=1:
        clear()
        cartel(text,color)
        if val>1:
            print("No existen emails con mas de un <@>.\nIntente nuevamente.")
        else:   
            print("No existen emails sin <@>.\nIntente nuevamente.")
        print("Ingrese su email:")
        email=input(AZUL+"\n>>> \033"+VACIO)
        val=0
        for i in range(len(email)):
            if email[i]=="@":
                val += 1   
    #-----------Validacion de existencia unica de email--------------#
    
    while busca_estud_email(email) !=-1 and busca_mod_email(email) !=-1:
        clear()
        cartel(text,color)
        print("Email ya utlizado.\nIntente con uno nuevo.")
        print("Ingrese su email:")
        email=input(AZUL+"\n>>> \033"+VACIO)
        #------------Validacion de <@> del email---------------------#
        val=0
        for i in range(len(email)):
            if email[i]=="@":
                val += 1 
        while val!=1:
            clear()
            cartel(text,color)
            if val>1:
                print("No existen emails con mas de un <@>.\nIntente nuevamente.")
            else:   
                print("No existen emails sin <@>.\nIntente nuevamente.")
            print("Ingrese su email:")
            email=input(AZUL+"\n>>> \033"+VACIO)
            val=0
            for i in range(len(email)):
                if email[i]=="@":
                    val += 1   
    return email
           
def alta_mod() -> None:                                                        # listo
    # var
    # Estudiantes: vm, vr
    # String: text
    # int: t, x, cant
    
    text="Registro Moderador"
    vm=Moderadores()
    clear()
    cartel(text,VIOLETA)
    
    vm.email=validacion_email(text, VIOLETA)
    
    #------------------------Contraseña-------------------------#
    clear()
    cartel(text,VIOLETA)
    vm.contraseña = getpass()
    
    #----------------------Nombre-------------------------------#
    print("Ingrese su nombre")
    vm.name = input(VIOLETA+"\n>>> \033"+VACIO)
    
   #---------------Elementos de asignacion automatica-----------#    
    vm.estado = True
    t = os.path.getsize(r_moderadores)
    l_moderadores.seek(0,0)
    vr = pickle.load(l_moderadores)
    x = l_moderadores.tell()
    cant = t//x
    l_moderadores.seek((cant-1)*x,0)
    vr = pickle.load(l_moderadores)
    vm.id = int(vr.id)+1
    
    #------------Archivar el moderador cargado------------------#
    Format_Mods(vm)
    l_moderadores.seek(0,2)
    pickle.dump(vm,l_moderadores)
    l_moderadores.flush()
    #-----------------------------------------------------------#     

def menu_registrarse() -> None:                                                # listo
    # var 
    # Estudiantes: va, vr
    # int: t, x, cant
    # String: seguir, text
    
    text = "Registro"
    clear()
    cartel(text,AZUL)
    ve=Estudiantes()
    
    ve.email=validacion_email(text)
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
    ve.sexo = menu(text, "Ingrese su sexo",
                ["f. Femenino.",
                "m. Masculino.",
                "","","","","","","",""],AZUL)
    
    #-------------------Fecha nacimiento----------------------------#
    clear()
    cartel(text,AZUL)
    ve.fecha = validar_fecha()
    
    #------------------Demas datos--------------------------------# 
    clear()
    seguir = menu(text,"¿Desea terminar de completar tus datos personales ahora?"
        ["s. Si",
        "n. No.",
        "","","","","","","",""],AZUL)
    
    if seguir=="s":
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
    vr=pickle.load(l_estudiantes)
    x=l_estudiantes.tell()
    cant=t//x
    l_estudiantes.seek((cant-1)*x,0)
    vr=pickle.load(l_estudiantes)
    ve.id = int(vr.id)+1
    
    #------------Archivar el estudiante cargado-----------------------#
    Format_Estudiante(ve)
    l_estudiantes.seek(0,2)
    pickle.dump(ve,l_estudiantes)
    l_estudiantes.flush()

def menu_reportes_estadisticos_admin() -> None:                                # listo
    clear()
    cartel("Menu de Reportes Estadisticos",VIOLETA)
    print(VIOLETA+"\n° "+VACIO+"Cantidad de reportes realizados por los estudiantes: ",cant_rep_totales())
    print(VIOLETA+"° "+VACIO+"Porcentaje de reportes ignorados: ",cant_rep_por_estado("2"))
    print(VIOLETA+"° "+VACIO+"Porcentaje de reportes aceptados: ",cant_rep_por_estado("1"))
    print(VIOLETA+"° "+VACIO+"Moderador que mayor cantidad de reportes ha ignorado : ",mod_con_mas_x_estado("reportes_ignorados","ignorado"))
    print(VIOLETA+"° "+VACIO+"Moderador que mayor cantidad de reportes ha aceptado : ",mod_con_mas_x_estado("reportes_aceptados","aceptado"))
    print(VIOLETA+"° "+VACIO+"Moderador que mayor cantidad de reportes ha procesado: ",cant_rep_mod())
    print("\nOprima cualquier tecla para volver al menu anterior\n")
    getch()
   
def cant_rep_totales() -> int:                                                 # listo
    # var
    # int: t, x
    t=os.path.getsize(r_reportes)
    l_reportes.seek(0,0)
    pickle.load(l_reportes)
    x=l_reportes.tell()#longitud de un registro de reportes
    return t//x

def cant_rep_por_estado(estado:str) -> int:                                    # listo
    # var 
    # int: x, i, k
    # Reportes: vr
    
    x=cant_rep_totales()
    i=0
    
    for k in range(x):
        l_reportes.seek(0,0)
        vr=pickle.load(l_reportes)
        if vr.estado==estado:
            i += 1
        
    return (i*100)/x

def mod_con_mas_x_estado(estado:str,name:str) -> str:                          # listo
    # var 
    # int: t, i
    # String: salida
    # Moderadores: mod
    
    t=os.path.getsize(r_moderadores)
    
    salida = "" 
    i=1
    l_moderadores.seek(0,0)
    while l_moderadores.tell()<t:        
        mod=pickle.load(l_moderadores)
        if int(mod.__dict__[estado])>i:
            i=int(mod.__dict__[estado])
            salida = mod.name
        elif int(mod.__dict__[estado]) == i:
            salida = salida + ", " + mod.name
            
    if salida=="":
        salida = f"No se han {name} reportes"

    return salida

def cant_rep_mod() -> str:                                                     # listo
    # var 
    # int: t, i
    # String: salida
    # Moderadores: mod
    
    t=os.path.getsize(r_moderadores)
    
    salida=""
    i=1
    l_moderadores.seek(0,0)
    while l_moderadores.tell()<t:
        mod=pickle.load(l_moderadores)
        if int(mod.reportes_aceptados)+int(mod.reportes_ignorados)>i:
            i=int(mod.reportes_aceptados)+int(mod.reportes_ignorados)
            salida=mod.name
        elif int(mod.reportes_aceptados)+int(mod.reportes_ignorados) == i:
            salida = salida + ", " + mod.name
            
    if salida=="":
        salida = "No se han visto reportes"
    
    return salida

#-----------------------------------------------------------#
# menu Gestionar mi perfil de nivel 2 dentro de menu estudiantes   
def menu_perfil(estudiante:Estudiantes) -> None:                               # listo
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

def menu_editar_datos(estudiante:Estudiantes) -> None:                         # listo
    # var:
    # String: opc, estab
    # int: pos
    
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
        
        if opc != "0":
            
            pos=busca_estud_id(estudiante.id)
            l_estudiantes.seek(pos,0)
            estudiante = pickle.load(l_estudiantes)
            
            match opc:
                case "1":
                    clear()
                    opc = menu("Cambio del dato Fecha de Nacimiento",f"Su Fecha de Nacimiento ya establecida es: {estudiante.fecha}.\n¿Desea cambiarlo?",
                    ["s. Si",
                    "n. No.",
                    "","","","","","","",""],AZUL)
                    clear()
                    if opc=="s":
                        estudiante.fecha = validar_fecha()
                        
                case "4": 
                    clear()
                    if estudiante.sexo == "f":
                        estab="Femenino"
                    else:
                        estab="Masculino"
                    
                    opc = menu("Cambio del dato sexo",f"Su sexo ya establecida es: {estab}.\n¿Desea cambiarlo o volver?",
                       ["f. Femenino.",
                        "m. Masculino.",
                        "o. Volver (no cambiar).",
                        "","","","","","",""],AZUL)
                    
                    if opc != "o":
                        estudiante.sexo=opc 
                    
                case "3": cambio_dato_estudiante("name",estudiante,"Nombre") 
                case "2": cambio_dato_estudiante("bio",estudiante,"Biografia") 
                case "5": cambio_dato_estudiante("materia_fav",estudiante,"Materia Favorita")
                case "6": cambio_dato_estudiante("pais",estudiante,"País")
                case "7": cambio_dato_estudiante("ciudad",estudiante,"Ciudad") 

            l_estudiantes.seek(pos,0)
            Format_Estudiante(estudiante)
            pickle.dump(estudiante,l_estudiantes)
            l_estudiantes.flush()

def cambio_dato_estudiante(dato:str,estudiante:Estudiantes,opcion:str) -> None:# listo
    # var:
    # String: opc
    
    clear()
    opc = menu("Cambio del dato "+opcion,f"Su {opcion} ya establecida es: \n{estudiante.__dict__[dato]}\n¿Desea cambiarlo?",
       ["s. Si",
        "n. No.",
        "","","","","","","",""],AZUL)
    clear()
    
    if opc=="s":
        cartel(f"Cambio del dato "+opcion,AZUL)
        print(f"Ingrese su nuevo/a {opcion}:")
        estudiante.__dict__[dato] = input(AZUL+"\n>>> "+VACIO)

# menu Gestionar candidatos de nivel 2 dentro de menu estudiantes 
def menu_candidatos(estudiante:Estudiantes) -> None:                           #listo
    # var:
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0":
        clear()
        if estudiante.revelar:
            opc = menu("Gestionar candidatos","",[
                "1. Ver candidatos.",
                "2. Reportar un candidato.",
                "3. Revelar Candidatos.",
                "0. Volver.",
                "","","","","",""],
                AZUL)  
        else:
            opc = menu("Gestionar candidatos","",[
                "1. Ver candidatos.",
                "2. Reportar un candidato.",
                "0. Volver.",
                "","","","","","",""],
                AZUL)
            
        match opc:
            case "1": menu_ver_candidatos(estudiante)
            case "2": menu_reportar(estudiante)
            case "3": bonus3(estudiante)
#--------------------Listado de candidatos------------------------------#
def menu_ver_candidatos(estudiante:Estudiantes) -> None:                       #listo 
    #
    # type:
    #   A_5_str = array[0..4] of String
    #   A_6_str = array[0..5] of String
    #   A_5_int = array[0..4] of int
    
    # var:
    # String: ch, prech
    # Entero: t, t1, min, max, pos, pp, i
    # Estudiantes: estud
    # A_6_str: opcv
    # A_5_str: opcs 
    # A_5_int: estados
    
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    pickle.load(l_estudiantes)
    t1=l_estudiantes.tell()
    
    min = 0
    l_estudiantes.seek(0,0)
    estud=pickle.load(l_estudiantes)
    while estud.estado == False:
        min=l_estudiantes.tell()
        estud=pickle.load(l_estudiantes)
        
    max = t
    l_estudiantes.seek(t-t1)
    estud=pickle.load(l_estudiantes)
    while estud.estado == False:
        max=l_estudiantes.tell()-t1
        l_estudiantes.seek(max-t1)
        estud=pickle.load(l_estudiantes)
        
    # arreglo donde guardo las opciones que se van a mostrar 
    opcs = [" << A << ","  Q. salir   ","     L. Quitar Like      ",""," >> S >> "]
    # arreglo donde guardo las opciones validas que tiene el usuario
    opcv = [ b'\r', b'q', b's', b'q', b'l', b'w'] 
    # arreglo de los estado de los botones
    estado = [0,1,1,3,1]
    # 0 no se muestra
    # 1 se muestra normal
    # 2 se muestra verde
    # 3 se muestra la cantidad de likes

    ch = ""
    prech = ""
    pos = min

    l_estudiantes.seek(pos)
    estud = pickle.load(l_estudiantes)

    while prech != b'q' or (ch !=  b'\r' and ch != b'q'):
        
        estado[2] = 1
        opcv[4] = b'l'
        
        # dependiendo de lo que el usuario ingreso realizo la opcion correspondiente      
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
                    if pp != -1:
                        quitar_Like(pp)
                    else:
                        dar_Like(estudiante,estud)

                case b'w':
                    if is_like(estudiante,estud) == -1:
                        dar_Like(estudiante,estud)
                        
                    if is_like(estud,estudiante) == -1:
                        dar_Like(estud,estudiante)
                    estudiante.super_like=False
                    
    
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
                
        elif ch ==  b'w':
            if prech == ch:
                if is_like(estudiante,estud) == -1:
                    dar_Like(estudiante,estud)
                        
                if is_like(estud,estudiante) == -1:
                    dar_Like(estud,estudiante)
                estudiante.super_like=False
                
            else:
                prech = b'w'
            
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
                if pp != -1:
                    quitar_Like(pp)
                else:
                    dar_Like(estudiante,estud)
            else:
                prech = b'l'
            
        # limito que no se pase de los limites del archivo
        if min >= pos:
            opcv[1] = b'q'
            estado[0] = 0
        
        if pos >= max-t1:
            opcv[2] = b'q'
            estado[4] = 0
            
        if is_like(estudiante,estud)!=-1:
            opcs[2] = "     L. Quitar Like      "
        else:
            opcs[2] = "       L. Dar Like       "

        clear()
        # preparo lo que voy a mostrar y lo dibujo en pantalla 
        print(f"""{AZUL}╔════════════════════════════════════╦════════════════════════════╦═══════╗
║{VACIO}""",end="")
        if estud.id != estudiante.id:
            print("   Nombre  ",end="")
        else:
            print(" Tu nombre ",end="")
            estado[2] = 0
            opcv[4] = b'q'
        print(f"""{AZUL}:{VACIO} {estud.name[:22].ljust(22," ")} {AZUL}║{VACIO}      Biografia.            {AZUL}║\033[4;34mID:{estud.id}{VACIO+AZUL}║
║{VACIO}   Email   {AZUL}:{VACIO} {estud.email[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[0:34]} {AZUL}║
║{VACIO}   Pais    {AZUL}:{VACIO} {estud.pais[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[34:68]} {AZUL}║
║{VACIO}   Ciudad  {AZUL}:{VACIO} {estud.ciudad[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[68:102]} {AZUL}║
║{VACIO}   Sexo    {AZUL}:{VACIO} """,end="")
        if estud.sexo == "m":
            print("Masculino             ",end="")
        else:
            print("Femenino              ",end="")
        
        print(f""" {AZUL}║{VACIO} {estud.bio[102:136]} {AZUL}║
║{VACIO}   Edad    {AZUL}:{VACIO} {str(calcular_edad(estud.fecha))[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[136:170]} {AZUL}║
║{VACIO} Nacimiento{AZUL}:{VACIO} {estud.fecha[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[170:204]} {AZUL}║
║{VACIO} MateriaFav{AZUL}:{VACIO} {estud.materia_fav[:22].ljust(22," ")} {AZUL}║{VACIO} {estud.bio[204:238]} {AZUL}║
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
                case 3:
                    print(" likes: " +str(cant_likes(estud.id)).center(4)+" ",end="")
            print(AZUL+"║",end="")
                    
        print("\n╚═════════╩═════════════╩═════════════════════════╩═════════════╩═════════╝")
        
        if estudiante.super_like and estud.id != estudiante.id:
            opcv[5] = b'w'
            print(BLANCO+"¡¡Tenes un superlike disponible!!\nPresiona 'w' y enter para usarlo.")
        else:
            opcv[5] = b'q'
        
        # leo y verifico lo que ingresa el usuario
        ch = "" 
        while ch !=  opcv[0] and ch !=  opcv[1] and ch !=  opcv[2] and ch !=  opcv[3] and ch !=  opcv[4] and ch != opcv[5]:
            ch = getch().lower()
            
    l_estudiantes.seek(int(estudiante.id)*t1,0)
    pickle.dump(estudiante,l_estudiantes)
    l_estudiantes.flush()

#-----------Bonus 3----------------#
def bonus3(ve:Estudiantes) -> None:
    ve2=Estudiantes()#Defino el tipo de variable
    t=os.path.getsize(r_estudiantes)#Tamaño total del archivo
    l_estudiantes.seek(0,0)
    cont=1#Inicializo un contador para mostrar solo 4
    while l_estudiantes.tell()<t:
        ve2=pickle.load(l_estudiantes)
        if is_like(ve,ve2)==-1 and is_like(ve2,ve)!=-1:
            print(f"{cont}. {ve2.name} te ha dado like, pero tu no le has respondido.\nSu email: {ve.email}.\nSu id: {ve.id}.\n#-----------------------------------#")
            cont+=1
        if cont==4:
            l_estudiantes.seek(t,0)
    if cont==1:
        print("Nadie le ha dado like")
        cartel("Usted podra acceder a esta opcion hasta que se pueda mostrar al menos una persona que le haya dado like.",AZUL)
    if cont!=1:
        ve.revelar=False
        pickle.dump(ve,l_estudiantes)
        l_estudiantes.flush()
        cartel("Usted no podra acceder a esta opcion de nuevo.\nPresione cualquier tecla para volver.",AZUL)
    getch()
    
    
def menu_reportar(estudiante:Estudiantes) -> None:                             #listo
    # Var
    # String: email, opc, men
    # Entero: pos, id, pos_r
    # Estudiantes: estud
    # Reportes: reporte
    
    clear()
    opc = menu("Reportar estudiante","Seleccione el metodo que quiere utilizar.",[
    "1. Desde el id.",
    "2. Desde el email de usuario.",
    "0. Volver.",
    "","","","","","",""],
    AZUL)
    
    if opc != "0":
        
        pos = -1
        men = ""
        while pos < 0:
            clear()
            cartel("Reportar estudiante ", AZUL)
            print(AMARILLO+men+VACIO)
            
            if opc == "1":
                print("Ingrese el id del estudiante que desea reportar. ")
                try:
                    men = "Dato Invalido."
                    id = int(input(AZUL+"\n>>> "+VACIO))
                    pos = busca_estud_id(id)
                    men = "Id no encontrado."
                    if pos != -1:
                        l_estudiantes.seek(pos,0)
                        estud = pickle.load(l_estudiantes)
                        if estud.estado == False:
                            pos = -1
                        if estud.id == estudiante.id:
                            men = "No te puedes reportar a ti mismo."
                            pos = -1 
                except:
                    pos = -1
                    
            else:
                print("Ingrese el email del estudiante que desea reportar.")
                email = input(AZUL+"\n>>> "+VACIO)
                pos = busca_estud_email(email)
                men = "Id no encontrado."
                if pos != -1:
                    l_estudiantes.seek(pos,0)
                    estud = pickle.load(l_estudiantes)
                    if estud.estado == False:
                        
                        pos = -1 
                    if estud.email == estudiante.email:
                        men = "No te puedes reportar a ti mismo."
                        pos = -1
                
        clear()

        opc = "s"
        pos_r = busca_reporte(estudiante.id, estud.id)
        if pos_r == -1:
            opc = menu("Reportar estudiante","Estudiante econtrado con el nombre: "+estud.name+"\n¿Quiere proceder con el reporte?",
            ["s. Si",
            "n. No.",
            "","","","","","","",""],AZUL)
        
            if opc == "s":
                clear()
                cartel("Reportar estudiante ", AZUL)
            
                
                reporte = Reportes()
                print("\nIngrese la razon del reporte")               
                reporte.razon = input(AZUL+"\n>>> "+VACIO)
                reporte.id_reportado = estud.id
                reporte.id_reportante = estudiante.id
                
                l_reportes.seek(0,2)
                Format_Reportes(reporte)
                pickle.dump(reporte,l_reportes)
                l_reportes.flush()
                    
        else:
            l_reportes.seek(pos_r)
            reporte = pickle.load(l_reportes)
        
        if opc == "s":
            clear()
            cartel("Reportar estudiante ", AZUL)
            print("\nUsuario ya reportado")
            print("La razon fue: ",reporte.razon)
            print("El reporte: ",end="")
                
            match str(reporte.estado):
                case "0": print("No ha sido visto")
                case "1": print("Ha sido exitoso")
                case "2": print("Ha sido ignorado")
            
            
            
            print("Oprima cualquier tecla para volver al menu anterior\n")
            getch()
    
# menu Gestionar candidatos de nivel 2 dentro de menu estudiantes
def menu_Matcheos() -> None:                                                   #listo
    # var:
    # string: opc
    
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    while opc!="0":
        clear()
        opc = menu("Matcheos","",[
        "1. Ver matcheos..",
        "2. Eliminar un matcheo.",
        "0. Volver.",
        "","","","","","",""],
        AZUL)
  
        match opc:
            case "1": construcción()            
            case "2": construcción()            

# menu Reportes estadísticos de nivel 2 dentro de menu estudiantes
def menu_reportes_estadisticos(estudiante) -> None:                            # listo
    # Var
    # Entero: cont_like, like_norec, like_nodev, c_est
    # Estudiantes: estud
    # float: por_match
    clear()
    cont_like = 0
    like_norec = 0
    like_nodev = 0
    por_match = 0.0
    c_est = 0
    
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)

    while l_estudiantes.tell() < t:
        estud=pickle.load(l_estudiantes)
        if estud.estado and estud.id != estudiante.id:
            c_est+=1
            
        
        if is_like(estudiante,estud) != -1 and is_like(estud,estudiante) != -1:
            cont_like += 1

        if is_like(estudiante,estud) != -1 and is_like(estud,estudiante) == -1:
            like_norec += 1

        if is_like(estudiante,estud) == -1 and is_like(estud,estudiante) != 1:
            like_nodev += 1
            
    por_match = (cont_like * 100) / c_est

    cartel("Reportes Estadísticos",AZUL)
    
    print(AZUL+"\n° "+VACIO+"Matcheados sobre el % posible: ",por_match,"%" )
    print(AZUL+"° "+VACIO+"Likes dados y no recibidos: ", like_norec)
    print(AZUL+"° "+VACIO+"Likes recibidos y no repondidos: ", like_nodev)
    print("\nOprima cualquier tecla para volver al menu anterior\n")
    getch()
   

#----------------------------------------------------------------------------#
# menu Gestionar usuarios de nivel 2 dentro de menu moderadores 
def menu_gest_usuario(color = CIAN) -> None:                                   # listo
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

        if opc == "1": menu_desactivar_usuario(color)

def menu_desactivar_usuario(color = CIAN) -> None:                             # listo
    # Var
    # Entero: user, pos
    # String: opc

    clear()
    opc = menu("Desactivar usuario","Seleccione el metodo que quiere utilizar.",[
    "1. Desde el id.",
    "2. Desde el email de usuario.",
    "0. Volver.",
    "","","","","","",""],
    color)

    if opc != "0":
        
        pos = -1
        men=""
        while pos < 0:
            clear()
            cartel("Desactivar usuario ", color)
            print(AMARILLO+men+VACIO)
            
            if opc == "1":
                print("Ingrese el id del usuario que desea desactivar: ")
                try:
                    men = "Dato Invalido."
                    user = int(input(AZUL+"\n>>> "+VACIO))
                    pos = busca_estud_id(user)
                    men = "Id no encontrado."
                    if pos != -1:
                        l_estudiantes.seek(pos,0)
                        estudiante = pickle.load(l_estudiantes)
                        if estudiante.estado == False:
                            pos = -1          
                except:
                    pos = -1    
            else:
                print("Ingrese el email del usuario que desea desactivar: ")
                user = input(AZUL+"\n>>> "+VACIO)
                pos = busca_estud_email(user)
                men = "Email no encontrado."
                if pos != -1:
                    l_estudiantes.seek(pos,0)
                    estudiante = pickle.load(l_estudiantes)
                    if estudiante.estado == False:
                        pos = -1

                
            invalido()
        clear()

        if deshabilitar_estud(pos,"¿Desea desactivar este perfil?",color):
            cartel("El usuario ha sido desactivado",color)
        else:
            cartel("El usuario no ha sido desactivado",color)
        print("Oprima cualquier tecla para volver al menu anterior")
        getch()
    
# menu Gestionar reportes de nivel 2 dentro de menu moderadores 
def menu_gest_reportes(id: int,is_mod = True) -> None:                         # listo
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

        if opc == "1": menu_reportes(id, is_mod)
  
def menu_reportes(id: int,is_mod = True) -> None:
    #
    # type:
    # A_99_int = array[0..99] of int
    
    # Var
    # Entero: t1_r, i, n_reportes, t, pp, t1_e, _t1_m
    # String: opc, salida, color
    # A_99_int: array_reporte
    # Reportes: reporte
    # Estudiantes: estud1, estud2
    # Moderadores: mod
    
    
    if is_mod:
        color = CIAN
    else:
        color = VIOLETA
        
    opc = ""
    while opc != "n":
        
        t=os.path.getsize(r_reportes)
        salida = ""
        n_reportes = 0
        array_reporte = [0]*99
        
        if t > 0:
            l_reportes.seek(0,0)
            pickle.load(l_reportes)
            t1_r=l_reportes.tell()

            
            l_reportes.seek(0,0)
            pp = 0
            while pp <t and n_reportes < 100:
                
                reporte = pickle.load(l_reportes)
                if reporte.estado == "0":
                
                    if n_reportes == 0:
                        salida += color+"╔"+"═"*73+"╗\n"
                        salida += "║ "+BLANCO+"Gestionar reportes".center(71)+color+" ║\n"
                        salida += "╠════╦════════╦═════════╦═════════════════════════════════════════════════╣\n"
                        salida += "║    ║"+BLANCO+" ID Del "+color+"║"+BLANCO+" ID Del  "+color+"║                                                 ║\n"
                        salida += "║"+BLANCO+" N° "+color+"║"+BLANCO+" Emisor "+color+"║"+BLANCO+" Acusado "+color+"║"+BLANCO+"                     Razon                       "+color+"║\n"
                    salida += "╠════╬════════╬═════════╬═════════════════════════════════════════════════╣\n"
                    
                    salida += "║ "+BLANCO+str(n_reportes).ljust(2)+color + " ║  "+BLANCO+reporte.id_reportante+color
                    salida += "  ║   "+BLANCO+reporte.id_reportado+color + "  ║ "+BLANCO+reporte.razon.center(49)+color
                    array_reporte[r_reportes] = pp
                    n_reportes += 1
                    
                pp = l_reportes.tell()
                    
            salida += "\n╚════╩════════╩═════════╩═════════════════════════════════════════════════╝\n"
            salida += "Ingrese el N° de reporte que desea modificar\n"


        if n_reportes > 0:
            
            men = ""
            n = -1
            while n < 0 or n >=n_reportes:
                clear()
                print(salida)
                print(AMARILLO+men+VACIO)
                
                try:
                    n = int(input(AZUL+"\n>>> "+VACIO))
                    men = "dato fuera de rango"
                except:
                    n = -1
                    men = "Dato Invalido."
            clear()
            
            l_estudiantes.seek(0,0)
            pickle.load(l_estudiantes)
            t1_e=l_estudiantes.tell()
            
            l_reportes.seek(array_reporte[n]*t1_r,0)
            reporte = pickle.load(l_reportes)
            
            l_estudiantes.seek(reporte.id_reportante*t1_e,0)
            estud1 = pickle.load(l_estudiantes)
            
            l_estudiantes.seek(reporte.id_reportado*t1_e,0)
            estud2 = pickle.load(l_estudiantes)
            
            opc = menu("Gestionar reportes",f"El reporte del usuario ({reporte.id_reportante}) {estud1.name} hacia ({reporte.id_reportado}) {estud2.name} por la razon:\n {reporte.razon.center}\n¿Desea desactivar a este usuario?",
               ["s. Si",
                "n. No.",
                "","","","","","","",""],color)
            
            if is_mod:
                l_moderadores.seek(0,0)
                pickle.load(l_moderadores)
                t1_m=l_moderadores.tell()
                
                l_moderadores.seek(id*t1_m,0)
                mod = pickle.load(l_moderadores)
                salida = ""
                
                if opc == "s":
                    estud2.estado = False
                    reporte.estado = "1"
                    mod.reportes_aceptados = int(mod.reportes_aceptados) + 1
                    
                    l_estudiantes.seek(reporte.id_reportado*t1_e,0)
                    pickle.dump(estud2, l_estudiantes)
                    l_estudiantes.flush()
                else : 
                    reporte.estado = "2"
                    mod.reportes_ignorados = int(mod.reportes_ignorados) + 1
                    
                l_moderadores.seek(id*t1_m,0)
                pickle.dump(mod, l_moderadores)
                l_moderadores.flush()
            
            else:
                if opc == "s":
                    estud2.estado = False
                    reporte.estado = "1"
                    
                    l_estudiantes.seek(reporte.id_reportado*t1_e,0)
                    pickle.dump(estud2, l_estudiantes)
                    l_estudiantes.flush()
                
                else : 
                    reporte.estado = "2"      
                
            l_reportes.seek(array_reporte[n]*t1_r,0)
            pickle.dump(reporte,l_reportes)
            l_reportes.flush()
                     
                
            opc = menu("Gestionar reportes",salida+"¿Desea ver otros reportes?",
                ["s. Si",
                "n. No.",
                "","","","","","","",""],color)
                
            clear()
                
        else:
            opc = "n"
            cartel("Gestionar reportes",color)
            print("Actualmente no hay reportes para ver.\n")
            print("Oprima cualquier tecla para volver al menu anterior")
            getch()
    clear()

abrir_archivos()#Llamamos a funcion para crear o abrir archivos
#-----------MENU PRINCIPAL DEL PROGRAMA--------------#
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