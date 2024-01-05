#Ejercicio 1 

objetivo = 1000
print("Bienvenidos al Banco Lyxuz")
nombre=input("Ingrese su nombre ")
cantidad = float(input("Ingrese la cantidad que desea abonar: "))

while cantidad <1:
    print("Dígite una cantidad por encima del 0.")
    cantidad = float(input("Ingrese la cantidad que desea abonar: "))

ahorrado = cantidad
while ahorrado < objetivo:
   
    cantidad_ahorro = float(input("Ingrese la cantidad que desea abonar ingrese 0 para salir: "))
    if (cantidad_ahorro==0):
        print("Good Bye...")
        break
    while (cantidad_ahorro < 1):
        cantidad_ahorro = float(input("Ingrese la cantidad que desea abonar o ingrese 0 para salir: "))
        if (cantidad_ahorro==0):
            print("Good Bye....")
            break
        
    ahorrado = ahorrado + cantidad_ahorro
    print(f"Perfecto Señor {nombre} ha alcanzado el objetivo, lo que recaudado son:{ahorrado} dólares")


#Ejercicio 2 

print("Bienvenidos a Cuantos dígitos locos tiene tu número")
nombre=input("Ingrese su nombre ")
numero = int(input("Ingrese un número: "))  
digitos = len(str(numero))
print(f"Mi estimado {nombre}, su número es {numero} y tiene: {digitos} dígitos")


#Ejercicio 3

print("Bienvenidos Comienzo de impresión")
nombre=input("Ingrese su nombre ")
print("1) Comenzar programa \n2)Imprimir el listado \n3)Finalizar programa")
opcion=int(input("Dígite el número de la opción que desea: "))
while (opcion<=0):
    print("Error, Elija correctamente la opción.")
    print("1) Comenzar programa \n2)Imprimir el listado \n3)Finalizar programa")
    opcion=int(input("Dígite el número de la opción que desea: "))
    if (opcion ==1):
        print("Comenzando el programa...")
    elif(opcion ==2):
        print("Imprimiendo el texto... \n Hola \nTengo 19 años \nMe gusta la pizza") 
    elif (opcion ==3):
        print("Se finalizo el programa y la impresion de texto" )   
    else:
        ("Error, Elija correctamente la opción.")
        
while(opcion==1):
    print("Comenzando el programa...")
    break
while(opcion ==2):
        print("Imprimiendo el texto... \n Hola \nTengo 19 años \nMe gusta la pizza") 
        break
while(opcion ==3):
        print("Se finalizó el programa y la impresión de texto" ) 
        break

#Ejercicio 4
total_pagar = 0
monto = float(input("Ingrese el monto de la compra (ingrese 0 para finalizar): "))

while monto != 0:
    if monto < 0:
        print("Por favor, ingrese un monto válido (mayor o igual a 0).")
    else:
        total_pagar += monto
        print("Su subtotal es: ", total_pagar)
    monto = float(input("Ingrese el monto de la compra (ingrese 0 para finalizar): "))

if total_pagar > 1000:
    descuento = total_pagar * 0.1
    total_pagar -= descuento

print("Total de compras: ", total_pagar)

if total_pagar > 1000:
    print("Descuento aplicado: ", descuento)

#Ejercicio 5
    categorias = ["Perfumería", "Joyería", "Maquillaje", "Ropa"]
total_compra = 0

for categoria in categorias:
    print(f"\n{categoria}:")

    if categoria == "Perfumería":
        articulos = {"Tentación": 30, "Primavera": 28, "Otoño": 15, "Seducción": 35}
    elif categoria == "Joyería":
        articulos = {"Aretes": 7, "Collar": 5, "Cadena": 20, "Pulsera": 15}
    elif categoria == "Maquillaje":
        articulos = {"Sombras": 8, "Maquillaje": 5, "Labiales": 4, "Rimel": 6}
    elif categoria == "Ropa":
        articulos = {"Blusa": 25, "Chaqueta": 60, "Pantalón": 18, "Abrigo": 90}

    for articulo, costo in articulos.items():
        respuesta = input(f"¿Desea comprar {articulo}? (S/N): ").upper()

        if respuesta == 'S':
            cantidad = int(input(f"Ingrese la cantidad de {articulo} que desea comprar: "))
            subtotal_articulo = cantidad * costo
            total_compra += subtotal_articulo

            comprar_otro = input(f"¿Desea comprar otro artículo de {categoria}? (S/N): ").upper()
            if comprar_otro != 'S':
                break

print("\nResumen de la compra:")
for categoria in categorias:
    cantidad_categoria = sum(1 for _ in articulos if input(f"¿Desea comprar {_}? (S/N): ").upper() == 'S')
    print(f"Cantidad de artículos de {categoria}: {cantidad_categoria}")

print(f"\nTotal de la compra: ${total_compra}")

#Ejercicio 6
lineas_completas = 0
total_digitos = 0
print("Ingrese el nombre de los libros: ")
print("Use * para finalizar o / para finalziar una linea")
titulo = input("Libro: ")

while titulo != "*":
    if titulo == "/":
        print("Línea completa. Aparecen ",total_digitos," dígitos numéricos.")
        total_digitos = 0
        lineas_completas += 1
    else:
        total_digitos += sum(c.isdigit() for c in titulo)

    titulo = input("Libro: ")

print("Fin. Se leyeron ",lineas_completas," líneas completas.")