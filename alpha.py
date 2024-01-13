# Module Imports


# External Visibility
__all__ = ['Alpha']


# Class Definitions
class Alpha(list):
    """
    # Alphabet

    Implements the alphabet as a set of characters.

    ## Parameters
        None

    ## Returns
        None

    """
    def __init__(self, *args, **kwargs):
        """
        # Alphabet Constructor

        Initializes a new instance of the Alpha class.

        ## Parameters
            None

        ## Returns
            None
            
        """
        super().__init__()
        self.extend([chr(i+65) for i in range(26)])
