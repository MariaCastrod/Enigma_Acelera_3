from rotor import *
from reflector import *

rotor = Rotor()
reflector = Reflector()
    

# Sin introducir posición inicial
print(rotor)
print(reflector)
#print(rotor.codifica("Z"))
#print(rotor.codifica("@"))

# Introducimos posición inicial "C" e imprimimos el rotor modificado
rotor.posicionInicial("C")
print(rotor.rotor_ix0)

# Prueba codifica "C", "A", "S", "A", con la intención de comprobar el avance del rotor
print(rotor.codifica("C"))
print(rotor.rotor_ix0)
print(rotor.codifica("A"))
print(rotor.rotor_ix0)
print(rotor.codifica("S"))
print(rotor.rotor_ix0)
print(rotor.codifica("A"))