import random


class Rotor():

    abecedario = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

    rotor_resultante = []

    # contador_pulsaciones = 0

    def __init__(self):
        self.creaRotor()

    # En este método se crea los rotores aleatoriamente. A cada letra del abecedario (en orden) se le asigna otra aleatoria.
    # Se almacena el par "letra fija - letra aleatoria" en un diccionario
    def creaRotor(self):
        for i in range(len(self.abecedario)):
            posicion_aleatoria = random.randint(0, 26)
            par_letras_resultante = dict()
            par_letras_resultante[self.abecedario[i]] = self.abecedario[posicion_aleatoria]
            self.rotor_resultante.append(par_letras_resultante)
    
    def avanzaPosicion(self, pulsaciones):
        for i in range(pulsaciones):
            self.rotor_resultante.insert(0, self.rotor_resultante[-1])
            self.rotor_resultante.pop()

    def __str__(self):
        return str(self.rotor_resultante)

if __name__ == "__main__":

    rotor = Rotor()
    print(rotor)
    rotor.avanzaPosicion(3)
    print(rotor)

