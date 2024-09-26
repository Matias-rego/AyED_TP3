
from consola import *

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
            print("\ny los huecos estan entre la posicion", i, "y la posicion", i+1, "y el numero faltante es", edades[i] + 1)
            
    getpass("\noprima enter para volver al menu anterior\n", '')
    clear()

def track_2(estudiantes):
    # (estudiantes: M_8x8_str)
    # var:
    # enteros: c_est, matcheos, i  

    c_est = 0
    for i in range(0,8):
        if estudiantes[i][2] == "ACTIVO":
            c_est += 1
         
    matcheos = c_est * c_est - c_est

    if matcheos == 0:
        print("No hay match debido a que todos los usuarios estan inactivos.")
    
    else:
        print(f"Existen {matcheos} matcheos posibles")   
    
    getpass("oprima enter para volver al menu anterior\n", '')
    clear()

def bonus(estudiantes):
    # (estudiantes: M_8x8_str)
    # var: 
    # String: opc
    opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir
    
    while opc!="0":
        print("\033[1;34m--------------------------------------")
        print("|\033[0;m        \033[1;37mBonus Tracks                \033[1;34m|")
        print("--------------------------------------\033[0;m\n")
        print("\033[1;37m1\033[0;m. Bonus Track 1")
        print("\033[1;37m2\033[0;m. Bonus Track 2")
        print("\033[1;37m0\033[0;m. Volver.")
        
        opc = input("\n\033[1;34m>>> \033[0;m")

        clear()  
        match opc:
            case "1": track_1()            
            case "2": track_2(estudiantes)            
            case "0": clear()
            case  _ : invalido()

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
            
