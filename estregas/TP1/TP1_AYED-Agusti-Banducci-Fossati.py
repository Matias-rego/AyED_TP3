#------------------------INTEGRANTES:----------------------
#AGUSTI, TOMAS
#FOSSATI, NICOLÁS
#BANDUCCI, MARCOS
#BOTTA, FRANCESCO
#----------------------------------------------------------
#GESTIONAR DATOS PERSONALES VARS
dia,mes,año=0,0,0
biografia_1=""
biografia_2=""
biografia_3=""
h_1=""
h_3=""
h_2=""
edad_1=""
edad_2=""
edad_3=""
fecha_nacimiento_1=0
fecha_nacimiento_2=0
fecha_nacimiento_3=0
name_1="usuario1"
name_2="usuario2"
name_3="usuario3"
apellido_1=""
apellido_2=""
apellido_3=""
name=""
apellido=""
listan=[name_1,name_2,name_3]
lista1=[name_1,apellido_1, biografia_1,fecha_nacimiento_1,h_1,edad_1]
lista2=[name_2,apellido_2,biografia_2,fecha_nacimiento_2,h_2,edad_2]
lista3=[name_3,apellido_3, biografia_3,fecha_nacimiento_3,h_3,edad_3]
#Importando modulos necesarios
import os
from getpass import *
from datetime import datetime

#Constantes globales para el ingreso
mailuser_1 = "estudiante1@ayed.com"
mailuser_2 = "estudiante2@ayed.com"
mailuser_3 ="estudiante3@ayed.com"
passuser_1 = "111222"
passuser_2 = "333444"
passuser_3 = "555666"

listauser={(mailuser_1,passuser_1),(mailuser_2,passuser_2),(mailuser_3,passuser_3)}

#Función ingresar y validar datos
#userintroducido=mailuser que entro=>string
#passintroducida=passuser del mailuser=>string
#Función ingresar y validar datos
def INGRESO_VALIDACION():
	global passintroducida, userintroducido
	intentos=3
	
	userintroducido = input("Ingrese su usuario: ")
	passintroducida = getpass('Ingrese su contraseña:')
	intentos = intentos-1
	user_on=userintroducido,passintroducida
	while (user_on not in listauser)and intentos>0:
		os.system("cls")
		print("ACCESO ERRONEO, LE QUEDAN",intentos,"INTENTOS")
		userintroducido = input("Ingrese su usuario: ")
		passintroducida = getpass('Ingrese su contraseña:')
		intentos = intentos-1
		user_on=userintroducido,passintroducida
	if intentos==0:
		os.system("cls")
		print("SISTEMA BLOQUEADO==>INTENTOS AGOTADOS")
	else:
		os.system("cls")
		print("Acceso correcto al sistema")
		MENU()


#CALCULADOR DE EDADES
#DATETIME modulo para calcular la edad con fecha del momento de la ejecucion

def NOMBRE():
	global name_1, name_2, name_3, apellido_1, apellido_2, apellido_3, name, apellido
	name=input("Ingrese su nombre;")
	apellido=input("Ingrese su apellido;")
	if userintroducido==mailuser_1:
		name_1=name
		apellido_1=apellido
	elif userintroducido==mailuser_2:
		name_2=name
		apellido_2=apellido
	elif userintroducido==mailuser_3:
		name_3=name
		apellido_3=apellido
	os.system("cls")
	EDITAR_DATOS()


def FECHA_NACIMIENTO():
	global fecha_nacimiento_1, fecha_nacimiento_2, fecha_nacimiento_3, edad_1, edad_2, edad_3
	q=1
	fechaF = input("ingrese fecha de nacimiento (dd/mm/yyyy): ")
	while q==1:
		try:
			fechaF = datetime.strptime(fechaF, '%d/%m/%Y')
			q=0
		except:
			print("La fecha ingresa no es la correcta el formato debe ser (dd/mm/yyyy)")
			fechaF = input("ingrese fecha de nacimiento (dd/mm/yyyy): ")
			q=1
	anioF = fechaF.year
	mesF = fechaF.month
	diaF = fechaF.day

    #Fecha actual "Hoy"
	fechaH = datetime.today()
	anioH = fechaH.year
	mesH = fechaH.month
	diaH = fechaH.day
	mesAdicional = 0
	if (diaF > diaH):
		import calendar
		ultimodia = calendar.monthrange(anioF, mesF)[1]
		diaH = diaH + ultimodia
		mesAdicional = 1
		dias = diaH - diaF
		anioAdicional = 0
	if (mesF > mesH):
		mesH = mesH + 12
		anioAdicional = 1

	meses = mesH - (mesF + mesAdicional)
	anios = anioH - (anioF + anioAdicional)
	if userintroducido==mailuser_1:
		fecha_nacimiento_1=fechaF
		edad_1=(str(anios)+ " Años "+str(meses)+" Meses "+str(dias) +" Dias")
	elif userintroducido==mailuser_2:
		fecha_nacimiento_2=fechaF
		edad_2=(str(anios)+ " Años "+str(meses)+" Meses "+str(dias) +" Dias")
	elif userintroducido==mailuser_3:
		fecha_nacimiento_3=fechaF
		edad_3=(str(anios)+ " Años "+str(meses)+" Meses "+str(dias) +" Dias")
	os.system("cls")
	EDITAR_DATOS()

