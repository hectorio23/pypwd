# PYPWD Program Usage Guide

The `pypwd` program is a password manager tool that allows you to generate and manage passwords. It provides a command-line interface for various password-related operations.

## Getting Started

Make sure you have Python 3.11 installed on your system. The program consists of modules such as `Generator`, `save_pwd`, and `argparse`.

## Usage

+ -**l**, **--length**: Generate a random password of the specified length.
+ **-p**, **--print**: Print all stored passwords.
+ **-d**, **--delete**: Delete a specific password associated with an account or + company.
+ -**s**, **--show**: Show the generated password.
+ -**sv**, **--save**: Save the generated password for a user or company.

```bash
## For create a password for the moment
## You need to write somethng like here

$ python pypwd.py [options]
```

This is the other example who creates a password and print it on terminal 

```bash
python pypwd.py --length 23 --show True
```

## Executing

For the moment you can install it using the pip command, the sintax will change
depends of your work envoriment.
In <span style="color:#0f94d2;">Arch Linux</span> you can install it using the following instructions.

```bash
sudo pacman -S python-xyz
```

Where `xyz` is the packet you want to install.
IF you don't install you can use stablished an alias. 
For example, on fish you can write:

```bash
alias pypswd "python /$HOME/user/your_directory/pypswd/pypswd.py"
```


