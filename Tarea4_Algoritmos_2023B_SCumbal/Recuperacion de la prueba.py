print("Bienvenido al Carbonero/ Santiago Cumbal")
print("Por favor ingrese los datos para la factura:")
nombre=input("Ingrese el nombre para la factura: ")
cedula=int(input("Ingrese su numero de cedula: "))
correo=input("Ingrese su correo electronico: ")
tipohambu=int(input("Menu:\n 1. Hamburguesa Sencilla\n 2. Hamburguesa Doble\n 3. Hamburguesa Triple\n Ingrese el numero del tipo de la hamburguesa que desea: "))

senci=1.50
doble=2.50
triple=3.25
pretotal=0

if tipohambu==1:
    cantidad=int(input("Ingrese la cantidad de hamburguesas que desea: "))
    pretotal=senci*cantidad
    print("El total previo es: ",pretotal)
elif tipohambu==2:
    cantidad=int(input("Ingrese la cantidad de hamburguesas que desea: "))
    pretotal=doble*cantidad
    print("El total previo es: ",round(pretotal,2))
elif tipohambu==3:
    cantidad=int(input("Ingrese la cantidad de hamburguesas que desea: "))
    pretotal=triple*cantidad
    print("El total previo es: ",round(pretotal,2))
else:
    print("Lo sentimos no ofrecemos ese tipo de hamburguesas")

total=0
metodo=int(input("Metodos de pagos:\n 1. Tarjeta de credito\n 2. Efectivo\n Ingrese el tipo de pago: "))
if metodo==1:
    total=pretotal+(pretotal*0.05)
    print("El total de su factura con el cargo de tarjeta (5%) es de: ",round(total,2))
    print(nombre,"Muchas gracias por su compra su factura se enviara al correo.")
elif metodo==2:
    total=pretotal
    print("El total de su factura en efectivo es de: ",round(total,2))
    print(nombre,"Muchas gracias por su compra su factura se enviara al correo.")
else:
    print("Lo sentimos ingreso un tipo de pago que no disponemos")