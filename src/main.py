# /bin/python3.11
import random

class Generator:
    ''' Class Generator:
    This class makes the hard wor for you!.
    just slices the password's size by 3 and generates
    letters, symbols and digits for security.
    
    - size: the unique param you need!
    '''

    def __init__(self, size=10):
        self.size = size
        self.numbers = "1234567890"
        self.string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.symbols = r"!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"

    def return_numbers(self, length):
        return [random.choice(self.numbers) for _ in range(1, length + 1)]

    def return_string(self, length):
        return [random.choice(self.string) for _ in range(1, length + 1)]

    def return_symbols(self, length):
        return [random.choice(self.symbols) for _ in range(1, length + 1)]


    @property
    def generate(self) -> str:
        calc = self.size // 3

        data =  self.return_numbers(calc) + self.return_string(calc) + self.return_symbols(calc + 1)
        random.shuffle(data)
        return "".join(element for element in data)


