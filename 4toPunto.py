# Script de Resolución de Problemas Simples
# Desarrollar un programa que simule una calculadora básica, permitiendo al usuario realizar sumas, restas, multiplicaciones y divisiones.
def Calculadora():
    print ("Bienvenido a la calculadora")
    print ("Selecciona la operacion")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Division")
    print ("5. Salir")

while True:
    try:
        Opcion = int(input("\Ingresar numero de operacion (1-5): "))
        if Opcion == 5:
            print ("Gracias por usar la calculadora. Chao")
            break
        elif Opcion in [1, 2, 3,4]:
            num1 = float(input("Escriba el primer numero: "))
            num2 = float(input("Escriba el segundo numero: "))

            if Opcion == 1:
                print (f"El resultado de {num1} + {num2} es: {num1 + num2}")
            elif Opcion == 2:
                print (f"El resultado de {num1} - {num2} es: {num1 - num2}")
            elif Opcion == 3:
                print (f"El resultado de {num1} * {num2} es: {num1 * num2}")
            elif Opcion == 4:
                if num2 != 0:
                    print (f"El resultado de {num1} / {num2} es: {num1 / num2}")
                else:
                    print ("Error: No se puede dividir entre cero")
        else:
            print ("Opcion no valida. Favor escoja entre 1 y 5")
    except ValueError:
        print ("Entrada no valida. Favor ingresa un numero")

# Crear un juego de adivinanza donde el programa genere un número aleatorio y el usuario deba adivinarlo, recibiendo pistas de "mayor" o "menor" en cada intento.