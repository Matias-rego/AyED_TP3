from consola import *

"""
        ╔════════════════════════════════════╦════════════════════════════╦═══════╗
        ║   Nombre  :                        ║         Biografia:         ║ID:    ║
        ║   Email   :                        ║                                    ║
        ║   Pais    :                        ║                                    ║
        ║   Ciudad  :                        ║                                    ║
        ║   Sexo    :                        ║                                    ║
        ║   Edad    :                        ║                                    ║
        ║ Nacimiento:                        ║                                    ║
        ║ MateriaFav:                        ║                                    ║
        ╠═════════╦═════════════╦════════════╩════════════╦═════════════╦═════════╣
        ║ << A << ║  Q. salir   ║     L. Quitar Like      ║ R. reportar ║ >> S >> ║
        ╚═════════╩═════════════╩═════════════════════════╩═════════════╩═════════╝
        
        
"""
min = 0
max = 10
opc = ""
pos = 0
ch  = b''

# areglo donde guardo las opsiones predeterminadas
opco = [" << A << ","  Q. salir   ","     L. Quitar Like      "," R. reportar "," >> S >> "] 
# areglo donde guardo las opsiones que se van a mostrar 
opca = opco.copy()
# areglo donde guardo las opsiones validas que tiene el usuario
opcv = [ b'\r', b'a', b's', b'q', b'l', b'r'] 

# opsion anterior
preopc = ""
# plantilla bave
out1 = f"""
{AZUL}╔════════════════════════════════════╦════════════════════════════╦═══════╗
║{VACIO}   Nombre  :                        {AZUL}║{VACIO}         Biografia:         {AZUL}║{VACIO}ID:    {AZUL}║
║{VACIO}   Email   :                        {AZUL}║{VACIO}                                    {AZUL}║
║{VACIO}   Pais    :                        {AZUL}║{VACIO}                                    {AZUL}║
║{VACIO}   Ciudad  :                        {AZUL}║{VACIO}                                    {AZUL}║
║{VACIO}   Sexo    :                        {AZUL}║{VACIO}                                    {AZUL}║
║{VACIO}   Edad    :                        {AZUL}║{VACIO}                                    {AZUL}║
║{VACIO} Nacimiento:                        {AZUL}║{VACIO}                                    {AZUL}║
║{VACIO} MateriaFav:                        {AZUL}║{VACIO}                                    {AZUL}║
{AZUL}╠═════════╦═════════════╦════════════╩════════════╦═════════════╦═════════╣"""


while opc != "r":
    # preparo lo que voy a mostrar y lo dibujo enpantalla 
    out2 = f"""
║{VACIO}{opca[0]}{AZUL}║{VACIO}{opca[1]}{AZUL}║{VACIO}{opca[2]}{AZUL}║{VACIO}{opca[3]}{AZUL}║{VACIO}{opca[4]}{AZUL}║
╚═════════╩═════════════╩═════════════════════════╩═════════════╩═════════╝{VACIO}
"""

    print (out1 +out2)
    
    # defino las opsiones que tiene el usuario 
    
    
    # leo y verifico lo que ingresa el usuario
    ch = "" 
    while ch !=  opcv[0] and ch !=  opcv[1] and ch !=  opcv[2] and ch !=  opcv[3] and ch !=  opcv[4] and ch !=  opcv[5] :
        ch = getch().lower()
    clear()
    
    
    opca = opco.copy()
    # atuo dependiendo de lo que el usuari ingreso      
    if ch ==  b'\r':
        print("enten")

    elif ch ==  b'a':
        opca[0] = VERDE+opco[0]


    elif ch ==  b's':
        opca[4] = VERDE+opco[4]


    elif ch ==  b'q':
        opca[1] = VERDE+opco[1]


    elif ch ==  b'l':
        opca[2] = VERDE+opco[2]


    elif ch ==  b'r':
        opca[3] = VERDE+opco[3]


 
    
    
    
    # opcs = ["r"]*5
