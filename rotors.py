# Module Imports
from alpha import Alpha
from random import shuffle
from keys import Key, rotor_configurations


# External Visibility
__all__ = ['Rotor']


# Class Definitions
class Rotor(list):
    """
    # Enigma Rotor

    Implements the base class for a single Enigma rotor.

    ## Attributes
        input (list): The input pins for the rotor.
        output (list): The output pins for the rotor.

    ## Methods
        None
    
    """

    def __init__(self, key: Key = None) -> None:
        """
        # Rotor Constructor

        Initializes a new instance of the Rotor class.

        ## Parameters
            None

        ## Returns
            None
        
        """
        self._alpha = Alpha()

        if isinstance(key, str):
            key = Key(key)
        elif key is None:
            key = Key()
        self._rotor = []
        for value in key:
            self._rotor.append(value)

        self._rotation_count = 0

        super().__init__(self._rotor)
        self._validate()


    def __call__(self, input: str, spaces: str = '', decode: bool = False) -> str:
        """
        # Rotor Call

        Implements the call method for the Rotor class.

        ## Parameters
            value (str): The value to be encoded.

        ## Returns
            str: The encoded value.
        
        """
        output = ''
        for character in input:
            if decode:
                output += self._decode(character, spaces)
            else:
                output += self._encode(character, spaces)
        
        return output
    

    def _validate(self) -> bool:
        """
        # Rotor Validation

        Validates the rotor.

        ## Parameters
            None

        ## Returns
            None
        
        """
        if len(self) != 26:
            raise ValueError('Rotor must contain 26 elements.')
        
        return True
    

    def _sanitize(self, input: str, spaces: str) -> str:
        """
        # Input Sanitation

        Sanitizes the input.

        ## Parameters
            input (str): The input to be sanitized.

        ## Returns
            str: The sanitized input.
        
        """
        spaces = spaces.upper() or ''
        output = input.upper()
        output = output.replace(' ', spaces)

        return output
    

    def _encode(self, input: str, spaces: str) -> str:
        """
        # Rotor Encoding

        Encodes a single input.

        ## Parameters
            value (str): The value to be encoded.

        ## Returns
            str: The encoded value.
        
        """
        print(self)

        output = ''
        for value in self._sanitize(input, spaces):
            if value == spaces:
                output += spaces
                continue
            # Convert letter to index and use index to get output
            index = self._alpha.index(value)
            output += self[index]

        self._rotate(1)

        return output
    

    def _decode(self, input: str, spaces: str) -> str:
        """
        # Rotor Decoding

        Decodes a single input.

        ## Parameters
            value (str): The value to be decoded.

        ## Returns
            str: The decoded value.
        
        """
        self._rotate(-1)

        output = ''
        for value in self._sanitize(input, spaces):
            if value == spaces:
                output += spaces
                continue
            # Convert letter to index and use index to get output
            index = self.index(value)
            output += self._alpha[index]

        return output
    

    def _rotate(self, num_clicks: int = 1) -> bool:
        """
        # Rotor Rotation

        Rotates the rotor.

        ## Parameters
            None

        ## Returns
            None
        
        """
        if num_clicks > 0:
            for _ in range(num_clicks):
                self.append(self.pop(0))
        else:
            for _ in range(-num_clicks):
                self.insert(0, self.pop())
                

        self._rotation_count += num_clicks
        self._rotation_count %= 26
        print(f'Rotation Count: {self._rotation_count}')
    
        return True

    