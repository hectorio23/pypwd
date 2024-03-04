# /bin/python3.11
import random
import string


# This class generate helps to us to generate properties 
# that allowed to us to save our password, encryp it an so more
class Generator:
    ''' Generator

    This is the class who generates the passwords and return new one
    for that you can access to `generate` method.

    '''
    def __init__(self, length=10):
        self.length = length

    # the main method, makes the perfect password
    @property
    def generate(self, length_password=0) -> str:
        if length_password == 0:
            length_password = self.length
        
        num_symbols = length_password // 3
        num_letters = (length_password - num_symbols) // 2
        
        words = list(string.ascii_lowercase + string.ascii_uppercase)
        symbols = list(string.punctuation)
        
        random.shuffle(words)
        random.shuffle(symbols)
        
        # Ajuste si la división no es exacta
        remainder = length_password - (num_letters + num_symbols)
        if remainder > 0:
            num_letters += remainder
        
        password = ''
        
        for _ in range(num_letters):
            password += words.pop()
        
        for _ in range(num_symbols):
            password += symbols.pop()
        
        # Mezcla la contraseña para mayor seguridad
        password_list = list(password)
        random.shuffle(password_list)
        return ''.join(password_list)
