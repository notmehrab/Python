class Mano:
    def __init__(self):
        self.cartas = []
        self.valor = 0
#Añadir cartas en la mano 
    def añadir_carta(self, carta):
        self.cartas.append(carta)
#mostarar mano
    def mostrar_mano(self):
        for carta in self.cartas:
            print(carta)