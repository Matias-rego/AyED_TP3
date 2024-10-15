import os #PARA BORRAR LA TERMINAL
import random #PARA LA ARRAY DE LOS LIKES ALEATORIOS
import getpass # PARA OCULTAR CONTRASEÑA
from datetime import datetime, date # PARA LA FECHA DE NACIMIENTO
import calendar #PARA LA FECHA DE NACIMIENTO
#-----INTEGRANTES-----#
#Tomas, Agusti
#Nicolás, Fossati
#Franchesco, Botta
#Marcos, Banducci
#---------------------#
adminuser = "admin@webmaster.com"
adminpassword = "12345abcde"
usuarios = [[""]*16 for n in range(8)] #Array bidimensional usuarios
moderadores = [[""]*4 for n in range(4)] #Array bidimensional moderadores
Gmails=[None]*12#Array unidimensional para Gmails
likes=[[0]*8 for n in range(8)]#Array bidimensional likes para  almacenar los valores de likes aleatorios.
reportes=[[""]*4 for n in range(8)]#Array bidimensional para almacenar los valores de reportes.
indice_usuarios = 0
indice_moderadores = 0
id_us = -1
id_mod=-1
mail_cont=-1
fecha_nacimiento = 0
cp = 0

# MENU DE LOGUEO 
def SELEC():
	print("------MENU LOGUEO------")
	print("1) Iniciar sesion \n2) Registrarse \n3) Salir")
	opcmen=int(input("Ingrese la opcion:"))
	while opcmen!= 1 and opcmen!=2 and opcmen!=3:
		os.system("cls")
		print("----Opcion no valida, intente de nuevo----")
		print("------MENU LOGUEO------")
		print("1) Iniciar sesion \n2) Registrarse \n3) Salir")
		opcmen=int(input("Ingrese la opcion:"))

	match opcmen:
		case 1:
			os.system("cls")
			INICIO_SESION(usuarios,moderadores)

		case 2:
			os.system("cls")
			REGISTRO(usuarios,moderadores)

		case 3:
			os.system("cls")
			print("Finalizado con exito")
			input("...")
		
