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

# 3. Implementar un script que permita al usuario agregar elementos a una lista o actualizar valores en un diccionario
def Agregar_Estudiante(Estudiantes):
    Nombre = input ("Escribe el nombre del estudiante para agregar: ")
    Estudiantes.append(Nombre)

# Funcion para agragar o actualizar
def Agregar_o_Actualizar_Contaacto(Contactos):
    Nombre = input("Escribe el nonbre del contacto: ")
    Correo = input (f"Escribe el correo de {Nombre}: ")
    Contactos{Nombre} = Correo

# Escoger menu
def Menu():
    Estudiantes = []
    Contactos = {}

    while True:
        print ("\nMenu:")
        print ("1. Agregar Estudiante a la lista")
        print ("2. Agregar/Actualizar contacto")
        print ("3. Mostrar lista de Estudiantes")
        print ("4. Mostrar Contactos")
        print ("5. Salir")

        Opcion = input("Seleccionar una opcion: ")

        if Opcion == "1":
            Agregar_Estudiante(Estudiantes)
        elif Opcion == "2":
            Agregar_o_Actualizar_Contaacto(Contactos)
        elif Opcion == "3":
            print ("\nLista de estudiantes: ")
            for estudiante in Estudiantes:
                print (estudiante)
        elif Opcion == "4":
            print ("\nInformacion de contacto: ")
            for Nombre, Correo in Contactos.items():
                print (f"{Nombre}: {Correo}")
        elif Opcion == "5":
            print ("Saliendo...")
            break
        else:
            print ("Opcion incorrecta, favor ingrese una opcion correcta")