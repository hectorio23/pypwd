# /bin/python3.11
from src.main import Generator      
from src import save_pwd
import argparse
import sys


# Argument object
parser = argparse.ArgumentParser(
    prog="pypswd",
    description="A Terminal Password Manager Utility",
    epilog="Your worry-free password manager – this program can generate, display, and manage your passwords securely."
)

parser.add_argument('-p', '--print', action='store_true', help='Print a generated password.')
parser.add_argument('-d', '--delete', action='store_true', help='Delete a stored password entry.')
parser.add_argument('-l', '--length', type=int, help='Specify the length of the generated password.')
parser.add_argument('-s', '--show', action='store_true', help='Display stored passwords.')
parser.add_argument('-sv', '--save', type=str, help='Save a new password entry.')


# ZONE OF VARIABLES
object_collection = parser.parse_args()
password = ""

# This stantment find out that the user
# wrote the command show_all and print all the passwords on 
# the terminal, then, the following commands are not necesaries
# the program will ignore them
if object_collection.print:
    save_pwd.load_data()
    sys.exit()

if item_delete := object_collection.delete:
    save_pwd.load_data('remove', item_delete)
    sys.exit()
# The following zone is the comprobation of the 
# input user
if length := object_collection.length:
    password = Generator(length).generate
    print(password)

# Show data by the terminal
if object_collection.show:
    print(password)

# Save the data in a binary file 
# with the sintax key -> value (yes, a dictonary in Python)
# If the user don't input nothing in this section, it raises an error
# notice him that he need to specify a user or company
# for example: <user_account>: <user_password>
if user := object_collection.save:
    try:
        save_pwd.save_data(user, password)
    except Exception as error:
        print(error)