#REGISTRO DE UN USUARIO
def REGISTRO(usuarios,moderadores):
	global indice_usuarios, indice_moderadores, id_mod, id_us, mail_cont
	print("----MENU REGISTRO----")
	print("1)Usuario\n2)Moderador\n3)Volver")
	opcreg=int(input("Ingrese la opcion:"))
	while opcreg!= 1 and opcreg!=2 and opcreg!=3:
		os.system("cls")
		print("----Opcion no valida, intente de nuevo----")
		print("----MENU REGISTRO----")
		print("1)Usuario\n2)Moderador\n3)Volver")
		opcreg=int(input("Ingrese la opcion:"))

	match opcreg:
		case 1:
			os.system("cls")
			id_us=id_us+1
			i=id_us
			usuarios[i][15]=id_us

			mail=input("Ingrese su mail:")
			for k in range (8):
				while (mail == usuarios[k][0]):
					print("Mail ya utilizado")
					mail=input("Ingrese su mail:")
			for n in range(4):
				while (mail == moderadores[n][0]):
					print("Mail ya utilizado")
					mail = input("Ingrese su mail:")

			else:
				mail_cont=mail_cont+1
				usuarios[i][0]=mail
				Gmails[mail_cont]=mail

			usuarios[i][1]=getpass.getpass(prompt='Ingrese su contraseña: ')
			os.system('cls')
			print("Se ha registrado correctamente, complete sus datos personales;")
			usuarios[i][2]=input("Nombre/s y apellido/s:")
			usuarios[i][3]=input("Genero (M/F):")
			while (usuarios[i][3] != "M") and (usuarios[i][3]!="F"):
				usuarios[i][3] = input("Error, valor no valido, Genero (M/F):")
			usuarios[i][4]=input("Hobbies:")
			usuarios[i][5]=input("Materia favorita:")
			usuarios[i][6]=input("Deporte favorito:")
			usuarios[i][7]=input("Materia fuerte:")
			usuarios[i][8]=input("Materia debil:")
			usuarios[i][9]=input("Biografia:")
			usuarios[i][10]=input("Nacionalidad:")
			usuarios[i][11]=input("Ciudad natal:")
			fecha_nacimiento = datetime.strptime(input("Fecha de nacimiento(Obligatorio)(YYYY/MM/DD): "),'%Y/%m/%d')
			hoy = date.today()
			edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
			usuarios[i][12] = fecha_nacimiento.strftime('%Y/%m/%d')
			usuarios[i][13] = str(edad)
			print ((f"({usuarios[i][13]} años.)"))
			indice_usuarios=indice_usuarios+1
			print("-----------------------------------------")
			i=id_us
			verif = input("Desea realizar algun cambio en los datos ya ingresados? \n \n 1=Si-----2=No-----:")
			usuarios[i][14]="ACTIVO"

			while (verif!="1") and (verif!="2"):
				verif = input("Error, valor fuera de rango, desea realizar algun cambio? \n 1=Si-----2=No-----:")
   			
			if verif=='1':
				VERIFICACION_DATOS(usuarios,i)
				print("Se ha registrado con exito.")
				SELEC()
			else:
				os.system('cls')
				print("Se ha registrado con exito.")
				SELEC()
			
		case 2:
			os.system("cls")
			id_mod = id_mod+1
			j=id_mod
			moderadores[j][2]=id_mod
			moderadores[j][3] = input("¿Como debemos llamarlo?...:")
			mail=input("Ingrese su mail:")
			
			for n in range (4):
				while (mail == moderadores[n][0]):
					print("Mail ya utilizado")
					mail=input("Ingrese su mail:")
			for k in range (8):
				while (mail == usuarios[k][0]):
					print("Mail ya utilizado")
					mail=input("Ingrese su mail:")
     
			else:
				mail_cont=mail_cont+1
				moderadores[j][0]=mail
				Gmails[mail_cont]=mail
	

			moderadores[j][1]=getpass.getpass(prompt='Ingrese su contraseña: ')
			indice_moderadores=indice_moderadores+1
			os.system('cls')
			print("Registro exitoso.")
			
		case 3:
			os.system("cls")
	SELEC()
