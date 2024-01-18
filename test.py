# Module Imports
from keys import Key, reflector_configurations, rotor_configurations
from plugboard import Plugboard
from random import seed, shuffle
from rotors import Rotor
from time import sleep


# Test Environment
k = Key('I')
r = Rotor(k)
print(k)
print(r)


# rotor_1 = 0
# rotor_2 = 0
# rotor_3 = 0

# for _ in range(10_000):
#     sleep(0.01)
#     rotor_1 += 1
#     if rotor_1 == 26:
#         rotor_1 = 0
#         rotor_2 += 1
#         if rotor_2 == 26:
#             rotor_2 = 0
#             rotor_3 += 1
#             if rotor_3 == 26:
#                 rotor_3 = 0

#     print(f'{rotor_1}, {rotor_2}, {rotor_3}')
