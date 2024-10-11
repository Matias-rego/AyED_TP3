from random import randint
import time
from turtle import delay
import keyboard

#     # Datos de usuarios pre-cargados
# #     # --gmail            --password --estado
esudiantes =[
    ["estudiante1@ayed.com","000111", "estudiante1","soy el estudiante 1","Programar, leer","",""],
    ["estudiante2@ayed.com","111222", "estudiante2","soy el estudiante 2","Pintar, viajar" ,"",""],
    ["estudiante3@ayed.com","222333", "estudiante3","soy el estudiante 3","Bailar, cocinar","",""],
    ["estudiante4@ayed.com","333444", "estudiante4","soy el estudiante 4","Jugar Videojuegos y leer","",""],
    ["Adminpre@ayed.com","000000", "estudiante5","soy el estudiante 5","Estudiar matematicas","",""],
    ["Modpre@ayed.com","666", "estudiante6","soy el estudiante 6","Aprender nuevos idiomas","",""],
    ["estudiante7@ayed.com","777", "estudiante7","soy el estudiante 7","Conocer nuevos lugares","",""],
    ["estudiante8@ayed.com","888", "estudiante8","soy el estudiante 8","Hacer amigos nuevos","",""],
]


for i in esudiantes:
    if randint(0,1):
        i[5] = "m"
    else:
        i[5] = "f"
    i[6] = f"{randint(1990,2010)}/{randint(1,12)}/{randint(1,27)}"
    

moderadores = [
    ["moderador1","mod1"],
    ["moderador2","mod2"],
    ["moderador3","mod3"],
    ["moderador4","mod4"]
 ]


tim = 0
tim2 = 0


while True:
    even = keyboard.read_event()
    if even.event_type == keyboard.KEY_UP:
    
        # print(even.event_type)
        print(even.name)
        # print(even.to_json())

        if even.name == "bloq mayus":
            print('inicio')
            while True:
                even = keyboard.read_event()
                if even.event_type == keyboard.KEY_UP:

                    # if even.name == "bloq despl":
                    if even.name == "f5" or even.name == "bloq despl" :
                        time.sleep(2)
                        keyboard.write("1\n")
                        r= randint(4,4)
                        keyboard.write(esudiantes[r][0],tim2)
                        keyboard.write("\n")
                        keyboard.write(esudiantes[r][1],tim2)
                        keyboard.write("\n")
                        time.sleep(2)
                        keyboard.write("2\n")
                        keyboard.write("2\n")
                        
                    # if even.name == "4":
                    #     keyboard.press_and_release("backspace")
                    #     print('Eestudiantes todos')
                    #     for i in range(0,4):
                    #         for j in range(0,7):
                    #             keyboard.write(esudiantes[i][j],tim2)
                    #             time.sleep(tim)
                    #             keyboard.write("\n")
                        
                    #     for i in range(0,3):
                    #         keyboard.write(moderadores[i][0]+"\n",tim2)
                    #         time.sleep(tim)
                    #         keyboard.write(moderadores[i][1]+"\n",tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("si\n")
                    #     keyboard.write(moderadores[3][0]+"\n"+moderadores[3][1]+"\n",tim2)  
                        
                    #     time.sleep(0)
                    #     tim = 0
                        
                    #     for i in range(4,8):
                    #         keyboard.write("2\n")
                    #         keyboard.write(esudiantes[i][0], tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][1],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][1],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][2],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][3],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][4],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][5],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                            
                    #         keyboard.write(esudiantes[i][6],tim2)
                    #         time.sleep(tim)
                    #         keyboard.write("\n")
                
                    
                    if even.name == "5":
                        print('mod1')

                    if even.name == "6":
                        print('mod2')

                    if even.name == "7":
                        print('mo3')
                        
                    if even.name == "8":
                        print('mo4')
                        
                    if even.name == "9":
                        print('mo4')
                        
                    if even.name == "bloq mayus":
                        print('salir')
                        break
        
        # if even.name == "right ctrl":
        #     print('right ctrl')
        #     while True:
        #         even = keyboard.read_event()
        #         if even.event_type == keyboard.KEY_UP:
        #             print()
                    
        # if even.name == "mayusculas":
        #     print('mayusculas')
        #     while True:
        #         even = keyboard.read_event()
        #         if even.event_type == keyboard.KEY_UP:
        #             print()
                    
        # if even.name == "right shift":
        #     print('right shift')
        #     while True:
        #         even = keyboard.read_event()
        #         if even.event_type == keyboard.KEY_UP:
        #             print()
                    
        # if even.name == "":
        #     print('mod')
        #     while True:
        #         even = keyboard.read_event()
        #         if even.event_type == keyboard.KEY_UP:
        #             print()
                    
        if even.name == "esc":
            print('salir')
            break


        
