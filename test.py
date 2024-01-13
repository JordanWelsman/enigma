# Module Imports
from plugboard import Plugboard
from rotors import Rotor


# Test Environment
p = Plugboard([['J', 'O'], ['R', 'D'], ['A', 'N']])
r = Rotor()

# string = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
# print(f"Raw:      {string}")

# encoded = r.encode(string, " ")
# print(f"Encoded:  {encoded}")

# decoded = r.decode(encoded, " ")
# print(f"Decoded:  {decoded}")

print(p('JORDAN'))