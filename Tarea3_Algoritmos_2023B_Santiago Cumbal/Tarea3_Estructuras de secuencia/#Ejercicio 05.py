#Santiago Cumbal
notaPa1= float(input("Ingrese su primera calificacion del parcial:"))
notaPa2= float(input("Ingrese su segunda calificacion del parcial:"))
notaPa3= float(input("Ingrese su tercera calificacion del parcial:"))
examen= float(input("Ingrese la calificaicon de su examen:"))
trabajo= float(input("Ingrese la calificacion de su trabajo final:"))
notasParciales= (notaPa1+notaPa1+notaPa3)*0.55
notaExamen= examen*0.30
notaTrabajo= trabajo*0.15 
promedioFinal= (notasParciales+notaExamen+notaTrabajo)/3
print("Su promedio final es:", promedioFinal) 
