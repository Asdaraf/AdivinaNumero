import random

numero_random = random.randint(1,100)

jugador = input("Nombre del Jugador: ")
print(f"Bienvenido al juego, {jugador}. Adivina el numero entre 1 a 100")

intento = 0

while True:

    #Verifica si el valor ingresado es un numero y no un string, y si el numero esta entre 1 a 100
    
    numero_string = input("Ingresa el número que crees que es. (presiona 0 para salir del juego): ")
    if numero_string.isnumeric():
        numero = int(numero_string)
        if numero > 100:
            print("Error. Debes ingresar un numero entre 1 a 100")
            continue
    else:
        print("Error. Debes ingresar un número")
        continue
    
    #Verifica si el numero ingresado es 0 para terminar con el juego
    if numero == 0:
        if (intento==0):
            print("Ni siquiera lo intentaste :(.")
        elif (intento==1):
            print(f"No lo lograste a pesar de tratar {intento} vez. Mas suerte para la proxima")
        else:
            print(f"No lo lograste a pesar de tratar {intento} veces. Mas suerte para la proxima")
        break
    
    intento += 1

    if abs(numero-numero_random) > 0 and abs(numero-numero_random) <= 5:
        print(f"Sorry {jugador}, ese no es pero estas a una distancia menor o igual a 5. Vuelve a intentarlo.")
    elif abs(numero-numero_random) > 5 and abs(numero-numero_random) <= 10:
        print(f"Sorry {jugador}, ese no es pero estas a una distancia mayor que 5 y menor o igual a 10. Vuelve a intentarlo.")
    elif abs(numero-numero_random) > 10 and abs(numero-numero_random) <= 20:
        print(f"Sorry {jugador}, ese no es pero estas a una distancia mayor que 10 y menor o igual a 20. Vuelve a intentarlo.")
    elif abs(numero-numero_random) > 20:
        print(f"Sorry {jugador}, ese no es pero estas a una distancia mayor que 20. Vuelve a intentarlo.")
    else:
        if (intento == 1):
            print(f"Felicitaciones {jugador}, lo lograste a la primera!")
        else:        
            print(f"Felicitaciones {jugador}, lo lograste en {intento} intentos")
        break
    
    