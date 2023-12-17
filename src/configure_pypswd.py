# /bin/python3.11
import subprocess

# Name of the file whose objetive is save the password
NAME_FILE = 'password'
USER = subprocess.check_output('whoami', shell=True, text=True).replace("\n", "")

# Here is the route of the file password
# for example: /home/<user>/<other_route>/<another_route>
ROUTE_FILE = f'/home/{USER}/.config/pypswd'

# Directory PATH
# You can delete NAME_FILE and ROUTE_FILE, but you need to write your 
# directory where you want to save the binary file
PATH = f'{ROUTE_FILE}/{NAME_FILE}.bin'

