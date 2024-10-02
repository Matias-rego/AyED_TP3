#-------------------------------DEFINICION DE CLASES-------------------------------#
#ESTUDIANTES
class Estudiantes:
    def __init__(self) -> None:
        self.id = 0
        self.estado = False
        self.email = ""
        self.contraseña = ""
        self.name = ""
        self.sexo = ""
        #self.deporte = ""
        self.materia_fav = ""
        # self.materia_fuerte= ""
        # self.materia_debil =""
        self.bio = ""
        self.pais =""
        self.ciudad = ""
        self.fecha = ""
        
def Format_Estudiante(x):
    x.id             = str(x.id).ljust(4," ")
    x.email          = x.email.ljust(32," ")
    x.contraseña     = x.contraseña.ljust(16," ")
    x.name           = x.name.ljust(32," ")
    x.materia_fav    = x.materia_fav.ljust(16," ")
    x.bio            = x.bio.ljust(255," ")
    x.pais           = x.pais.ljust(32," ")
    x.ciudad         = x.ciudad.ljust(32," ")
    x.fecha          = x.fecha.ljust(10," ")
    #x.materiafuerte = x.materiafuerte.ljust(16, " ")
    #x.materiadebil  = x.materiadebil.ljust(16,"")
    #x.deporte=x.deporte.ljust(16," ")
    
#MODERADORES  
class Moderadores:
    def __init__(self) -> None:
        self.id         = 0
        self.email      = ""
        self.contraseña =""
        self.name       = ""
        self.estado     = False

def Format_Mods(x):
    x.id         =str(x.id)
    x.id         = x.id.ljust(4," ")
    x.email      = x.email.ljust(16," ")
    x.contraseña =x.contraseña.ljust(32," ")
    x.name       = x.name.ljust(32," ")

#ADMINS        
class Administradores:
    def __init__(self) -> None:
        self.id=0
        self.email=""
        self.contraseña=""

def Format_Admins(x):
    x.id         =str(x.id).ljust(4," ")
    x.email      =x.email.ljust(32," ")
    x.contraseña =x.contraseña.ljust(16," ")

#LIKES
class Likes:
    def __init__(self) -> None:
        self.remitente= 0
        self.destinatario = 0

def Format_likes(x):
    x.remitente      = str(x.remitente).ljust(4," ")
    x.destinatario   = str(x.destinatario).ljust(4," ")

#REPORTES
class Reportes:
    def __init__(self) -> None:
        self.id_reportante=0
        self.id_reportado=0
        self.razon=""
        self.estado=False
        
def Format_Reportes(x):
    x.id_reportado  = str(x.id_reportado).ljust(4," ")
    x.id_reportante = str(x.id_reportante).ljust(4," ")
    x.razon         = x.razon.ljust(255," ")