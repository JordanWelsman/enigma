# Module Imports


# External Visibility
__all__ = ['Plugboard']


# Class Definitions
class Plugboard(dict):
    """
    # Enigma Plugboard

    Implements the Enigma plugboard.

    ## Attributes
        None

    ## Methods
        None
    
    """

    def __init__(self, letter_pairs: list[list] = None) -> None:
        """
        # Plugboard Constructor

        Initializes a new instance of the Plugboard class.

        ## Parameters
            letter_pairs (list[list]): The letter pairs to use for the plugboard.

        ## Returns
            None
        
        """
        self._plugboard = {}

        for pair in letter_pairs:
            self._plugboard[pair[0]] = pair[1]
            self._plugboard[pair[1]] = pair[0]

        super().__init__(self._plugboard)
        self._validate()

    
    def __call__(self, input: str) -> str:
        """
        # Plugboard Call

        Implements the call method for the Plugboard class.

        ## Parameters
            input (str): The input string to encode.

        ## Returns
            str: The encoded string.
        
        """
        output = ''
        for letter in input:
            output += self._passthrough(letter)
        
        return output


    def _validate(self) -> None:
        """
        # Plugboard Validation

        Validates the plugboard.

        ## Parameters
            None

        ## Returns
            None
        
        """
        letters = []
        for letter in self:
            if letter in letters:
                raise ValueError('Plugboard cannot contain duplicate letters.')
            letters.append(letter)
        if len(self) > 26:
            raise ValueError('Plugboard cannot contain more than 26 elements.')
        

    def _passthrough(self, letter: str) -> str:
        """
        # Plugboard Passthrough

        Implements the passthrough method for the Plugboard class.

        ## Parameters
            letter (str): The letter to pass through the plugboard.

        ## Returns
            str: The letter after passing through the plugboard.
        
        """
        if letter in self:
            return self[letter]
        else:
            return letter
