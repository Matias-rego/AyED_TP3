class Estudiantes:
    def __init__(self) -> None:
        self.id = 0
        self.email = ""
        self.contraseña = ""
        self.name = ""
        self.sexo = ""
        #self.deporte = ""
        self.estado = False
        self.materia_fav = ""
        # self.materia_fuerte= ""
        # self.materia_debil =""
        self.bio = ""
        self.pais =""
        self.ciudad = ""
        self.fecha = ""

    def Format_Estudiante(self):
        self.id             = str(self.id).ljust(4," ")
        self.email          = self.email.ljust(32," ")
        self.contraseña     =self.contraseña.ljust(32," ")
        self.name           =self.name.ljust(32," ")
        self.materia_fav    =self.materia_fav.ljust(13," ")
        self.bio            =self.bio.ljust(255," ")
        self.pais           =self.pais.ljust(32," ")
        self.ciudad         =self.ciudad.ljust(32," ")
        self.fecha          = self.fecha.ljust(10," ")
        #self.materiafuerte = self.materiafuerte.ljust(16, " ")
        #self.materiadebil  = self.materiadebil.ljust(16,"")
        #self.deporte=self.deporte.ljust(16," ")
        
class Moderadores:
    def __init__(self) -> None:
        self.id         = 0
        self.email      = ""
        self.contraseña =""
        self.name       = ""
        self.estado     = False

    def Format_Mods(self):
        self.id         =str(self.id)
        self.id         = self.id.ljust(4," ")
        self.email      = self.email.ljust(32," ")
        self.contraseña =self.contraseña.ljust(32," ")
        self.name       = self.name.ljust(32," ")


         
class Administradores:
    def __init__(self) -> None:
        self.id=0
        self.email=""
        self.contraseña=""
        
    def Format_Admins(self):
        self.id         =str(self.id).ljust(4," ")
        self.email      =self.email.ljust(32," ")
        self.contraseña =self.contraseña.ljust(32," ")

class Likes:
    def __init__(self) -> None:
        self.remitente=0
        self.destinatario = 0
        
    def Format_likes(self):
        self.remitente      = str(self.remitente).ljust(4," ")
        self.destinatario   = str(self.destinatario).ljust(4," ")

class Reportes:
    def __init__(self) -> None:
        self.id_reportante=0
        self.id_reportado=0
        self.razon=""
        self.estado=False
    def Format_Reportes(self):
        self.id_reportado  = str(self.id_reportado).ljust(4," ")
        self.id_reportante = str(self.id_reportante).ljust(4," ")
        self.razon         = self.razon.ljust(255," ")