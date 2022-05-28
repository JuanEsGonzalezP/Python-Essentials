""" Considerando la siguiente tupla codifique un programa que permita separar 
los números pares e impares. Identifique también los posibles valores que
considere atípicos a ese arreglo. """

Datos_2021=[1, 2,3,4, 5, 6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
print(Datos_2021)    # Imprimimos los datos de la tupla

pares=[]                    # Se define lista para numeros pares
impares=[]                  # Se define lista para números impares
atipicos=[]                 # Se define list para numeros atípicos

for i in Datos_2021:                # Bucle Flor
    if i %2 == 0:                   # Condición para números pares
        pares.append(i)
    elif i %2 != 0:                 # Condición para números impares
        impares.append(i)
    else:                       
        atipicos.append(i)          # Condición para números atípicos
        
pares.sort()                        # Se ordena la lista par
impares.sort()                      # Se ordena lista impar
atipicos.sort()                     # Se ordena lista atípica    

print("Pares: ",pares)              # Se imprimen resultados
print("Impares: ",impares)
print("Atípicos: ",atipicos) 
