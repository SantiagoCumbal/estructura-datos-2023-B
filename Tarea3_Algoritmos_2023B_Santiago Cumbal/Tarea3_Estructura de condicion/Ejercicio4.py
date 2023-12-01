#Santiago Cumbal
a=float(input("Ingrese el lado A del triangulo: "))
b=float(input("Ingrese el lado B del trinagulo: "))
c=float(input("Ingrese el lado C del triangulo: "))
if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    print("Es un triangulo rectangulo")
elif a==b==c:
    print("Es un triangulo equilatero")
elif a==b or a==c or b==c:
    print("Es un triangulo isosceles") 
else:
    print("Es un triangulo escaleno")