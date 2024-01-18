# Module Imports
from random import random as generate_seed, seed as set_seed, shuffle
from typing import Any


# External Visibility
__all__ = ['Key']


# Key Configurations
reflector_configurations = {
    'A': {
        'key': [4, 9, 12, 25, 0, 11, 6, 3, 17, 1, 7, 5, 2, 23, 24, 22, 21, 8, 19, 18, 16, 15, 14, 13, 20, 10]
    },
    'B': {
        'key': [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 25, 9, 0, 12, 24, 4, 22, 5, 2, 21, 1, 14, 10, 19]
    },
    'C': {
        'key': [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 7, 1, 19, 12, 16, 22, 20, 18, 11, 13, 6, 10, 2]
    }
}

rotor_configurations = {
    'I': {
        'key': [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 17, 15, 0, 18, 1, 9, 2, 8],
        'notch': 'Q'
    },
    'II': {
        'key': [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 24, 6, 25, 13, 5, 21, 4, 14, 15],
        'notch': 'E'
    },
    'III': {
        'key': [1, 3, 5, 7, 9, 11, 12, 15, 17, 19, 23, 20, 24, 21, 25, 13, 10, 14, 6, 0, 8, 4, 22, 2, 18, 16],
        'notch': 'V'
    },
    'IV': {
        'key': [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 10, 6, 12, 2, 22, 3, 1],
        'notch': 'J'
    },
    'V': {
        'key': [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 0, 18, 3, 5, 16, 22, 25, 13, 14, 12, 7, 4, 10, 23, 11, 2],
        'notch': 'Z'
    },
}


# Class Definitions
class Key(list):
    """
    # Enigma Key

    Implements the Enigma rotor key.

    ## Attributes
        None

    ## Methods
        None
    
    """

    def __init__(self, config: str = None, sequence: list = None, seed: Any = None):
        """
        # Key Constructor

        Initializes a new instance of the Key class.

        ## Parameters
            config (str): The configuration to use for the key.
            sequence (list): The sequence of numbers to use for the key.
            seed (Any): The seed to use for the key.

        ## Returns
            None
        
        """
        # Generate a random seed if none is provided
        if seed is None:
            seed = generate_seed() # generate a seed
        set_seed(seed) # set the seed

        # Generate a random sequence if none is provided
        if config is not None:
            try:
                sequence = rotor_configurations[config]['key']
            except KeyError:
                raise ValueError('Invalid rotor configuration.')
        else:
            if sequence is None:
                sequence = list(range(26))
                shuffle(sequence)
        
        super().__init__(sequence) # turn self into a list subtype
        self._validate()

    def _validate(self):
        """
        # Key Validation

        Validates the key.

        ## Parameters
            None

        ## Returns
            None
        
        """
        if len(self) != 26:
            raise ValueError('Key must contain 26 elements.')
        for i in range(26):
            if i not in self:
                raise ValueError('Key must contain all numbers from 0 to 25.')
        return True
    
    def __str__(self):
        """
        # Key String

        Returns the string representation of the key.

        ## Parameters
            None

        ## Returns
            str: The string representation of the key.
        
        """
        return(f'Key({", ".join([str(i) for i in self])})')
    
    def __repr__(self):
        """
        # Key Representation

        Returns the string representation of the key.

        ## Parameters
            None

        ## Returns
            str: The string representation of the key.
        
        """
        return self.__str__()
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
