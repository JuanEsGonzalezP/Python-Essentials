"""
Desarrollar un programa que permita encontrar valores máximos y mínimos dentro de los valores de un diccionario, 
considerar lo siguiente para el código:
      * La parte modular de encontrar máximos y mínimos debe realizarse como una función.
      * La cantidad de valores máximos es variable y se debe obtener del usuario.
      * La cantidad de valores mínimos es variable y se debe obtener del usuario, y puede ser diferente de la 
           cantidad de máximos.
      * Se debe disponer de un menú con la siguiente salida:

        .- Elija una opción:
             1) Demostración del cálculo de máximos y mínimos en diccionarios.
             2) Salir.
    
      * Si no se elige una opción válida se debe mostrar un mensaje de error y el programa debe empezar nuevamente.
      * Si se elige la opción 1 se deben mostrar las siguientes opciones de diccionarios con la siguiente salida:
        .- Elija un diccionario para la demostración:
            
             1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}
             2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}
             3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}
             4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}
      
    * Si no se elige una opción válida se debe mostrar un mensaje de error y se debe pedir una opción válida.
    * Una vez elegido el diccionario se debe solicitar al usuario el ingreso de cuantos máximos y mínimos quiere mostrar:
                  
                  Digite el número de máximos que desea mostrar:
                  Digite el número de mínimos que desea mostrar:
                      
    * Se debe validar internamente si es posible trabajar con estos últimos valores, es decir si el número de valores 
      máximos y mínimos excede el tamaño del arreglo se debe mostrar un mensaje de error y debe pedir nuevamente estos valores.
    
    * Con los valores correctos deben mostrarse los valores máximos y mínimos en una lista y una tupla, con la siguiente salida:

                 Valores calculados en formato LISTA: […]
                 Valores calculados en formato TUPLA: […]
                 
    * Cuando se termine la ejecución del programa en la primera opción, éste debe seguirse ejecutando, es decir, debe permitir
      volver a usar las opciones hasta que el usuario use la opción salir.
"""
def mayorNumeroDiccionario(diccionario):
    maximo = max(diccionario.keys(), key=lambda k:diccionario[k])
    return diccionario[maximo]
def menorNumeroDiccionario(diccionario):
    maximo = min(diccionario.keys(), key=lambda k:diccionario[k])
    return diccionario[maximo]

diccionarioUno = {'Raul': 34, 'Paula': 19, 'Jorge': 43,'Richard': 10, 'Diana': 3, 'Isabel': 76, 'Gustavo': 12, 'Diego': 37}
diccionarioDos= {'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
diccionarioTres = {'val1':-12.5,'val2':12.5,'val3':83,'val4':2.1,'val5':23,'val6':100,'val7':13.4,'val8':92}
diccionarioCuatro = {'lst1':[4,6,-12,56,-9,5.7,33,100],'lst2':[9,0,81,-2,-56,],'lst3':[12,31,87,1,0,4,-11]}

   
menuprincipal=int(input("Elija una opción: \n 1- Demostración del cálculo de máximos y mínimos en diccionarios. \
                        \n 2- Salir.\n "))
while menuprincipal !=2:
    
    if menuprincipal==1:
        menu1=int(input(f"Elija un diccionario para la demostración: \n 1).{diccionarioUno} \n 2).{diccionarioDos} \n 3).{diccionarioTres} \n 4).{diccionarioCuatro} \n 5). Salir "))
        while menu1 !=5:
            if menu1 ==1:
                entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
                entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
                print(mayorNumeroDiccionario(diccionarioUno))
                print(menorNumeroDiccionario(diccionarioUno))
            elif menu1 == 2:
                entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
                entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
                enTuplaMax=mayorNumeroDiccionario(diccionarioDos)
                enTuplaMin=menorNumeroDiccionario(diccionarioDos)
                print(max(enTuplaMax))
                print(min(enTuplaMin))
            elif menu1 ==3:
                entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
                entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
                print(mayorNumeroDiccionario(diccionarioTres))
                print(menorNumeroDiccionario(diccionarioTres))
            elif menu1==4:
                entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
                entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
                enTuplaMax=mayorNumeroDiccionario(diccionarioCuatro)
                enTuplaMin=menorNumeroDiccionario(diccionarioCuatro)
                print(max(enTuplaMax))
                print(min(enTuplaMin))
                
            else:
                print("Error,por favor, escoga una opción correcta....")
                
            menu1=int(input(f"Elija un diccionario para la demostración: \n 1).{diccionarioUno} \n 2).{diccionarioDos} \n 3).{diccionarioTres} \n 4).{diccionarioCuatro} \n 5).Salir "))
                
    else:
        print("Error, escoga una opción correcta por favor")
    
    menuprincipal=int(input("Elija una opción: \n 1- Demostración del cálculo de máximos y mínimos en diccionarios. \
                            \n 2- Salir.\n "))






    
#print(mayorMenorDiccionario(diccionarioDos))


entrada = int(input("1) Demostración del cálculo de máximos y mínimos en diccionarios.\n2)Salir.\n"))
if entrada ==1:
    otraEntrada= int(input(f'opcion 1) {diccionarioUno}\nopcion 2) {diccionarioDos}\nopcion 3) {diccionarioTres}\nopcion 4) {diccionarioCuatro}\n'))
    if otraEntrada == 1:
        entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
        entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
        print(mayorNumeroDiccionario(diccionarioUno))
        print(menorNumeroDiccionario(diccionarioUno))
    elif otraEntrada == 2:
        entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
        entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
        enTuplaMax=mayorNumeroDiccionario(diccionarioDos)
        enTuplaMin=menorNumeroDiccionario(diccionarioDos)
        print(max(enTuplaMax))
        print(min(enTuplaMin))
    elif otraEntrada == 3:
        entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
        entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
        print(mayorNumeroDiccionario(diccionarioTres))
        print(menorNumeroDiccionario(diccionarioTres))
    elif otraEntrada == 4:
        entradaParaMin = input("Digite el número de máximos que desea mostrar: ")
        entradaParaMin = input("Digite el número de mínimos que desea mostrar: ")
        enTuplaMax=mayorNumeroDiccionario(diccionarioCuatro)
        enTuplaMin=menorNumeroDiccionario(diccionarioCuatro)
        print(max(enTuplaMax))
        print(min(enTuplaMin))
