from baraja import Baraja
from mano import Mano

#creamos una baraja
mibaraja = Baraja()

# Crear una mano
mano1 = Mano()

# Mezclar la baraja
mibaraja.mezclar()
mibaraja.mostrar()

# Coger una carta de la baraja y poner lo en la mano
cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
mano1.mostrar_mano()
# Mirar el valor de la mano

# Si valor > 21 se acaba el juego

#sino sigue