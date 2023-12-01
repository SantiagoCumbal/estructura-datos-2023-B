#Santigo Cumbal
cadena=input("Ingrese una palabra: ")
mayuscula=False
for caracter in cadena:
    if caracter.isupper():
        mayuscula = True
        break
if mayuscula:
    print("La palabra ingresada contiene al menos una letra mayúscula.")
else:
    print("La palabra ingresada no contiene letras mayúsculas.")