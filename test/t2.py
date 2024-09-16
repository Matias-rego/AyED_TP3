# import os
# from pynput import keyboard as kb


# def clear():
#     # funcion para limpiar la consola
#     # dependiendo del sistema operativo mandamos se usa el comando corespondiente 
    
#     if os.name == "nt":
#         os.system("cls")
#     else:
#         os.system("clear")
  
# def release_k(key):
#     # print("Soltada tecla " + str(key))
    
#     if key == kb.Key.ctrl_l:
#         print(kb.Key.ctrl_l)
    
#     if key == kb.Key.shift:
#         print(kb.Key.shift)
    
#     if key == kb.Key.shift_r:
#         print(kb.Key.shift_r)
    
#     if key == kb.Key.ctrl_r:
#         print(kb.Key.ctrl_r)
    
#     if key == kb.Key.right:
#         print(kb.Key.right)
    
#     if key == kb.KeyCode.from_dead("q"):
#         print("fin")
#         return False
    
# kb.Listener(on_release=release_k).run()

# from pynput import keyboard

# # The event listener will be running in this block
# with keyboard.Events.() as events:
#     for event in events:
#         if event.key == keyboard.Key.esc:
#             break
#         elif event.key == keyboard.Key.ctrl_l:
#             print("mod")
#             with keyboard.Events.Release() as events:
#                 for event in events:
#                     print(event)

#                     if event.key == keyboard.KeyCode.from_dead("1"):
#                         print("mod1")
                        
#                     elif event.key == keyboard.KeyCode.from_dead("2"):
#                         print("mod2")
                        
#                     elif event.key == keyboard.KeyCode.from_dead("3"):
#                         print("mod3")
                        
#                     elif event.key == keyboard.KeyCode.from_dead("4"):
#                         print("mo4")
                        
#                     elif event.key == keyboard.KeyCode.from_dead("5"):
#                         print("salir")
#                         break
#         # else:
#         #     print('Received event {}'.format(event))
            
