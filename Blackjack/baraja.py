import random
from main import Carta

class Baraja:
    def __init__(self):
        self.cartas = []

        palos = ["picas", "corazones", "tréboles", "diamantes"]
        valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9","10", "Jota", "Reina", "Rey"]

        for palo in palos:
            for valor in valores:
                cartanueva = Carta(palo, valor)
                self.cartas.append(cartanueva)
                
    def mezclar (self):
        random.shuffle(self.cartas)

    def contar(self):
        return len(self.cartas)
    
    def coger_carta(self):
        return self.cartas.pop() #pop saca algo de la lista
    
    def mostrar(self):
        for carta in self.cartas:
            print(carta)
