# /bin/python3.11
"""
Encryption module for PYPWD password manager.
Implements AES-256 encryption with PBKDF2 key derivation.
"""

import os
import base64
import getpass
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class EncryptionManager:
    """
    Handles encryption and decryption of password data using AES-256.
    Uses PBKDF2 for key derivation from master password.
    """
    
    def __init__(self):
        self.salt_file = os.path.join(os.path.dirname(__file__), '.salt')
        self.salt = self._load_or_create_salt()
    
    def _load_or_create_salt(self) -> bytes:
        """Load existing salt or create a new one."""
        if os.path.exists(self.salt_file):
            with open(self.salt_file, 'rb') as f:
                return f.read()
        
        salt = os.urandom(32)
        with open(self.salt_file, 'wb') as f:
            f.write(salt)
        os.chmod(self.salt_file, 0o600)
        return salt
    
    def _derive_key(self, master_password: str) -> bytes:
        """
        Derive encryption key from master password using PBKDF2.
        
        Args:
            master_password: User's master password
            
        Returns:
            Derived 256-bit encryption key
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(master_password.encode('utf-8'))
    
    def encrypt_data(self, data: dict, master_password: str) -> str:
        """
        Encrypt password data using AES-256 in CBC mode.
        
        Args:
            data: Dictionary containing password data
            master_password: Master password for encryption
            
        Returns:
            Base64 encoded encrypted data
        """
        key = self._derive_key(master_password)
        json_data = json.dumps(data).encode('utf-8')
        iv = os.urandom(16)
        
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # PKCS7 padding: pad to 16-byte block boundary
        padding_length = 16 - (len(json_data) % 16)
        padded_data = json_data + bytes([padding_length] * padding_length)
        
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        combined = iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    
    def decrypt_data(self, encrypted_data: str, master_password: str) -> dict:
        """
        Decrypt password data.
        
        Args:
            encrypted_data: Base64 encoded encrypted data
            master_password: Master password for decryption
            
        Returns:
            Decrypted password data as dictionary
        """
        try:
            key = self._derive_key(master_password)
            combined = base64.b64decode(encrypted_data.encode('utf-8'))
            
            iv = combined[:16]
            encrypted = combined[16:]
            
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            
            decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
            
            # Remove PKCS7 padding
            padding_length = decrypted_padded[-1]
            decrypted_data = decrypted_padded[:-padding_length]
            
            return json.loads(decrypted_data.decode('utf-8'))
            
        except Exception as e:
            raise ValueError(f"Decryption failed. Check your master password: {e}")
    
def get_master_password() -> str:
    """
    Securely prompt user for master password.
    
    Returns:
        Master password entered by user
    """
    return getpass.getpass("Enter master password: ")


def setup_master_password() -> str:
    """
    Setup master password for first-time users.
    
    Returns:
        Confirmed master password
    """
    while True:
        password1 = getpass.getpass("Set master password: ")
        password2 = getpass.getpass("Confirm master password: ")
        
        if password1 == password2:
            if len(password1) < 8:
                print("Master password must be at least 8 characters long.")
                continue
            print("Master password set successfully!")
            return password1
        else:
            print("Passwords don't match. Try again.")


def encrypt_passwords(passwords: dict, master_password: str) -> str:
    """
    Encrypt password dictionary.
    
    Args:
        passwords: Dictionary of passwords to encrypt
        master_password: Master password for encryption
        
    Returns:
        Encrypted password data
    """
    encryptor = EncryptionManager()
    return encryptor.encrypt_data(passwords, master_password)


def decrypt_passwords(encrypted_data: str, master_password: str) -> dict:
    """
    Decrypt password data.
    
    Args:
        encrypted_data: Encrypted password data
        master_password: Master password for decryption
        
    Returns:
        Decrypted password dictionary
    """
    encryptor = EncryptionManager()
    return encryptor.decrypt_data(encrypted_data, master_password)
