import random


class Reflector():

    # Cuidado: Abecedario con ñ, 27 letras, por lo que una tiene que apuntarse a si misma
    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        self.abecedario_aux = list(self.abecedario)
        self.reflector = []
        for letra in self.abecedario:
            if letra in self.abecedario_aux:  # Si aún no se ha eliminado de la auxiliar, le busco un par
                ix_aleatorio = random.randint(0, len(self.abecedario_aux)-1)
                if len(self.abecedario_aux) > 1:  # La última letra restante se emparejará consigo misma
                    while letra == self.abecedario_aux[ix_aleatorio]:
                        ix_aleatorio = random.randint(0, len(self.abecedario_aux)-1)
                self.reflector.append((letra, self.abecedario_aux[ix_aleatorio]))
                self.abecedario_aux.pop(ix_aleatorio)
                if len(self.abecedario_aux) > 1:
                    self.abecedario_aux.remove(letra)
        
    def __str__(self):
        return str(self.reflector)