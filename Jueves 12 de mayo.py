""" Creación de una aplicación que muestre nombre, apellido, edad y estatuta """

nombre="Sandra"
apellido="González"
edad=14
estatura=1.5

str1="Saludos, mi nombre es Juan, mi apellido es Sánchez, \
   tengo 33 años y mi estatura es de 1.75 metros"

print(str1)

print("Saludos, mi nombre es",nombre,"mi apellido es ",apellido,"tengo ",
      edad,"años y mi estatura es de ",estatura," metros")
 
print("Saludos, mi nombre es",
       nombre," mi apellido es ",
       apellido,"tengo ",
       edad,"años y mi estatura es de ",
       estatura,
       "metros")

str2="Saludos, mi nombre es "+nombre+"mi apellido es "+apellido+"tengo "+str(edad)+"años y mi estatura es de "+str(estatura)+" metros"
print("Saludos, mi nombre es "+nombre+"mi apellido es "+str(apellido)+"tengo "+str(edad)+" años y mi estatura es de "+str(estatura)+" metros")


# Operadores de formato

str3="Saludos, mi nombre es %s" % nombre
print(str3)

