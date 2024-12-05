# 1. Crear una lista de elementos, como nombres de estudiantes, y mostrar cada uno utilizando un bucle.
Estudiantes = []

# Ingresar nombres de estudiantes
n = int(input("¿Cuantos estudiantes va ha ingresar? "))
for _ in range(n):
    Nombre = input("Escribe el nombre del estudiante: ")
    Estudiantes.append(Nombre)

# Consultar los nombre de los estudiantes
print ("\nLista de estudiantes:")
for estudiante in Estudiantes:
    print (estudiante)

# 2. Crear un diccionario simple que almacene información de contacto (nombre, correo) y mostrar sus claves y valores.
Contactos = {}

# Ingresar datos
n = int(input("Numero de  contactos ha agregar "))
for _ in range(n):
    Nombre = input ("Escribe el nombre del contacto: ")
    Correo = input (f"Escribe el correo de {Nombre}: ")
    Contactos{Nombre} = Correo

# Ver claves y diccionario
print ("\nInformacion de contacto: ")
for Nombre, Correo in Contactos.items():
    print(f"{Nombre}: {Correo}")
