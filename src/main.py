# /bin/python3.11
import random

class Generator:
    """
    Password generator that creates secure random passwords.
    Divides password length by 3 and generates letters, symbols, and digits.
    """

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
        """Generate a random password with balanced character distribution."""
        calc = self.size // 3

        data = self.return_numbers(calc) + self.return_string(calc) + self.return_symbols(calc + 1)
        random.shuffle(data)
        return "".join(data)