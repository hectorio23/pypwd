# PYPWD Program Usage Guide  
(For UNIX systems only)

The `pypwd` program is a Python-based password manager that allows you to generate and manage passwords with ease. It offers a command-line interface to perform various password-related operations.  
Installation is straightforward, and using it is simple—`pypwd` takes care of managing all your passwords.

## Getting Started

Ensure you have Python 3.x installed on your system. The program includes modules such as `Generator`, `save_pwd`, and `argparse`.

## Usage

- **-l**, **--length**: Generate a random password of the specified length.  
- **-p**, **--print**: Display all stored passwords.  
- **-d**, **--delete**: Delete a specific password associated with an account or company.  
- **-sv**, **--save**: Save the generated password for a user or company.  
- **-e**, **--export**: Export the passwords to another directory in a different format.  
- **-r**, **--repeat**: Generate multiple passwords and display them in the terminal.

```shell
# To generate a password instantly
# Use a command like this:

$ python pypwd.py [options]
```

For example, to display all available commands, use the `-h` or `--help` flag.  
![pypwd_help_example](./screenshots/pypwd_help_example.png)

Here is another example that generates a password and prints it in the terminal:  

```bash
python pypwd.py --length 23 
```
![pypwd_length_example](./screenshots/pypwd_length_example.png)
<sub>Note: It's not necessary to specify the `-p` flag because the password will be displayed in the terminal by default after generation.</sub>

## Installation

For now, you can install it using the `pip` command. The syntax may vary depending on your environment.

On <span style="color:#0f94d2;">Arch Linux</span>, you can install it using the following command:

```bash
sudo pacman -S python-pyspwd
```

Where `pyspwd` is the package to be installed.  
If you choose not to install it globally, you can set an alias or add the following to the end of your shell configuration file (e.g., `.bashrc`, `.zshrc`, or `.config/fish/config.fish`).  
For instance, in Fish, you can write:

```shell
alias pypswd="python $HOME/user/your_directory/pypswd/pypswd.py"
```