#     print("r. Para regresar al menu principal")
#     if min < pos:
#         print("a. Pagina anterior         ",end="")
#         opcs[0] = "a"
#     else:
#         print("                           ",end="")
    
#     # if estud.id != estudiante.id:
#     #     if likes[id][pos] == 0:
#     #         print("m. Dar Like         ",end="")
#     #     else:
#     #         print("m. Quitar Like      ",end="")
#     #     opcs[1] = "m"
        
# #     else:
# #         print("                    ",end="")
        
#     if pos < max:
#         print("s. Pagina siguiente")
#         opcs[2] = "s"
#     else:
#         print("                   ")
        
    
#     clear()
#     if opc == "r": clear()
#     elif opc == opcs[0] : pos -= t1
#     # elif opc == opcs[1] : 
#     #     if likes[id][poss[pos]] == 0:
#     #         likes[id][poss[pos]] = 1
#     #     else:
#     #         likes[id][poss[pos]] = 0
#     elif opc == opcs[2] : pos += t1
#     else: invalido()







    # opc = ""
    
    # while opc != "r":
    #     clear()
    #     l_estudiantes.seek(pos)
    #     estud = pickle.load(l_estudiantes)
    #     # id         - 4
    #     # email      - 32
    #     # name       - 32
    #     # materia_fav  13
    #     # bio        - 255
    #     # pais       - 32
    #     # ciudad     - 32
    #     # fecha      - 10
       
        
    #     opc = ""
    #     print(AZUL+"╔"+"═"*73+"╗")
    #     print("\033[1;34m|\033[0;mid                 : ",estud.id)
    #     print("\033[1;34m|\033[0;mEmail              : ",estud.email)
    #     print("\033[1;34m|\033[0;mNombre             : ",estud.name)
    #     print("\033[1;34m|\033[0;mFecha de nacimiento: ",estud.fecha)
    #     print("\033[1;34m|\033[0;mEdad               : ",calcular_edad(estud.fecha))
    #     print("\033[1;34m|\033[0;mBiografia          : ",estud.bio)
    #     print("\033[1;34m|\033[0;mPais               : ",estud.pais)
    #     print("\033[1;34m|\033[0;mSexo               : ",estud.sexo)
    #     print("\033[1;34m--------------------------------------\033[0;m")
        
    #     opcs = ["r"]*3
        
    #     if estud.id == estudiante.id:
    #         print("Estos son tus datos actuales")
            
    # #     me_gusta = ""    
    # #     for i in range(0,j+1):
    # #         if likes[id][poss[i]] == 1:
    # #             if me_gusta != "":
    # #                 me_gusta = me_gusta + ", " 
    # #             me_gusta = me_gusta + str(estudiantes[poss[i]][3])
                
    # #     if me_gusta != "":
    # #         print("Le diste like a: ", me_gusta)        
    # #     else:
    # #         print("Aun no le diste like a nadie ")
    
    
    #     print("r. Para regresar al menu principal")
    #     if min < pos:
    #         print("a. Pagina anterior         ",end="")
    #         opcs[0] = "a"
    #     else:
    #         print("                           ",end="")
        
    #     # if estud.id != estudiante.id:
    #     #     if likes[id][pos] == 0:
    #     #         print("m. Dar Like         ",end="")
    #     #     else:
    #     #         print("m. Quitar Like      ",end="")
    #     #     opcs[1] = "m"
            
    # #     else:
    # #         print("                    ",end="")
            
    #     if pos < max-t1:
    #         print("s. Pagina siguiente")
    #         opcs[2] = "s"
    #     else:
    #         print("                   ")
            
    #     opc = input(AZUL+">>> \033"+VACIO)
    #     clear()
    #     if opc == "r": clear()
    #     elif opc == opcs[0] : pos -= t1
    #     # elif opc == opcs[1] : 
    #     #     if likes[id][poss[pos]] == 0:
    #     #         likes[id][poss[pos]] = 1
    #     #     else:
    #     #         likes[id][poss[pos]] = 0
    #     elif opc == opcs[2] : pos += t1
    #     else: invalido()