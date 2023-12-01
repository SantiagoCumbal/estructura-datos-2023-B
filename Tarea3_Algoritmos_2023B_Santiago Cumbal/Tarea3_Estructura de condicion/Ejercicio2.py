#Santiago Cumbal
nota=float(input("Ingrese su nota: "))
edad=int(input("Ingrese su edad: "))
sexo=str(input("Ingrese su sexo F si es femenino y M si es masculino: "))
if nota>=5 and edad>=18 and sexo=="F":
    print("ACEPTADA")
elif nota>=5 and edad>=18 and sexo=="M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")