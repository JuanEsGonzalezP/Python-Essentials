print("Empezando a trabajar con Python")  #Saludo inicial

print(input("Realizado por: "))     # Aqui se ingresa el nombre

print("Consultando los tipos de valores") # Aqui se nombra la actividad a seguir

#Se definen las variables de las preguntas
a=875
b=4.89
c="Now is better than never"
d=1.32
e=5+8j
f=8.2
g=" Readability counts"

print(f"El tipo de dato de {a} es:")     #Primera pregunta
print(type(a))                          #Salida de la primera pregunta.

print(f"El tipo de dato de {b} es:")    #Segunda  pregunta
print(type(b))                          #Salida de la 2da pregunta, función anidada.

print(f"El tipo de dato del texto: {c}. es: ")  #Tercera  pregunta
print(type(c))                                  #Salida de la 3ra pregunta, función anidada.

print(f"El tipo de dato de {d} es")             #Cuarta  pregunta
print(type(d))                                  #Salida de la 4ra pregunta, función anidada.

print(f"¿El valor {e} corresponde a un valor entero?") #Quinta  pregunta
print(isinstance(e,int))                        # Salida de la 5ta pregunta, función anidada y de comparación.

print(f"¿El valor {f} corresponde a un valor entero?")  #Sexta  pregunta
print(isinstance(f,int))                    # Salida de la 6ta pregunta, función anidada y de comparación.

print(f"¿El texto:{g}. corresponde a un string?")       #Septima  pregunta
print(isinstance(g,str))            # Salida de la 7ma pregunta, función anidada y de comparación.