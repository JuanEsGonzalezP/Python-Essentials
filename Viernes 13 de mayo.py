
nombre="Sandra"
apellido="González"
edad=14
estatura=1.50

str1="Saludos, mi nombre es Juan, mi apellido es Sánchez, \
     tengo 33 años y mi estatura es de 1.75 metros"

print(str1)

print("Saludos, mi nombre es",nombre,"mi apellido es ",apellido,"tengo ",edad,"años y mi estatura es de ",estatura," metros")
 
print("Saludos, mi nombre es",
       nombre,"mi apellido es ",
       apellido,"tengo ",
       edad,"años y mi estatura es de ",
       estatura,
       "metros")

str2="Saludos, mi nombre es "+nombre+"mi apellido es "+apellido+"tengo "+str(edad)+"años y mi estatura es de "+str(estatura)+" metros"
print("Saludos, mi nombre es "+nombre+"mi apellido es "+str(apellido)+"tengo "+str(edad)+" años y mi estatura es de "+str(estatura)+" metros")


#Operadores de formato, la de operador porcentual %s es la más general para Python

# str5="Saludos, mi nombre es %s, mi apellido es %s, tengo %s años y mi estatura es de %s" % (nombre,nombre,nombre, nombre)"

print("Saludos, mi nombre es %s, mi apellido es %s, tengo %s años y mi estatura es de %s metros")

srt3="Saludos, mi nombre es %s, mi apellido es %s, tengo %s años y mi estatura es de %s metros." %(nombre,apellido,edad, estatura)

#(nombre,apellido,edad, estatura))

str3="Saludos, mi nombre es {0} {1} {2} {3}".format(784, apellido, edad,estatura)
print(str3)

str3="Saludos, mi nombre es {var1} {var2} {var3} {var4}".format(var1="Diego", var2="Zurita", var3=25, var4=1.47)

str3="Saludos, mi nombre es {var1} {var2} {var3} {var4}".format(var1="Diego", var2=input(), var3=25, var4=1.47)
print(str3)

#                           Metodos de CADENA DE TIPO F

str3=f"Saludos, mi nombre es {nombre}, mi apellido es {apellido}, tengo {edad} años y mi estatura es de {estatura} metros"
print(str3)

str3=f"Saludos, mi nombre es {nombre}, mi apellido es {apellido.upper()}, tengo {edad} años y mi estatura es de {estatura} metros"
print(str3)

str3=f"Saludos, mi nombre es {nombre+str(edad)}, mi apellido es {apellido.upper()}, tengo {edad} años y mi estatura es de {estatura} metros"
print(str3)

#    Cadena tipo Roww, todo lo que esta denttor de las comillas

str3=r"Saludos, mi nombre es {nombre+str(edad)}, mi apellido es {apellido.upper()}, tengo {edad} años y mi estatura es de {estatura} metros"
print(str3)


####################### Creacion del programa o primer ejercicio //////////////////////////////////////////////

# se necesita una aplicación que pregunta, nombre, apellido, edad y estatura
# en salto de línea mostrar nombre, en la segunda su apellido, en la tercera su edad y en la cuarta su estatura
# como requisito todos los nombres deben ir con mayus sea como sea

str1=input("Ingrese su nombre: ")
str2=input("Ingrese su apellido: ")
str3=input("Ingrese su edad: ")
str4=input("Ingrese su estatura: ")

saludo1=f"Hola, mi nombre es {str1.capitalize()}"
saludo2=f"Mi apellido es: {str2.capitalize()}"
saludo3=f"Mi edad es {str3}"
saludo4=f"Mi estatura es {str4}"

print(saludo1)
print(saludo2)
print(saludo3)
print(saludo4)

print(str1," ", str2, str3, str4)


#        ////// 2 da parte ////

# se necesita una aplicacion que pregunta, nombre, apeliido, edad y estautra
# en salto de linea mostrar nombre, en la segunda su apeliido, en la tercera su edad y en la cuarta su estatura
# como requisito todos los nombres deben ir con mayus sea como sea

str1=input("Ingrese su nombre: ")
str2=input("Ingrese su apellido: ")
str3=input("Ingrese su edad: ")
str4=input("Ingrese su estatura: ")

saludo1=f"Hola, mi nombre es {str1.capitalize()}"
saludo2=f"Mi apellido es: {str2.capitalize()}"
saludo3=f"Mi edad es {str3}"
saludo4=f"Mi estatura es {str4}"

print(saludo1)
print(saludo2)
print(saludo3)
print(saludo4)

print(str1," ", str2, str3, str4)

### 8 variables en una sola linea

print(f"Hola mi nombre es: {str1.capitalize()}\n",
       f"Mi apellido es: {str2.capitalize()}\n",
       f"Mi edad es: {str3.capitalize()}\n",
       f"Mi estatura es :{str4.capitalize()}")


print(str1," ", str2, str3, str4)


print(f"Hola mi nombre es: {str1.capitalize()},\nMi apellido es: {str2.capitalize()},\nMi edad es: {str3.capitalize()},\nMi estatura es :{str4.capitalize()}")


print(str1," ", str2, str3, str4)


#puedo hacerlo en una solo variables

#   //////////////asignacion umultiple de variables multiples

str1,str2,str3,str4=str1=input("Ingrese su nombre: "),input("Ingrese su apellido: "),input("Ingrese su edad: "),input("Ingrese su estatura: ")
print(f"Hola mi nombre es: {str1.capitalize()},\nMi apellido es: {str2.capitalize()},\nMi edad es: {str3.capitalize()},\nMi estatura es :{str4.capitalize()}")


# estructuras de control de flujo condicional → en condiciones logicas, sirven para separar partes de código

num1,num2=23,-10

if num1<num2:
    print("Esto está dentro del If")
    print(f"Suma de los números {num1} y {num2}:{num1+num2}")

print("Este código esta fuera de la estructura")

num1,num2=23,150

if num1<num2:
    print("Esto está dentro del If")
    print(f"Suma de los números {num1} y {num2}:{num1+num2}")

print("Este código esta fuera de la estructura")


num1,num2=23,-10

if num1<num2:
    print("Esto está dentro del If")
    print(f"Suma de los números {num1} y {num2}:{num1+num2}")
else:
    print("Este código esta dentro del ELSE")

#  //////////////////////////////////// ///////
edad1=int(input("Ingrese su edad: "))
if edad1 >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# --------------- cuando hay letra en ves de numeros ------------

edad1=input("Ingrese su edad: ")

if type (edad1)==int:
   print("Es posible hacer typecasting")
else:
    print("Se han ingresado letras")

