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
        self.super_like = True
        self.revelar = True
        
def Format_Estudiante(x:Estudiantes):
    x.id             = str(x.id)[:4].ljust(4," ")
    x.email          = x.email[:32].ljust(32," ")
    x.contraseña     = x.contraseña[:16].ljust(16," ")
    x.name           = x.name[:22].ljust(22," ")
    x.materia_fav    = x.materia_fav[:22].ljust(22," ")
    x.bio            = x.bio[:238].ljust(238," ")
    x.pais           = x.pais[:22].ljust(22," ")
    x.ciudad         = x.ciudad[:22].ljust(22," ")
    x.fecha          = x.fecha[:10].ljust(10," ")
    #x.materiafuerte = x.materiafuerte[:16].ljust(16, " ")
    #x.materiadebil  = x.materiadebil[:16].ljust(16,"")
    #x.deporte=x.deporte[:16].ljust(16," ")
    
#MODERADORES  
class Moderadores:
    def __init__(self) -> None:
        self.id         = 0
        self.email      = ""
        self.contraseña = ""
        self.name       = ""
        self.estado     = False
        self.reportes_aceptados = 0
        self.reportes_ignorados = 0

def Format_Mods(x):
    x.id         =str(x.id)
    x.id         = x.id[:4].ljust(4," ")
    x.email      = x.email[:32].ljust(32," ")
    x.contraseña =x.contraseña[:16].ljust(16," ")
    x.name       = x.name[:22].ljust(22," ")
    x.reportes_aceptados=str(x.reportes_aceptados)
    x.reportes_aceptados=x.reportes_aceptados[:4].ljust(4," ")
    x.reportes_ignorados=str(x.reportes_ignorados)
    x.reportes_ignorados=x.reportes_ignorados[:4].ljust(4," ")
    
#ADMINS        
class Administradores:
    def __init__(self) -> None:
        self.id=0
        self.email=""
        self.contraseña=""

def Format_Admins(x):
    x.id         =str(x.id)[:4].ljust(4," ")
    x.email      =x.email[:32].ljust(32," ")
    x.contraseña =x.contraseña[:16].ljust(16," ")

#LIKES
class Likes:
    def __init__(self) -> None:
        self.remitente= 0
        self.destinatario = 0

def format_likes(x):
    x.remitente      = str(x.remitente)[:4].ljust(4," ")
    x.destinatario   = str(x.destinatario)[:4].ljust(4," ")

#REPORTES
class Reportes:
    def __init__(self) -> None:
        self.id_reportado=0
        self.id_reportante=0
        self.razon = ""
        self.estado = "0"
        
def Format_Reportes(x):
    x.id_reportado  = str(x.id_reportado)[:4].ljust(4," ")
    x.id_reportante = str(x.id_reportante)[:4].ljust(4," ")
    x.razon         = x.razon[:49].ljust(49," ")
    x.estado = str(x.estado)[:1].ljust(1," ")
    