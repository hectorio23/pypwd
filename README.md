# PYPWD - Secure Password Manager 

(For UNIX systems only)

The `pypwd` password manager written un Python that allows you to generate and manage passwords with ease. It offers a command-line interface to perform various password-related operations with **AES-256 encryption** for maximum security.
Installation is straightforward, and using it is simple—`pypwd` takes care of managing all your passwords securely with military-grade encryption.

##  Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup your master password (first time only)
python pypwd.py --setup

# 3. Generate a password
python pypwd.py --length 20

# 4. Save a password
python pypwd.py --length 20 --save "Gmail"

# 5. View all passwords
python pypwd.py --print
```

That's it! Your passwords are now encrypted and secure. 

##  Security Features

- **AES-256 Encryption**: All passwords are encrypted using industry-standard AES-256 encryption (same as banks and government agencies)
- **PBKDF2 Key Derivation**: Master password is processed through PBKDF2 with 100,000 iterations for maximum security
- **Secure Salt Generation**: Unique 256-bit salt for each installation prevents rainbow table attacks
- **Master Password Protection**: All operations require your master password for security
- **Zero-Knowledge Architecture**: Your master password is NEVER stored anywhere - only in your memory
- **Military-Grade Security**: Uses the same encryption standards as KeePass, 1Password, and Bitwarden


## Getting Started

Ensure you have Python 3.x installed on your system. The program includes modules such as `Generator`, `save_pwd`, `encryption`, and `argparse`.

### First Time Setup

**Step 1: Setup your master password**

```bash
python pypwd.py --setup
```

This will prompt you to create a master password that will encrypt all your stored passwords.

**Step 2: Start using PYPWD**

```bash
# Generate a password
python pypwd.py --length 20

# Save a password
python pypwd.py --length 20 --save "Gmail"

# View all passwords
python pypwd.py --print
```

**Important:** Your master password is never stored anywhere - you must remember it! If you forget it, you'll need to start over with `--setup`.

##  Troubleshooting

### "Password file not found" Error

``` Password file not found. This appears to be your first time using PYPWD!
Please run: python pypwd.py --setup
```

**Solution:** Run the setup command to create your encrypted password vault.

### "Wrong master password" Error

```
**[X]** Wrong master password! Please try again.
If you forgot your master password, you'll need to start over.
Run: python pypwd.py --setup (this will reset all passwords)
```

**Solution:**

- Try typing your master password again (check for typos)
- If you forgot it, run `python pypwd.py --setup` to start over (This will delete all stored passwords!)

### "Master password must be at least 8 characters long"

**Solution:** Choose a stronger master password with at least 8 characters.

### "Passwords don't match"

**Solution:** Make sure you type the same password in both fields during setup.


## Usage

- **-l**, **--length**: Generate a random password of the specified length.
- **-p**, **--print**: Display all stored passwords.
- **-d**, **--delete**: Delete a specific password associated with an account or company.
- **-sv**, **--save**: Save the generated password for a user or company.
- **-e**, **--export**: Export the passwords to another directory in a different format (json, xml, yaml, txt).
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


