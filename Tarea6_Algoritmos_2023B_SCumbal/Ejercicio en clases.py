print("Bienvenidos a la Tabla")
numero=int(input("  Ingrese un número para crear su tabla de multiplicar"))
i=1
while i<=12:
    producto=numero*i
    print(numero,"x",i,"=",producto)
    i +=1
    
#Ejercicio 2
print("Bienvenidos a los Números pares ")
m=0
while m<=50:
    print (m)
    m +=2

#Ejercicio 3
print("Bienvenidos a los °° Números pares e impares °°")
numero_f=int(input("Ingrese el numero final que desea que termine: "))
print("Número impares")
m=1
while m<=numero_f:
    print(m)
    m +=2
print("Números pares")
j=0
while j<=numero_f:
    print(j)
    j +=2
    
#Ejercicio 4
print("Bienvenidos a los °° Números pares e impares 2 °°")
val=int(input("Ingresa la cantidad de números que deseas ejecutar: "))
conta=1
impar=0
par=0
while(conta<=val):
    numero=int(input("Ingrese el número: "))
    conta +=1
    modulo=numero%2
    if(modulo==0):
        par+=1
    else:
        impar+=1    
print("Números pares son : ",par)
print("Números impares son: ", impar)

#Ejercicio 5
print("Bienvenidos a los °° Calculadora°°")
conta=1
rat=1
rel=0
while(rat!=0):
    numero=int(input("Ingrese el número: "))
    conta +=1
    if(numero==0):
        rat-=1
    else:
        rel+=numero
    print("La suma es: ", rel)
print ("La suma total es: ", rel )  

#Ejercico 5
print("Bienvenidos a los °° Calculadora°°")
conta=-1
rat=1
rel=0
while(rat!=0):
    numero=float(input("Ingrese el número: "))
    conta +=1
    if(numero==0):
        rat-=1
    else:
        rel= rel+numero
        print("La suma es: ", rel)
promedio= rel/conta
print("El promedio es: ",round(promedio, 2))

#Ejercicio 6
for i in range (0,101, 5):
    print(i)
   
numero=int(input("Ingrese el número que desea su múltiplos: "))
numero_final=int(input("Ingrese el número final: "))
limite_final=numero_final+1
if (numero_final>0):
    for i in range (0,limite_final, numero):
        print(i)
else:
    print("Digite los numeros correctamente") 

#Ejercicio SUCESIÓN FIBONACI
numero=int(input("Ingrese el número: "))
sum= numero+1
if (numero>1):
    for i in range (1, numero, sum):
        print(i)
