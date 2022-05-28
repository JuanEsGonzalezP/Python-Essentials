"""
Desarrollar un programa que permita validar la contraseña introducida por un usuario con las
siguientes comprobaciones:
    Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
    Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
    Debe contener al menos un número entre 0 y 9.
    Debe contener un símbolo especial entre: $,%,*,@
    Tamaño mínimo de 5 caracteres y máximo de 15. Listo
Se debe solicitar la contraseña al usuario, así como informarle sobre estos requisitos para su
contraseña, una vez validada mostrar un mensaje al usuario informándole al respecto.
"""

contrasenia = input("Ingrese su contraseña: ")
letraminuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
letramayuscula = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
simboloespecial = ['$', '%', '*', '@']
numero = [1, 2, 3, 4, 5, 6, 7, 8]

if len(contrasenia)<5 or len(contrasenia)>15: 
    print("La contraseña debe tener entre 5 y 15 caracteres")
elif letraminuscula==False:
    print("la contraseña debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j")
elif letramayuscula==False:
    print("la contraseña Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T ")
elif numero==False:
    print("la contraseña Debe contener al menos un número entre 0 y 9 ")
elif simboloespecial==False:
    print("la contraseña Debe contener un símbolo especial entre: $,%,*,@" )
else:
    print("Contraseña establecida correctamente")
 
