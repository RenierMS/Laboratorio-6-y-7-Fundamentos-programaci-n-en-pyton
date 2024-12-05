# Pida al usuario un numero y determinar si es par o impar
Numero = int(input("Ingresa numero: "))

if Numero % 2 == 0:
    print(f"Este numero {Numero} es par.")
else:
    print(f"Este numero {Numero} es impar.")

# Implementar un bucle for para iterar sobre una lista de números e imprimir sus cuadrados.
Entrada = input("Ingresa una lista de numeros separados por espacios: ")
numeros = [int(x) for x in Entrada.split()]

# Iterar
print("Los cuadrados de los numeros son: ")
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

# Usar bucle while para pedir numero
while True:
    numero_while = int(input("Introduce un numero entre 1 y 10: "))
    if 1 <= numero_while <= 10:
        print(f"El numero {numero_while} esta dentro del rango.")
        break
    else:
        print("Numero fuera del rango. Intentalo de nuevo.")