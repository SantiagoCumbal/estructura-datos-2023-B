#Conversion de Tipos:
#Santiago Cumbal

# Convierte edad a int y suma 10
edad=2
edad = int(edad) + 10
print(edad)

# Convierte edad a str
edad = str(edad)
print(edad)

# Convierte un str a float
numero_float = float('18.66')
print(numero_float)

# Intenta convertir un str no válido a float
# Esto generará un ValueError, ya que 'hola' no es un número válido
try:
    numero_invalido = float('hola')
except ValueError as e:
    print(f"Error: {e}")