#AÑADIR BIOGRAFIA	
def BIOGRAFIA():
	global biografia, biografia_1, biografia_2, biografia_3
	print("Ingrese su biografia")
	biografia=input()
	print("Biografia modificada con exito")
	if userintroducido==mailuser_1:
		biografia_1=biografia
	elif userintroducido==mailuser_2:
		biografia_2=biografia
	elif userintroducido==mailuser_3:
		biografia_3=biografia
	os.system("cls")
	EDITAR_DATOS()

#AÑADIR HOBBIES
def HOBY():
	global h_1, h_2, h_3
	print("Ingrese su/s hobbies")
	if userintroducido==mailuser_1:
		h_1=input()
	elif userintroducido==mailuser_2:
		h_2=input()
	elif userintroducido==mailuser_3:
		h_3=input()
	os.system("cls")
	EDITAR_DATOS()
#MOSTRAR DATOS DEL USUARIO
def VER_DATOS():
	if userintroducido==mailuser_1:
		print("Nombre:",name_1,",",apellido_1,"\nBiografia:",biografia_1,"\nFecha de nacimiento:",fecha_nacimiento_1,"\nHobbies:",h_1,"\nEdad:",edad_1,"\nMail:",mailuser_1)
	elif userintroducido==mailuser_2:
		print("Nombre:",name_2,",",apellido_2,"\nBiografia:",biografia_2,"\nFecha de nacimiento:",fecha_nacimiento_2,"\nHobbies:",h_2,"\nEdad:",edad_2,"\nMail:",mailuser_2)
	elif userintroducido==mailuser_3:
		print("Nombre:",name_3,",",apellido_3,"\nBiografia:",biografia_3,"\nFecha de nacimiento:",fecha_nacimiento_3,"\nHobbies:",h_3,"\nEdad:",edad_3,"\nMail:",mailuser_3)

	EDITAR_DATOS()


#----------------------------------------------------------FUNCIONES OPCION 2----------------------------------------------------------------------------------------------


def VER_CANDIDATOS():
	if userintroducido==mailuser_1:
	print("-------------------------------------------------")
	print("Nombre:",name_2,",",apellido_2,"\nBiografia:",biografia_2,"\nFecha de nacimiento:",fecha_nacimiento_2,"\nHobbies:",h_2,"\nEdad:",edad_2,"\nMail:",mailuser_2)
	print("-------------------------------------------------")
	print("Nombre:",name_3,",",apellido_3,"\nBiografia:",biografia_3,"\nFecha de nacimiento:",fecha_nacimiento_3,"\nHobbies:",h_3,"\nEdad:",edad_3,"\nMail:",mailuser_3)
	ME_GUSTA()

def ME_GUSTA():
		global reportes
		me_gusta = input("Desea dar me gusta a algun usuario?")
		while me_gusta not in listan:
			print("USUARIO INTRODUCIDO NO EXISTENTE")
			me_gusta = input("¿Que usuario desea reportar?. Por favor, escriba el nombre de dicho usuario: ")
		os.system("cls")
		SEGUNDO_SUBMENU()
     
        
