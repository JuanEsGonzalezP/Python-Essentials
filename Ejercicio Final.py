"""
Ejercicio de módulos y menús de elección.
En este apartado se mostrará los ejercicio de tarea del curso 
Python Essencials mayo 2022
"""
# Se importan los módulos de los ejercicios
 # Una vezcargada los módulos con los que se piensa trabajar, ideamos
 # el menú interactivo

# Eligir opciones en el menú 

  
menu=int(input("Elija una opción: \n 1.- Ejemplo 1. \n 2.- Ejemplo 2. \n 3.- Ejemplo 3. \
                        \n 4.- Ejemplo 4. \n 5.- Ejemplo 5 \n 6.- Salir.\n "))
while menu !=6:
    
    if menu==1:
       import Ejercicio1_Parte1
       print(Ejercicio1_Parte1)
       
    elif menu==2:
        import Ejercicio1_Parte2
        print(Ejercicio1_Parte2)
    
    elif menu==3:
        import Ejercicio2_Parte1
        print(Ejercicio2_Parte1)
    
    elif menu==4:
        import Ejercicio2_Parte2
        print(Ejercicio2_Parte2)
    
    elif menu==5:       
        import Ejercicio3_Parte1        
        print(Ejercicio3_Parte1)
                           
    else:
        print("Error, escoga una opción correcta por favor")
    
    menu=int(input("Elija una opción: \n 1.- Ejemplo 1. \n 2.- Ejemplo 2. \n 3.- Ejemplo 3. \
                            \n 4.- Ejemplo 4. \n 5.- Ejemplo 5. \n 6.- Salir.\n "))
