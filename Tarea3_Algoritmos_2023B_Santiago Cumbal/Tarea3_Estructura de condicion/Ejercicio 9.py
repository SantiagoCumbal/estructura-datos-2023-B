#Santiago Cumbal
motor= int(input("Ingrese el tipo de motor (1. 2. 3. 4. ): "))

if motor==0:
    print("No hay un valor definido para el tipo de bomba.")
elif motor==1:
    print("Labomba es una bomba de agua.")
elif motor==2:
    print("La bomba es una bomba de gasolina.")
elif motor==3:
    print("La bomba es una bomba de hormigón.")
elif motor==4:
    print("La bomba es una bomba de pasta alimenticia.")
else:
    print("No existe un valor válido para tipo de bomba.")
