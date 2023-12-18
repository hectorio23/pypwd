# /bin/python3
from setuptools import setup, find_packages

setup(
    name='pypswd',
    version='1.2',
    packages=find_packages(),  # Esto buscará automáticamente paquetes en el directorio actual
    entry_points={
        'console_scripts': [
            'pypswd = pypswd:__main__',
        ],
    },
)