#FUNCION PARA CAMBIAR DATOS INGRESADOS
def VERIFICACION_DATOS(usuarios,x):
				i=x
				os.system("cls")
				chang = input("Que valor desea modificar? \n 1:Nombre/s y apellido/s \n 2:Genero \n 3:Hobbies \n 4:Materia Favorita \n 5:Deporte Favorito \n 6:Materia Fuerte \n 7:Materia Debil \n 8:Biografia \n 9:Nacionalidad \n 10:Ciudad Natal \n 11:Fecha de Nacimiento \n")
				while chang !="1" and chang !="2" and chang !="3" and chang !="4" and chang !="5" and chang !="6" and chang !="7" and chang !="8" and chang !="9" and chang !="10" and chang !="11":
					chang = input("Error, que valor desea modificar? \n 1:Nombre/s y apellido/s \n 2:Genero \n 3:Hobbies \n 4:Materia Favorita \n 5:Deporte Favorito \n 6:Materia Fuerte \n 7:Materia Debil \n 8:Biografia \n 9:Nacionalidad \n 10:Ciudad Natal \n 11:Fecha de Nacimiento \n")
				
				match chang:
					case "1":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][2])
						usuarios[i][2]=input("Nombre/s y apellido/s: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "2":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][3])
						usuarios[i][3]=input("Genero (M/F): ")
						while (usuarios[i][3] != "M") and (usuarios[i][3]!="F"):
							usuarios[i][3] = input("Error, valor no valido, Genero (M/F): ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "3":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][4])
						usuarios[i][4]=input("Hobbies:")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "4":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][5])
						usuarios[i][5]=input("Materia favorita: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "5":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][6])
						usuarios[i][6]=input("Deporte favorito: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "6":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][7])
						usuarios[i][7]=input("Materia fuerte: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "7":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][8])
						usuarios[i][8]=input("Materia debil: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "8":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][9])
						usuarios[i][9]=input("Biografia: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "9":
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][10])
						usuarios[i][10]=input("Nacionalidad: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "10": 
						os.system('cls')
						print("Ingresado previamente:",usuarios[i][11])
						usuarios[i][11]=input("Ciudad natal: ")
						os.system('cls')
						print("Se ha modificado con éxito.")
					case "11":
						os.system('cls')
						print("Ingresado previamente: ",usuarios[i][12])
						print(f"(Edad: {usuarios[i][13]})")
						fecha_nacimiento = datetime.strptime(input("Fecha de nacimiento(Obligatorio)(YYYY/MM/DD): "),'%Y/%m/%d')
						hoy = date.today()
						edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
						usuarios[i][12] = fecha_nacimiento.strftime('%Y/%m/%d')
						usuarios[i][13] = str(edad)
						os.system('cls')
						print("Se ha modificado con éxito.")
# INICIO DE SESION		
def INICIO_SESION(usuarios,moderadores):
	global indice_usuarios, indice_moderadores, x, mail #X ES LA POSICION EN EL ARRAY DEL USUARIO ACTIVO
	if (indice_usuarios >= 4) and (indice_moderadores >= 1):
		intentos=3
		mail = input("Ingrese su mail:")
		contraseña = getpass.getpass(prompt='Ingrese su contraseña: ')
		x=-1
		while intentos>0 and x==-1:
			intentos=intentos-1

			for i in range(8):
				if (mail == usuarios[i][0]) and (contraseña == usuarios[i][1]):
					x=i
			for j in range(4):
				if (mail == moderadores[j][0]) and (contraseña==moderadores[j][1]):
					x=j
			if x==-1:
				os.system("cls")
				print("Contraseña o usuario incorrectos, le quedan ",intentos,"intentos.")
				mail = input("Ingrese su mail:")
				contraseña = getpass.getpass(prompt='Ingrese su contraseña: ')

		if intentos==0:
			os.system("cls")
			print("Intentos agotados;SISTEMA BLOQUEADO")
			SELEC()

		else:
			if contraseña == usuarios[x][1]:
				if mail == usuarios[x][0]:
					if usuarios[x][14]=="ACTIVO":
						os.system("cls")
						PRIMER_MENU(x, usuarios)
					else:
						os.system("cls")
						print("Usuario INACTIVO")
						SELEC()

			if contraseña == moderadores[x][1]:
				if mail == moderadores[x][0]:
					os.system("cls")
					MENU_MOD(x,moderadores)

	else:
		print("Error: minimo de 1 moderador y 4 estudiantes no cumplido. Registre los usuarios faltantes.")
		SELEC()
#--------------------------------------------------------------------------------------------------------------------------------------
#MENU PRINCIPAL USUARIOS
#f=>char (opcion elegida)
def PRIMER_MENU(x, usuarios):
	print("--------------------------------------")
	print(f"Bienvenido/a {usuarios[x][2]}")
	print("--------------------------------------")
	print("-----MENU-----")
	print("1)Gestionar mi perfil\n2)Gestionar candidatos\n3)Matcheos\n4)Reportes estadisticos\n5)Bonus Tracks\n6)Salir")
	f=input("Ingrese el numero de la opcion requerida:")
	while (f!="1") and (f!="2") and (f!="3") and (f!="4") and (f!="5") and f!="6":
		print("---DATOS ERRONEOS, INTENTE DE NUEVO---")
		print("1)Gestionar mi perfil\n2)Gestionar candidatos\n3)Matcheos\n4)Reportes estadisticos\n5)Salir")
		f=input("Ingrese el numero de la opcion requerida:")
	match f:
		case "1":
			os.system("cls")
			PRIMER_SUBMENU(x)
		case "2":
			os.system("cls")
			SEGUNDO_SUBMENU(x)
		case "3":
			os.system("cls")
			print("En construccion")
			PRIMER_MENU(x, usuarios)
		case "4":
			os.system("cls")
			REPORTES_ESTADISTICOS(x,likes)
			PRIMER_MENU(x, usuarios)
		case "5":
			os.system("cls")
			BONUSTRACKS(edades)
			PRIMER_MENU(x, usuarios)
		case "6":
			os.system("cls")
			print("Finalizado con exito")
			x=0
			SELEC()

#MENU OPCION 1
def PRIMER_SUBMENU(x):
	print("----MENU OPCION 1----")
	print("a)Editar mis datos personales\nb)Eliminar perfil\nc)Ver datos\nd)Volver")
	c=input("Ingrese la letra de la opcion requerida:")
	while c!="a" and c!="b" and c!="c" and c!="d":
		os.system("cls")
		print("---DATOS ERRONEOS, INTENTE DE NUEVO---")
		print("a)Editar mis datos personales\nb)Eliminar perfil\nc)Volver")
		c=input("Ingrese la letra de la opcion requerida:")
	match c:

		case "a":
			os.system("cls")
			VERIFICACION_DATOS(usuarios,x)
			PRIMER_SUBMENU(x)
		case "b":
			os.system("cls")
			ELIMINAR(usuarios,x)
		case "c":
			os.system("cls")
			VER_DATOS(usuarios,x)
		case "d":
			os.system("cls")
			PRIMER_MENU(x, usuarios)

#MENU OPCION 2
def SEGUNDO_SUBMENU(x):
	print("----MENU OPCION 2----")
	print("a)Ver candidatos\nb)Reportar un candidato\nc)Volver")
	c=input("Ingrese la letra de la opcion requerida:")
	while c!="a" and c!="b" and c!="c":
		os.system("cls")
		print("---DATOS ERRONEOS, INTENTE DE NUEVO---")
		print("a)Ver candidatos\nb)Reportar un candidato\nc)Volver")
		c=input("Ingrese la letra de la opcion requerida:")
	match c:

		case "a":
			os.system("cls")
			VER_CANDIDATOS(x,likes)
		case "b":
			os.system("cls")
			REPORTES(usuarios,x)
		case "c":
			os.system("cls")
			PRIMER_MENU(x, usuarios)
#REPORTES ESTADISTICOS
def REPORTES_ESTADISTICOS(x,likes):
	os.system("cls")
	print("-----MENU REPORTES ESTADISTICOS-----")
	print("Te has dado likes mutuamente con el ",LIKES_MATCHEADOS(x,likes),"porciento de los usuarios. ")
	print("Likes dados y no recibidos:",LIKES_DADOS(x,likes))
	print("Likes recibidos y no respondidos:",LIKES_NO_RESPONDIDOS(x,likes))
	input()
	os.system("cls")
#MENU BONUS TRACKS
def BONUSTRACKS(edades):
	os.system("cls")
	print("-------MENU DE BONUS TRACK-------")
	print("1)Bonus track I;edades\n2)Bonus track II;cantidad de matcheos posibles\n3)volver")
	opcb=input("Ingrese la opcion requerida:")
	while opcb !="1" and opcb !="2" and opcb != "3":
		os.system("cls")
		print("Valores invalidos")
		print("-------MENU DE BONUS TRACK-------")
		print("1)Bonus track I;edades\n2)Bonus track II;cantidad de matcheos posibles\n3)Volver")
		opcb=input("Ingrese la opcion requerida:")
	match opcb:
		case "1":
			os.system("cls")
			print("La cantidad de huecos encontrados es:",ORDENAR(edades))
			print("Array ordenada")
			for i in range(6):
				print(edades[i])
			input()
			BONUSTRACKS(edades)
		case "2":
			os.system("cls")
			print("La cantidad de matcheos posibles es de:",CANT_MATCHEOS_POSIBLES(indice_usuarios))
			input()
			BONUSTRACKS(edades)
		case "3":
			os.system("cls")

#--------------------------------------------------------------------------------------------------------------------------------------
#menu moderadores
def MENU_MOD(x,moderadores):
	print("--------------------------------------")
	print(f"Bienvenido/a {moderadores[x][3]}")
	print("--------------------------------------")
	print("----MENU MODERADORES----")
	print("1)Gestionar usuarios\n2)Gestionar reportes\n3)Reportes estadisticos\n4)Bonus Tracks\n5)Salir")
	opc=input("Ingrese el numero de la opcion requerida:")
	while opc!="1" and opc!="2" and opc!="3" and opc!="4" and opc=="5":
		os.system("cls")
		print("-Valores incorrectos-")
		print("1)Gestionar usuarios\n2)Gestionar reportes\n3)Reportes estadisticos\n4)Salir")
		opc=input("Ingrese el numero de la opcion requerida:")
	match opc:
		case "1":
			os.system("cls")
			GESTIONAR_USUARIOS(x)
		case "2":
			os.system("cls")
			GESTIONAR_REPORTES(reportes, x, usuarios)

		case "3":
			os.system("cls")
			REPORTES_ESTADISTICOS(x,likes)
			MENU_MOD(x,moderadores)
		case "4":
			os.system("cls")
			BONUSTRACKS(edades)
			MENU_MOD(x,moderadores)
		case "5":
			os.system("cls")
			print("Finalizado con exito")
			SELEC()
#menu moderadores opcion 1
def GESTIONAR_USUARIOS(x):
	print("----MENU GESTIONAR USUARIOS----")
	print("1)Desactivar usuario\n2)Volver")
	opcb=input("Ingrese el numero de la opcion requerida:")
	while opcb!="1" and opcb!="2":
		os.system("cls")
		print("-Valores incorrectos-")
		print("----MENU GESTIONAR USUARIOS----")
		print("1)Desactivar usuario\n2)Volver")
		opcb=input("Ingrese el numero de la opcion requerida:")
	match opcb:
		case "1":
			os.system("cls")
			DESACTIVAR(usuarios,x)
		case "2":
			os.system("cls")
			MENU_MOD(x,moderadores)
#menu moderadores opcion 2
def GESTIONAR_REPORTES(reportes,x,usuarios):
	global cp
	print("----MENU GESTIONAR REPORTES----")
	print("1)Ver reportes\n2)Volver")
	opcb=input("Ingrese el numero de la opcion requerida:")
	while opcb!="1" and opcb!="2":
		os.system("cls")
		print("-Valores incorrectos-")
		print("----MENU GESTIONAR REPORTES----")
		print("1)Ver reportes\n2)Volver")
		opcb=input("Ingrese el numero de la opcion requerida:")
	match opcb:
		case "1":
			os.system("cls")
			if cp>0:                                                             #Ya que deben haber reportes para poder revisarlos
					print(f"Debe revisar {cp} reporte/s.")
					for h in range(indice_usuarios):
						if (reportes[h][0] == "0"):
							print(f"Se ha reportado al usuario nro: {reportes[pos_us_rep][1]}, por el usuario ID,nro: {reportes[pos_us_rep][3]} ")
							print(f"La razon por la que decidio reportar fue: {reportes[pos_us_rep][2]}")
							opcrep = input("¿Desea revisar este reporte ahora? \n<1> Si, <2> No \n Ingrese su opcion:")
							while opcrep != "1" and opcrep!="2":
								os.system('cls')
								opcrep = input("Error, valor fuera de rango.\n¿Desea revisar este reporte ahora? \n<1> Si, <2> No\nIngrese su opcion: ")
							if opcrep=="1":
								os.system('cls')
								accrep = input("¿Que accion desea realizar? \n1.Ignorar reporte\n2.Bloquear/desactivar al reportado\nIngrese su opcion:")
								while accrep != "1" and accrep!= "2" :
									os.system('cls')
									accrep= input("Error, valor fuera de rango\n ¿Que accion desea realizar? \n1.Ignorar reporte\n2.Bloquear/desactivar al reportado\nIngrese su opcion:")
								
								if accrep == "1":
									os.system('cls')
									reportes[pos_us_rep][0] = "2"                             #Actualizar el estado del reporte a 2, lo que indica que el reporte fue ignorado por el moderador
									cp= cp-1
									print("Reporte ignorado con exito.")
									print("-----------------------------")
									MENU_MOD(x,moderadores)

								else:
									os.system('cls')
									reportes[pos_us_rep][0] = "1"                             #Actualizar el estado del reporte a 1, lo que indica que se bloqueo el usuario
									usuarios[pos_us_rep][14] = "INACTIVO"
									cp= cp-1
									print("Usuario desactivado con exito.")
									print("-----------------------------")
									MENU_MOD(x,moderadores)

			else:
				os.system('cls')
				print("No hay reportes por revisar.")
				MENU_MOD(x,moderadores)

		case "2":
			os.system("cls")
			MENU_MOD(x, moderadores)
#------------------------------------------------------------------------------------------------------------------------------------------------------------#

#CARGA DE LIKES ALEATORIOS EN UNA ARRAY BIDIMENSIONAL
def LIKES_RANDOM(likes):
    
	for i in range(indice_usuarios):
		for j in range(indice_usuarios):
			likes[i][j]=random.randint(0,1)
		likes[i][i]=0
#DEFINICION DE ESTADO DE USUARIO
def ESTADO(usuarios):
	for i in range(8):
		usuarios[i][14]="INACTIVO"
#FUNCIONES PARA LOS DISTINTOS MENUS
def ELIMINAR(usuarios,x):
	os.system("cls")
	print("Estas seguro de que quieres eliminar tu perfil?,\nTus datos se eliminaran permanentemente.")
	eliminar=input("INGRESE <1> PARA ELIMINAR O <2> PARA CANCELAR:")
	while eliminar!="1" and eliminar!="2":
		os.system("cls")
		print("-Valores incorrectos-")
		print("Estas seguro de que quieres eliminar tu perfil?,\nTus datos se eliminaran permanentemente.")
		eliminar=input("INGRESE <1> PARA ELIMINAR O <2> PARA CANCELAR:")
	match eliminar:
		case "1":
			os.system("cls")
			usuarios[x][14]="INACTIVO"
		case "2":
			os.system("cls")
			PRIMER_SUBMENU(x)

def VER_DATOS(usuarios,x):
	os.system("cls")
	print("Nombre/s y apellido/s:", usuarios[x][2])
	print("Género(M/F):", usuarios [x][3])
	print("Hobbies:", usuarios[x][4])
	print("Materia Favorita:", usuarios[x][5])
	print("Deporte Favorito:", usuarios[x][6])
	print("Materia Fuerte:", usuarios[x][7])
	print("Materia Debil:", usuarios[x][8])
	print("Biografia:", usuarios[x][9])
	print("Nacionalidad:", usuarios[x][10])
	print("Ciudad Natal:", usuarios[x][11])
	print("Fecha de Nacimiento:", usuarios[x][12])
	print("Edad:", usuarios[x][13])
	input("")
	os.system("cls")
	PRIMER_SUBMENU(x)

def VER_CANDIDATOS(x,likes):
	os.system("cls")
	for k in range(indice_usuarios):
		print("-------------------------------------------------------")
		print("ID del usuario:",usuarios[k][15])
		print(f"1:Nombre/s y apellido/s:{usuarios[k][2]}  \n 2:Genero:{usuarios[k][3]} \n 3:Hobbies:{usuarios[k][4]} \n 4:Materia Favorita:{usuarios[k][5]} \n 5:Deporte Favorito:{usuarios[k][6]} \n 6:Materia Fuerte:{usuarios[k][7]} \n 7:Materia Debil:{usuarios[k][8]} \n 8:Biografia:{usuarios[k][9]} \n 9:Nacionalidad:{usuarios[k][10]} \n 10:Ciudad Natal:{usuarios[k][11]} \n 11:Fecha de Nacimiento:{usuarios[k][12]}. ({usuarios[k][13]} años)")
		print("-------------------------------------------------------")
	me_gusta_R = input("¿Desea dar me gusta a algun Usuario? \n <1>: Si, <2>: No \n Ingrese una opcion: ")
	while me_gusta_R != "1" and me_gusta_R != "2":
		me_gusta_R = input("¿Desea dar me gusta a algun Usuario? \n <1>: Si, <2>: No \n Ingrese una opcion: ")
	match me_gusta_R:
		case "1":
			me_gusta=input("Ingrese el ID del usuario:")
			while me_gusta<"0" and me_gusta>"7":
				print("ID fuera de rango")
				me_gusta=input("Ingrese el ID del usuario:")
			
			likes[x][x]=0
			likes[x][int(me_gusta)]=1

			os.system("cls")
			SEGUNDO_SUBMENU(x)

		case "2":
			os.system("cls")
			SEGUNDO_SUBMENU(x)

def DESACTIVAR(usuarios,x):
	os.system("cls")
	for k in range(indice_usuarios):
		print("-------------------------------------------------------")
		print("ID del usuario:",usuarios[k][15])
		print(f"1:Nombre/s y apellido/s:{usuarios[k][2]}  \n 2:Genero:{usuarios[k][3]} \n 3:Hobbies:{usuarios[k][4]} \n 4:Materia Favorita:{usuarios[k][5]} \n 5:Deporte Favorito:{usuarios[k][6]} \n 6:Materia Fuerte:{usuarios[k][7]} \n 7:Materia Debil:{usuarios[k][8]} \n 8:Biografia:{usuarios[k][9]} \n 9:Nacionalidad:{usuarios[k][10]} \n 10:Ciudad Natal:{usuarios[k][11]} \n 11:Fecha de Nacimiento:{usuarios[k][12]}. ({usuarios[k][13]} años)")
		print("-------------------------------------------------------")
	print("--------------------------------------")
	des=int(input("Ingrese el numero de usuario a desactivar:"))
	
	while des >7 and des <0:
		print("Opcion no valida")
		des=int(input("Ingrese el numero de usuario a desactivar:"))
		
	print("Estas seguro de querer desactivar este usuario?\n1)Si\n2)No")
	seguro=input("Opcion:")
	while seguro!="1" and seguro !="2":
		os.system("cls")
		print("Opcion no valida")
		print("Estas seguro de querer desactivar este usuario?\n1)Si\n2)No")
		seguro=input("Opcion:")
	match seguro:
		case "1":
			usuarios[des][14]="INACTIVO"
			os.system("cls")
			GESTIONAR_USUARIOS(x)
		case "2":
			os.system("cls")
			GESTIONAR_USUARIOS(x)

def REPORTES(usuarios,x):
		global pos_us_rep, cp
		for m in range(indice_usuarios):
			print(f"{m+1}:Nombre/s y apellido/s:{usuarios[m][2]}")
		report_us = input("¿Que usuario desea reportar? \n Ingrese el nombre de dicho usuario: ")
		while report_us == usuarios[x][2]:                                                                                                 #Para no poder autoreportarse
			print("-------------------------------------------")
			report_us = input("Error, no podes reportarte solo.\n Ingrese el nombre de dicho usuario:")
			print("-------------------------------------------")		
		for k in range(indice_usuarios):
			if report_us == usuarios[k][2]:
				pos_us_rep = k                                                                                                             #Para guardar la posicion de dicho usuario
				if reportes[pos_us_rep][0] !="0" or  reportes[pos_us_rep][0] !="1" or reportes[pos_us_rep][0] !="2":
					if (usuarios[pos_us_rep][14]=="ACTIVO"): 
						os.system('cls')                                                                           #Para verificar que el estado del usuario no es inactivo
						valid = input(f"Seguro que desea reportar a:  {usuarios[pos_us_rep][2]} \n <1> Si, <2> No \n Ingrese una opcion: ")
						while valid !="1" and valid!="2":
							os.system('cls')
							valid = input(f"Error, valor fuera de rango. Seguro que desea reportar a:  {usuarios[pos_us_rep][2]} \n <1> Si, <2> No \n Ingrese una opcion: ")
						match valid:
							case "1":
								reportes[pos_us_rep][1] = usuarios[pos_us_rep][15]
								os.system('cls')
								reportes[pos_us_rep][2] = input("Escriba su motivo(OBLIGATORIO): ")
								while (reportes[pos_us_rep][2] == ""):
									os.system('cls')
									print("¡Debes escribir un motivo valido!")
									reportes[pos_us_rep][2] = input("Escriba su motivo(OBLIGATORIO): ")
								reportes[pos_us_rep][0] = "0"
								cp+=1
								reportes[pos_us_rep][3] = usuarios[x][15]
								os.system('cls')
								print("¡Reporte realizado con exito!, ¡Muchas gracias!")
								SEGUNDO_SUBMENU(x)

							case "2":
								os.system('cls')
								SEGUNDO_SUBMENU(x)

					else:
						os.system('cls')
						print("Error, no se puede reportar un usuario inactivo. ")
						report_us = input("¿Que usuario desea reportar? \n Ingrese el nombre de dicho usuario: ")
				else:
					os.system('cls')
					print("Ese usuario ya ha sido reportado previamente, por lo que esta esperando ser revisado por un moderador.")
					print("-----------------------------------------")
					SEGUNDO_SUBMENU(x)
#Funciones de reportes estadisticos

def LIKES_NO_RESPONDIDOS(x,likes):
	t=0
	for i in range(8):
		if likes[i][x]==1:
			if likes[x][i]==0:
				t=t+1
	return t

def LIKES_DADOS(x,likes):
	t=0
	for i in range(8):
		if likes[x][i]==1:
			if likes[i][x]==0:
				t=t+1
	return t

def LIKES_MATCHEADOS(x,likes):
	t=0
	for i in range(8):
		if likes[i][x]==1:
			if likes[x][i]==1:
				t=t+1
	porcen=(t*100)//indice_usuarios
	return porcen


#---------------------------------------------------------BONUS TRACK I---------------------------------------------------------------------#
edades = [21, 18, 20, 19, 23, 24] 

def ORDENAR(edades):
	#--------ordenamiento--------#
	for j in range(3):
		for i in range(5):
			if edades[i]>edades[i+1]:
				aux=edades[i]
				edades[i]=edades[i+1]
				edades[i+1]=aux
	#-------deteccion--huecos----------#		
	huecos=0	
	for i in range(5):
		if (edades[i+1]-edades[i])>1:
			huecos=huecos+1
	return huecos


#---------------------------------------------------------BONUS TRACK II--------------------------------------------------------------------#

# indice_usuarios===>contador de usuarios registrados;variable global
def CANT_MATCHEOS_POSIBLES(indice_usuarios):
	r=(indice_usuarios*(indice_usuarios-1))//2
	return r


#----------------------------------------------------------------------------------------------------------------------------------------------#
#PROGRAMA PRINCIPAL
ESTADO(usuarios)
LIKES_RANDOM(likes)
SELEC()

