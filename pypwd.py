# Author: Héctor Adán
# https://github.com/hectorio23
# /bin/python3.11

# Import necessary modules
from src.export import export_as  
from src.main import Generator    
from src import save_pwd
import argparse
import sys

# Create an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser(
    prog="pypwd",
    description="A Terminal Password Manager Utility",
    epilog="Your worry-free password manager - this program can generate, display, and manage your passwords securely."
)

# Define command-line arguments
parser.add_argument('-p', '--print', action='store_true', help='Print a generated password.')
parser.add_argument('-d', '--delete', help='Delete a stored password entry.')
parser.add_argument('-l', '--length', type=int, help='Specify the length of the generated password.')
parser.add_argument('-sv', '--save', type=str, help='Save a new password entry.')
parser.add_argument('-e', '--export', type=str, help='Export password files')
parser.add_argument('-r', '--repeat', type=int, default=0, help='Generates n passwords')

# Parse command-line arguments
object_collection = parser.parse_args()
password = ""

# Check for the --print option
if object_collection.print:
    save_pwd.load_data()
    sys.exit()

# Check for the --delete option
if item_delete := object_collection.delete:
    save_pwd.DataHandler.delete_element(item_delete)
    sys.exit()

# Generate passwords based on the --repeat option
if repeater := object_collection.repeat:
    for item in range(repeater):
        print(f"{ item + 1 } - ", Generator(object_collection.length).generate)

# Generate a password of specified length
elif length := object_collection.length: 
    password = Generator(length).generate
    print(password)
    
# Export password files
if export_path := object_collection.export:
    print(export_path)
    export_as(export_path)

# Save a new password entry
if user := object_collection.save:
    try:
        save_pwd.save_data(user, password)
    except Exception as error:
        print(error)
