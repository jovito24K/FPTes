import random

def daño_critico():
    return random.randint(1,5)
def daño():
    return random.randint(2,10)

ataque=daño
p1 = 60
p2 = 60
while True:
    print("1. Jugador 1")
    print("2. Jugador 2")
    print("3. Salir")
    
    try:
        j = int(input(":"))
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue
    
    if j == 1:  # Jugador 1
        atacar = ataque()
        print(f"El jugador 1 sacó {atacar }")
        p2 -= atacar
        if p2 <0:
            exceso1 = p2 - 0 
            p2 = 0 
        print(f"el daño que resivio el jugador 2 es de : {atacar} el hp del jugador2  quedo en {p2}")
        
        if p2 == 0 :
            print("jugador 2 has pedirdo")
            break
    else:

        if j == 2:  # Jugador 2
            atacar = ataque()
            print(f"El jugador 2 sacó {atacar }")
            p1 -= atacar
            if p1 <0:
                exceso2 = p1 - 0 
                p1 = 0 
            print(f"el daño que resivio el jugador 1 es de : {atacar} el hp del jugador 1 quedo en {p1}")
            if p1 ==0:
                print("jugador 1 has pedirdo")
                break
            else:

                if j == 3:  # Salir
                        print("¡Gracias por jugar!")
                        break
        else:
             print("Opción no válida. Por favor selecciona 1, 2, o 3.")
