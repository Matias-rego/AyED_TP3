
from consola import *
from main import *
from registros import *
#---------------Bonus TP2-----------------#
def track_1():
    # var:
    # enteros: i
    # array: edades, edades2
    
    edades = [0]*6
    edades[0] = 21
    edades[1] = 18
    edades[2] = 20
    edades[3] = 19
    edades[4] = 23
    edades[5] = 24
    
    print("Las edades desordenadas son:")
    for i in range(0,6):
        print(edades[i], end=", ")

    ordenamiento(edades)
    
    print("\nLas edades ordenadas serian:")
    for i in range(0,6):
        print(edades[i], end=", ")
        
    for i in range(0,5):
        if edades[i + 1] != edades[i] + 1:
            print("\nLos huecos estan entre la posicion", i, "y la posicion", i+1, "y el numero faltante es", edades[i] + 1)
            
    getpass("\nOprima enter para volver al menu anterior\n", '')
    clear()
def track_2(estudiantes):
    # (estudiantes: M_8x8_str)
    # var:
    # enteros: c_est, matcheos, i  

    #c_est = 0
    #for i in range(0,8):
    #    if estudiantes[i][2] == "ACTIVO":
    #        c_est += 1
         
    #matcheos = c_est * c_est - c_est
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    pickle.load(l_estudiantes)
    x=l_estudiantes.tell()
    cant=t//x
    matcheos=(cant*(cant-1))//2
    if matcheos == 0:
        print("No hay match debido a que todos los usuarios estan inactivos.")
    
    else:
        print(f"Existen {matcheos} matcheos posibles")   
    
    getpass("Oprima enter para volver al menu anterior\n", '')
    clear()
def ordenamiento(x):
    # (x: M_6_int)
    # var:
    # enteros: i, j, aux 
    
    aux = 0
    for i in range(0,5):
        for j in range(i+1, 6):
            if x[i] > x[j]:
                aux = x[i]
                x[i] = x[j]
                x[j] = aux

#------------MENU BONUS-------------#
def bonus():
    # var: 
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0":
        clear()  
        opc = menu("Bonus track","",[
            "1. Bonus track 1 (TP2).",
            "2. Bonus track 2 (TP2).",
            "3. Bonus track 1 (TP3).",
            "","","","","","",""],
        AZUL)
         
        match opc:
            case "1": track_1()            
            case "2": track_2()            
            case "0": clear()
            case  _ : invalido()
            case "3": bonus1_muestra()




#---------------------BONUS TP3------------------------------#
#------------BONUS 1------------------#
def bonus1_puntuacion(ve:Estudiantes):
    ve2=Estudiantes()
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    puntaje=0
    cont=0
    while l_estudiantes.tell()<t:
        ve2=pickle.load(l_estudiantes)
        if is_like(ve,ve2)!=-1 and is_like(ve2,ve)!=-1:
            puntaje+=1
            cont+=1
        if is_like(ve,ve2)!=-1 and is_like(ve2,ve)==-1:
            puntaje-=1
            cont=0
        if cont>=3:
            puntaje+=1
    
    return puntaje
def bonus1_muestra():
    t=os.path.getsize(r_estudiantes)
    l_estudiantes.seek(0,0)
    pickle.load(l_estudiantes)
    x=l_estudiantes.tell()
    cant=t//x
    cartel("Bonus 1",AZUL)
    print("╠════╦═════════════════╦═══════")
    for i in range(cant):
        l_estudiantes.seek(i*x,0)
        ve=pickle.load(l_estudiantes)
        print("ID ",ve.id," Estudiante ",ve.name," tiene un puntaje de: ",bonus1_puntuacion(ve).ljust(4," "),"\n")

    print("Oprima cualquier tecla para volver al menu anterior\n")
    getch()            
