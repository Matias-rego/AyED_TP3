from consola import *

min = 0
max = 10
opc = ""
pos = 0
ch  = b''

opcs = [" << A << ","  Q. salir   ","     L. Quitar Like      "," R. reportar "," >> S >> "]
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

out2 = f"""
║{VACIO}{opcs[0]}{AZUL}║{VACIO}{opcs[1]}{AZUL}║{VACIO}{opcs[2]}{AZUL}║{VACIO}{opcs[3]}{AZUL}║{VACIO}{opcs[4]}{AZUL}║
╚═════════╩═════════════╩═════════════════════════╩═════════════╩═════════╝{VACIO}
"""
while opc != "r":
    clear()
    out2 = f"""
║{VACIO}{opcs[0]}{AZUL}║{VACIO}{opcs[1]}{AZUL}║{VACIO}{opcs[2]}{AZUL}║{VACIO}{opcs[3]}{AZUL}║{VACIO}{opcs[4]}{AZUL}║
╚═════════╩═════════════╩═════════════════════════╩═════════════╩═════════╝{VACIO}
"""

    print (out1 +out2)
    ch = getch().lower()
    
    match ch:
        case b'a': opcs[0]
        case b's': opcs[4]
        case b'q': opcs[1]
        case b'l': opcs[3]
        case b'r': opcs[4]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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