#-------------------------------------------------INICIO DE MENU------------------------------------------------
# x=int(1 o 0)===> variable que hace que continue la ejecucion del while de la funcion MENU. No hace falta ponerla en todos, lo puse por comodidad de comprension; para saber cuando se sigue ejecutando.
#MENU DE LA OPCION EDITAR DATOS PERSONALES
# opc=opcion elegida=>char
def EDITAR_DATOS():
	global opc
	print("----MENU OPCION a----")
	print("a)Añadir o editar la biografia\nb)Añadir o editar la fecha de nacimiento\nc)Añadir o editar hobbies\nd)Añadir o editar nombre\ne)Ver datos\nf)Volver")
	opc=input("Ingrese la letra de la opcion requerida:")
	while opc!="a" and opc!="b" and opc!="c" and opc!="d" and opc!="e" and opc!="f":
		print("-Valores incorrectos-")
		print("a)Añadir o editar la biografia\nb)Añadir o editar la fecha de nacimiento\nc)Añadir o editar hobbies\nd)Añadir o editar nombre\ne)Ver datos\nf)Volver")
		opc=input("Ingrese la letra de la opcion requerida:")

	if opc=="a":
		os.system("cls")
		BIOGRAFIA()
		

	elif opc=="b":
		os.system("cls")
		FECHA_NACIMIENTO()
		

	elif opc=="c":
		os.system("cls")
		HOBY()
		

	elif opc=="e":
		os.system("cls")
		VER_DATOS()
		print("\n")

	elif opc=="d":
		os.system("cls")
		NOMBRE()
		


	else:
		os.system("cls")
		PRIMER_SUBMENU()

#x es un valor entero que hace repetir o no al while del GENERAL
#f es la opcion elegida del PRIMER_MENU()
#c es la opcion elegida de los demas Sub_menues

#MENU PRINCIPAL
#f=>char (opcion elegida)
def PRIMER_MENU():
	global x, f
	print("-----MENU-----")
	print("1)Gestionar mi perfil\n2)Gestionar candidatos\n3)Matcheos\n4)Reportes estadisticos\n5)Salir")
	f=input("Ingrese el numero de la opcion requerida:")
	while (f!="1") and (f!="2") and (f!="3") and (f!="4") and (f!="5"):
		print("---DATOS ERRONEOS, INTENTE DE NUEVO---")
		print("1)Gestionar mi perfil\n2)Gestionar candidatos\n3)Matcheos\n4)Reportes estadisticos\n5)Salir")
		f=input("Ingrese el numero de la opcion requerida:")
	else:
		x=1

#MENU OPCION 1
def PRIMER_SUBMENU():
	global x
	print("----MENU OPCION 1----")
	print("a)Editar mis datos personales\nb)Eliminar perfil\nc)Volver")
	c=input("Ingrese la letra de la opcion requerida:")
	while c!="a" and c!="b" and c!="c":
		print("---DATOS ERRONEOS, INTENTE DE NUEVO---")
		print("a)Editar mis datos personales\nb)Eliminar perfil\nc)Volver")
		c=input("Ingrese la letra de la opcion requerida:")
	if c=="a":
		os.system("cls")
		EDITAR_DATOS()
	elif c=="b":
		os.system("cls")
		print("En construccion\n")
		PRIMER_SUBMENU()
		#LLamar funcion
	else:
		os.system("cls")
		x=1
		while x==1:
			PRIMER_MENU()
			ORDEN_DE_MENUS()


#MENU OPCION 2
def SEGUNDO_SUBMENU():
	global x
	print("----MENU OPCION 2----")
	print("a)Ver candidatos\nb)Reportar un candidato\nc)Volver")
	c=input("Ingrese la letra de la opcion requerida:")
	while c!="a" and c!="b" and c!="c":
		print("---DATOS ERRONEOS, INTENTE DE NUEVO---")
		print("a)Ver candidatos\nb)Reportar un candidato\nc)Volver")
		c=input("Ingrese la letra de la opcion requerida:")
	if c=="a":
		os.system("cls")
		VER_CANDIDATOS()
		
	elif c=="b":
		os.system("cls")
		print("En construccion...")
		SEGUNDO_SUBMENU()
		
	else:
		os.system("cls")
		x=1
		while x==1:
			PRIMER_MENU()
			ORDEN_DE_MENUS()


#ORDEN Y DECISION DE EJECUCION
def ORDEN_DE_MENUS():
	global x
	if f=="1":
		os.system("cls")
		PRIMER_SUBMENU()
		x=0
	elif f=="2":
		os.system("cls")
		SEGUNDO_SUBMENU()
		x=0
	elif f=="3":
		os.system("cls")
		print("En construccion\n")
		PRIMER_MENU()
	elif f=="4":
		os.system("cls")
		print("En construccion\n")
		PRIMER_MENU()
	elif f=="5":
		os.system("cls")
		print("Finalizado con exito")
		x=0

#MENU COMPLETO EN MODULO PARA FACIL ACCESO
def MENU():
	PRIMER_MENU()
	while x==1:
		ORDEN_DE_MENUS()

#--------------------------------------------FIN DE MENUS-------------------------------------------------------------------------------

#EJECUCION

INGRESO_VALIDACION()





			
input()
