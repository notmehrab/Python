class Carta:  #claas - "molde para hacer carta"
    def __init__(self,palo, valor): #init- función creará mi carta
        self.palo = palo
        self.valor = valor
    
    def __repr__(self): #pinta info de la carta
        return f"{self.valor} de {self.palo}"

carta1 = Carta("corazones", "reina")
carta2 = Carta("treboles", "as")

valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9","10", "Jota", "Reina", "Rey"]
baraja = []

for valor in valores:
    cartanueva = Carta("picas", valor)
    baraja.append(cartanueva)

print(baraja)