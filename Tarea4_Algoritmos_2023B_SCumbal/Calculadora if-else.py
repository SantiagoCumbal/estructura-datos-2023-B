print("Calculadora/Santiago Cumbal")
tipo=int(input("Elija las siguientes operaciones: \n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n 5. Potencia\n 6. Modulo\n"))
if tipo==1:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    suma=num1+num2
    print("La respuesta de su operacion: ",suma)
elif tipo==2:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    resta=num1-num2
    print("La respuesta de su operacion: ",resta)
elif tipo==3:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    multiplicacion=num1*num2
    print("La respuesta de su operacion: ",multiplicacion)
elif tipo==4:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    if num2==0:
        print("No se puede dividir para cero")
    else:
        divi=num1/num2
        print("La respuesta de su operacion: ",divi)
elif tipo==5:
    num1=float(input("Ingrese el numero base: "))
    num2=float(input("Ingrese el exponente: "))
    potencia=num1**num2
    print("La respuesta de su operacion: ",potencia)
elif tipo==6:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    modulo=num1%num2
    print("La respuesta de su operacion: ",modulo)
else:
    print("ERROR DE SELECCION")