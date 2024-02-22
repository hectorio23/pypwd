# Author: Héctor Adán
# https://github.com/hectorio23

class TextFormat:
    _instance = None

    def __init__(self, content="") -> None:
        self.__file_content = content

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance 
    
    def add(self, content: str) -> None:
        self.__file_content += content

    def get_content(self) -> str:
        return self.__file_content