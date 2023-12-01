#santiago Cumbal
class EjemploBooleano:
    def __bool__(self):
        return False

    def __len__(self):
        return 0

# Crear una instancia de la clase
objeto_ejemplo = EjemploBooleano()

# Evaluar el valor booleano de la instancia
valor_booleano = bool(objeto_ejemplo)
print(f'Valor booleano: {valor_booleano}')  

# Obtener la longitud de la instancia
longitud = len(objeto_ejemplo)
print(f'Longitud: {longitud}') 