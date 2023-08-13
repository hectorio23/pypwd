# /bin/python3.11
import random
import string


# This class generate helps to us to generate properties 
# that allowed to us to save our password, encryp it an so more
class Generator:
    def __init__(self, length = 10):
        self.length = length

    # the main method, makes the perfect password
    @property
    def generate(self, length_password:int = 0) -> str:
        if length_password == 0: length_password = self.length
          
        words = list(string.ascii_lowercase + string.ascii_uppercase)
        symbols = list(string.punctuation)

        temp_password = str()

        # This part of the code generate the password
        for item in range(length_password):
            temp_password += words.pop(words.index(random.choice(words)))

            if len(temp_password) == length_password:
                break
            
            if len(symbols) == 31:
                symbols = list(string.punctuation)
                words = list(string.ascii_lowercase + string.ascii_uppercase)

            temp_password += symbols.pop(symbols.index(random.choice(symbols)))


        return str(temp_password)
