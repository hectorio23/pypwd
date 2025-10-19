# /bin/python3.11
"""
Encryption module for PYPWD password manager.
Implements AES-256 encryption with PBKDF2 key derivation.
"""

import os
import base64
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import json


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
        else:
            # Generate a new random salt
            salt = os.urandom(32)  # 256-bit salt
            with open(self.salt_file, 'wb') as f:
                f.write(salt)
            # Set restrictive permissions on salt file
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
            length=32,  # 256 bits
            salt=self.salt,
            iterations=100000,  # High iteration count for security
            backend=default_backend()
        )
        return kdf.derive(master_password.encode('utf-8'))
    
    def encrypt_data(self, data: dict, master_password: str) -> str:
        """
        Encrypt password data using AES-256.
        
        Args:
            data: Dictionary containing password data
            master_password: Master password for encryption
            
        Returns:
            Base64 encoded encrypted data
        """
        key = self._derive_key(master_password)
        
        # Convert data to JSON string
        json_data = json.dumps(data).encode('utf-8')
        
        # Generate random IV
        iv = os.urandom(16)
        
        # Create cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Pad data to block size (16 bytes for AES)
        padding_length = 16 - (len(json_data) % 16)
        padded_data = json_data + bytes([padding_length] * padding_length)
        
        # Encrypt data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine IV and encrypted data, then encode
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
            
            # Decode base64 data
            combined = base64.b64decode(encrypted_data.encode('utf-8'))
            
            # Separate IV and encrypted data
            iv = combined[:16]
            encrypted = combined[16:]
            
            # Create cipher
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            
            # Decrypt data
            decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
            
            # Remove padding
            padding_length = decrypted_padded[-1]
            decrypted_data = decrypted_padded[:-padding_length]
            
            # Convert back to dictionary
            return json.loads(decrypted_data.decode('utf-8'))
            
        except Exception as e:
            raise ValueError(f"Decryption failed. Check your master password: {e}")
    
    def verify_master_password(self, master_password: str) -> bool:
        """
        Verify if the provided master password is correct.
        
        Args:
            master_password: Password to verify
            
        Returns:
            True if password is correct, False otherwise
        """
        try:
            # Try to decrypt with the provided password
            # If it fails, the password is wrong
            return True  # This will be implemented when we have encrypted data
        except:
            return False


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
