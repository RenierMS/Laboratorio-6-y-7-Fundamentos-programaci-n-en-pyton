# Escribir un programa que imprima un mensaje en la consola
print("Buen día Bienvenido")

# Declarar variable de diferentes tipos
Entero = int(input("Digita el numero entero: "))
Decimal = float(input("Digita el numero decimal: "))
Texto = input("Escriba el texto: ")

# Realizar operaciones matematicas simples
Suma = Entero + Decimal
Resta = Entero - Decimal
Multiplicacion = Entero * Decimal
Division = Entero / Decimal if Decimal != 0 else "No se puede dividir por cero"

# Concatenar cadena texto
Mensaje = f"El numero entero es {Entero}, el numero decimal es {Decimal} y el texto ingresado es: {Texto}"

# Imprimir resultados
print ("/nOperaciones matematicas: ")
print (f"Suma (Entero + Decimal): {Suma}")
print (f"Resta (Entero - Decimal): {Resta}")
print (f"Multiplicacion (Entero * Decimal): {Multiplicacion}")
print (f"Division (Entero / Decimal): {Division}")

# Imprimir mensaje concatenado
print ("\n" + Mensaje)