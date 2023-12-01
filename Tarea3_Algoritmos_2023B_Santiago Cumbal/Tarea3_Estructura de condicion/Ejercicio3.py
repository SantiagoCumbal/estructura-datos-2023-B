#Santiago Cumbal
n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese un numero: "))
n3=int(input("Ingrese un numero: "))
if n1>n2 and n2>n3:
    print("El orden de sus numeros son : ",n1," ",n2," ",n3)
elif n2>n1 and n1>n3:
    print("El orden de sus numeros son : ",n2," ",n1," ",n3)
elif n2>n1 and n2>n3:
    print("El orden de sus numeros son : ",n2," ",n3," ",n1)
elif n1>n3 and n3>n2:
    print("El orden de sus numeros son : ",n1," ",n3," ",n2)
elif n3>n1 and n1>n2:
    print("El orden de sus numeros son : ",n3," ",n1," ",n2)
else:
    print("El orden de sus numeros son : ",n3," ",n2," ",n1)