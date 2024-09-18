from random import randint
import time
import keyboard

#     # Datos de usuarios pre-cargados
# #     # --gmail            --password --estado
esudiantes =[
    ["estudiante1","111", "estudiante1","soy el estudiante 1","Programar, leer","",""],
    ["estudiante2","222", "estudiante2","soy el estudiante 2","Pintar, viajar" ,"",""],
    ["estudiante3","333", "estudiante3","soy el estudiante 3","Bailar, cocinar","",""],
    ["estudiante4","444", "estudiante4","soy el estudiante 4","Jugar Videojuegos y leer","",""],
    ["estudiante5","555", "estudiante5","soy el estudiante 5","Estudiar matematicas","",""],
    ["estudiante6","666", "estudiante6","soy el estudiante 6","Aprender nuevos idiomas","",""],
    ["estudiante7","777", "estudiante7","soy el estudiante 7","Conocer nuevos lugares","",""],
    ["estudiante8","888", "estudiante8","soy el estudiante 8","Hacer amigos nuevos","",""],
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
tim2 = 0.0


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
                    
                    if even.name == "1":
                        print('mod2')
                        even = keyboard.read_event()
                        if even.event_type == keyboard.KEY_UP:
                            
                            if even.name == "1":
                                keyboard.press_and_release("backspace")
                                print('1')
                        
                        
                    if even.name == "2":
                        keyboard.press_and_release("backspace")
                        print('Eestudiantes todos')
                        for i in range(1,4):
                            for j in range(0,7):
                                keyboard.write(esudiantes[i][j], tim2)
                                # time.sleep(tim5)
                                keyboard.write("\n")
                        print('listo')

                    if even.name == "3":
                        keyboard.press_and_release("backspace")
                        print('Eestudiantes todos')
                        for i in range(0,4):
                            for j in range(0,7):
                                keyboard.write(esudiantes[i][j],tim2)
                                # time.sleep(0.)
                                keyboard.write("\n")
                        keyboard.write("moderador1@ayed.com\n111222\nno\n")
                                
                        print('listo')
                        
                    if even.name == "4":
                        keyboard.press_and_release("backspace")
                        print('Eestudiantes todos')
                        for i in range(0,4):
                            for j in range(0,7):
                                keyboard.write(esudiantes[i][j],tim2)
                                time.sleep(tim)
                                keyboard.write("\n")
                        
                        for i in range(0,3):
                            keyboard.write(moderadores[i][0]+"\n",tim2)
                            time.sleep(tim)
                            keyboard.write(moderadores[i][1]+"\n",tim2)
                            time.sleep(tim)
                            keyboard.write("si\n")
                        keyboard.write(moderadores[3][0]+"\n"+moderadores[3][1]+"\n",tim2)  
                        
                        time.sleep(0)
                        tim = 0
                        
                        for i in range(4,8):
                            keyboard.write("2\n")
                            keyboard.write(esudiantes[i][0], tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][1],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][1],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][2],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][3],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][4],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][5],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                            
                            keyboard.write(esudiantes[i][6],tim2)
                            time.sleep(tim)
                            keyboard.write("\n")
                
                    
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


        
