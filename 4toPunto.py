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
import randon

def Juego_Adivinanza():
    print ("Bienvenid@ al juego")
    print ("Tengo un numero del 1 al 100. ¿Puedes adivinarlo?")

# numero aleatorio del 1 al 100
Numero_Secreto = randon.randint(1, 100)
Intentos = 0
Adivinado = False

while not Adivinado:
    try:
        # Introducir el numero
        Intento = int(input("Cual es tu numero: "))
        Intentos += 1

        if Intento < Numero_Secreto:
            print ("El numero es mayor. Sigue intentando")
        elif Intento > Numero_Secreto:
            print ("El numero es menor. Sigue intentando")
        else:
            print (f"Felicidades Has adivinado el numero {Numero_Secreto} en {Intentos} intentos.")

            Adivinado = True
    except ValueError:
        print ("Por favor, introduce un numero valido.")

# Ejecutar el juego
if_name_ == "_main_":
    Juego_Adivinanza()