#Santiago Cumbal
print("Santiago Cumbal- Bienvenido a TRANSPORTE INTERNACIONAL.");
peso=float(input("Ingrese el peso del paquete(en kg): "));
pesof=peso*1000

print("Ingrese la zona de destino:");
print("1. América del Norte");
print("2. América Central");
print("3. América del Sur");
print("4. Europa");
print("5. Asia");
zona=int(input("Opción: "));

if zona==1:
    costo=24
elif zona==2:
    costo=20
elif zona==3:
    costo=21
elif zona==4:
    costo=10
elif zona==5:
    costo=18

if peso>5:
    print("El peso sobrepasa lo sorportado");
else:
    print("El costo de entrega de paquete es de: $",round(pesof*costo,3))
