#Santiago Cumbal
alumnos=int(input("Ingrese el número de estudiantes para el viaje: "))

if alumnos>=100:
    costo = 65
elif 99>=alumnos>=50:
    costo = 70
elif 49>=alumnos>=30:
    costo= 95
elif alumnos<30:
    print("La renta del autobus es de 400.")
else:
    print("¡ERROR!.")

print("Costo por alumno es $", costo, "y renta del autobus es de $",costo*alumnos)