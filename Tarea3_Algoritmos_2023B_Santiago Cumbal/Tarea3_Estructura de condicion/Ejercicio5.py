#Santiago Cumbal
precioinicial=float(input("Ingrese el precio inicial del kilo de uva: "))
kilo=float(input("Ingrese la cantidad de kilos que desea: "))
tipo=input("Ingrese el tipo de uva A o B: ")
tama=int(input("Ingrese el tamaño 1 o 2: "))
extra=0
if tipo == "A":
        if tama == 1:
            extra = 0.20
        elif tama == 2:
            extra = 0.30
elif tipo == "B":
        if tama == 1:
            extra = -0.30
        elif tama == 2:
            extra = -0.50
else:
     print("Eleccion invalida")
preciokilo=precioinicial + extra
preciofinal=preciokilo*kilo
print("La ganancia obtenida por las uvas es de: ",preciofinal)
