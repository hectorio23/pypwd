# /bin/python3.11
import random
import string

class Generator:
    ''' 
    Class Generator:
    This class generates passwords and returns new ones 
    through the `generate` method.

    Attributes:
    - length (int): The default length of the generated password.
    
    Methods:
    - generate(length_password=0) -> str: 
      Generates a password of the specified length.
    '''

    def __init__(self, length=10):
        '''
        Initializes a Generator object with a default length for generated passwords.

        Args:
        - length (int): The default length of the generated password.
        '''
        self.length = length

    @property
    def generate(self, length_password=0) -> str:
        '''
        Generates a password with the specified length.
        
        Args:
        - length_password (int): The length of the generated password. 
                                 If not provided, uses the default length.
        
        Returns:
        - str: The generated password.
        '''
        if length_password == 0:
            length_password = self.length
        
        num_symbols = length_password // 3
        num_letters = (length_password - num_symbols) // 2
        
        words = list(string.ascii_lowercase + string.ascii_uppercase)
        symbols = list(string.punctuation)
        
        random.shuffle(words)
        random.shuffle(symbols)
        
        # Adjust if division is not exact
        remainder = length_password - (num_letters + num_symbols)
        if remainder > 0:
            num_letters += remainder
        
        password = ''
        
        for _ in range(num_letters):
            password += words.pop()
        
        for _ in range(num_symbols):
            password += symbols.pop()
        
        # Shuffle the password for added security
        password_list = list(password)
        random.shuffle(password_list)
        return ''.join(password_list)
