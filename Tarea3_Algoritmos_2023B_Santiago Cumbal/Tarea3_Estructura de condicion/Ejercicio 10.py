#Santiago Cumbal
estudiante= str(input("Ingrese el nombre del estudiante: ")).title()

n1=float(input("Ingrese nota 1: "))
n2=float(input("Ingrese nota 2: "))
n3=float(input("Ingrese nota 3: "))

promedio= (n1+n2+n3)/3

if  9<=promedio<=10 :
    print(estudiante, "Felicidades Su nota es:",round(promedio,2),"equivale a excelente.")
elif  7<=promedio<=8:
    print(estudiante, "Siga adelante Su nota es:",round(promedio,2),"equivale a muy buena.")
elif  6<=promedio<=7:
    print(estudiante, "Debe esforazarse más Su nota es:",round(promedio,2),"equivale a buena.")
elif  0<=promedio<=4:
    print(estudiante, " Usted puede reprobar ya que Su nota es:",round(promedio,2),"equivale a regular.")
else:
    print("fuera de rango.")
