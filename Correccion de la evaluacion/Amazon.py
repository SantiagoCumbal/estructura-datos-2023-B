print("Por favor inicie sesion:") 
email=str(input("Ingrese su correo electronico: "))
contraseña=str(input("Ingrese su contraseña: "))
emailcorrec=str("tosh@gmail.com")
contraseñacorrec=str("Secret*")
while email!=emailcorrec or contraseña!=contraseñacorrec:
    print(" ERROR \n Credenciales incorrectas")
    email=str(input("Ingrese su correo electronico: "))
    contraseña=str(input("Ingrese su contraseña: "))
print("Ingreso Exitoso")

i=1
precompra=0
descupon=0
while True:
    print("Bienvenido a AMAZON \nMenu de opciones: \n1. Ingresar productos al carrito de compras \n2. Facturar \n3. Salir")
    opcion=int(input("Ingrese su opcion: "))
    match opcion:
        case 1: 
            producto=int(input("Ingrese el numero de productos: "))
            if producto<=0:
                print("ERROR \n Productos mal ingresados")
            elif producto>0:
                while i<=producto:
                    print("¿El producto N°",i,"tiene cupon de descuento?")
                    elecupon=str(input("Ingrese si o no: "))
                    if elecupon=="no" or elecupon=="No":
                        precioproducto=float(input("Ingrese el precio del producto: "))
                        producto0=0
                        while precioproducto==producto0: 
                            print("ERROR DEL PRECIO \nPor favor ingrese nuevamente el precio del producto")
                            precioproducto=float(input("Ingrese el precio del producto: "))
                        precompra+=precioproducto
                    elif elecupon=="si" or elecupon=="Si":
                        cupon=str(input("Ingrese el cupon del producto: "))
                        nombrecupon=str("enero")
                        while cupon!=nombrecupon:
                            print("ERROR DEL CUPON \nPor favor ingrese nuevamente el cupon")
                            cupon=str(input("Ingrese el cupon del producto: "))
                        precioproducto=float(input("Ingrese el precio del producto: "))
                        producto0=0
                        while precioproducto==producto0:
                            print("ERROR DEL PRECIO \nPor favor ingrese nuevamente el precio del producto")
                            precioproducto=float(input("Ingrese el precio del producto: "))
                        prodescu=precioproducto*(0.20)
                        productocondescuento=precioproducto-prodescu
                        precompra+=productocondescuento
                        descupon+=1
                    i+=1
        case 2:
            if descupon>0:
                print("Factura Electronica \nSu factura sera enviada al correo")
                print("Descuento Aplicado")
                print("El copdigo del cupon es enero")
                print("El numero de productos es: ",producto)
                print("Productos con descuentos:", descupon)
                print("El precio total de la compra es de: $",precompra)
            elif descupon<=0:
                print("Factura Electronica \nSu factura sera enviada al correo")
                print("El numero de productos es: ",producto) 
                print("El precio total de la compra es de: $",precompra)
            break

        case 3:
            print("Saliendo del programa \nMuchas gracias por usar nuestro sistema")
            break
        case _:
            print("ERROR DE SELECCION")
