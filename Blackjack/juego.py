from baraja import Baraja
from mano import Mano

#creamos una baraja
mibaraja = Baraja()

# Crear una mano
mano1 = Mano()

# Mezclar la baraja
mibaraja.mezclar()


while True:
    # Coger una carta de la baraja y poner lo en la mano
   
    cartacogida = mibaraja.coger_carta()
    mano1.añadir_carta(cartacogida)

    mano1.mostrar_mano()

    # Mirar el valor de la mano
    mano1.calcula_valor()
    print(mano1.valor)

    # Si valor > 21 se acaba el juego
    if mano1.valor == 21:
        print("Has ganado")
    elif mano1.valor > 21:
        print("Has perdidio")
        break

#sino sigue