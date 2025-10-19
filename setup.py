# /bin/python3
from setuptools import setup, find_packages

setup(
    name='pypswd',
    version='1.3',
    packages=find_packages(),
    install_requires=[
        'cryptography>=3.4.8',
    ],
    entry_points={
        'console_scripts': [
            'pypswd = pypswd:__main__',
        ],
    },
)
