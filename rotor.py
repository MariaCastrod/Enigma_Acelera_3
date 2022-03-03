import random


class Rotor():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        self.rotor = []
        abc_auxiliar = list(self.abecedario)
        for letra in self.abecedario:
            ix_aleatorio = random.randint(0, len(abc_auxiliar)-1)
            self.rotor.append((letra, abc_auxiliar[ix_aleatorio]))
            abc_auxiliar.pop(ix_aleatorio)
        # Copia del rotor creado para modificar sobre ella la posición inicial, manteniendo el otro intacto
        self.rotor_ix0 = self.rotor[:] 

    # Método que recibe la letra tecleada, y en base a la posición inicial y los avances, devuelva la codificada
    def codifica(self, letra):
        ix = self.abecedario.find(letra)
        if ix != -1:
            letra_codif = self.rotor_ix0[ix][1]
            self.avanzaPosicion()
            return letra_codif
        raise ValueError("{} no pertenece al abecedario".format(letra))   

    # Método al que le indico la letra inicial cada día y modifica el rotor 
    def posicionInicial(self, letra):
        ix = self.abecedario.find(letra)
        if ix != -1:
            self.rotor_ix0 = self.rotor[ix:] + self.rotor[:ix]
            # Opción 2:
            '''for i in range(0,ix):
                self.rotor_ix0.append(self.rotor_ix0[0])
                self.rotor_ix0.pop(0)'''
        else:
            raise ValueError("{} no pertenece al abecedario".format(letra))    

    # Método para avanzar 1 posición con cada codificación de letra
    def avanzaPosicion(self):
        self.rotor_ix0 = self.rotor_ix0[1:] + self.rotor_ix0[0:1]
        # Opción 2:
        '''for i in range(pulsaciones):
            self.rotor.insert(0, self.rotor[-1])
            self.rotor.pop()'''

    def __str__(self):
        return str(self.rotor_ix0)
