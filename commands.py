# /bin/python3.11
import argparse
from src.main import Generator

parser = argparse.ArgumentParser(
    prog="pypswd",
    description="Manager of password",
    epilog="Don't with yours passwords  "
)

parser.add_argument('-l'  , '--length', type=int)
parser.add_argument('-s', '--show')
parser.add_argument('-sv', '--save')

# ZONE OF VARIABLES

object_collection = parser.parse_args()
password = ""



if length := object_collection.length:
    password = Generator(length).generate
if object_collection.show:
    print(password)
if object_collection.save:
    
