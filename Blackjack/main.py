class Carta:  #claas - "molde para hacer carta"
    def __init__(self,palo, valor): #init- función creará mi carta
        self.palo = palo
        self.valor = valor
    
    def __repr__(self): #pinta info de la carta
        return f"{self.valor} de {self.palo}"
