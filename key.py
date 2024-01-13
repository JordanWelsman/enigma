# Module Imports
from random import sample
from typing import Any


# External Visibility
__all__ = ['Key']


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

    def __init__(self, sequence: list = None):
        """
        # Key Constructor

        Initializes a new instance of the Key class.

        ## Parameters
            sequence (list): The sequence of numbers to use for the key.

        ## Returns
            None
        
        """
        if sequence is None:
            sequence = [i for i in range(26)]
            sequence = sample(sequence, len(sequence))
        super().__init__(sequence)
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
