# /bin/python3.11
from src.env import PATH  
import os
from src.encryption import encrypt_passwords, decrypt_passwords, get_master_password, setup_master_password

class Formatter:
    @staticmethod
    def json(content: dict):
        counter = 1
        for key, value in content.items():
            print('[{}] {} ->     {} '.format(counter, key.ljust(12, ' '), value))
            counter += 1


class DataHandler:
    """
    Handles password data storage and retrieval operations.
    Manages encrypted password file operations including save, query, and delete.
    """
    @staticmethod
    def create_file():
        """Initialize encrypted password storage file and set up master password."""
        os.makedirs(os.path.dirname(PATH), exist_ok=True)
        print(f"Folder '{os.path.dirname(PATH)}' created successfully.")

        master_password = setup_master_password()
        encrypted_data = encrypt_passwords({}, master_password)
        
        with open(PATH, 'w') as file:
            file.write(encrypted_data)
        print("Encrypted file created successfully.")


    @staticmethod
    def data_saver(company: str, data: str, data_save={ }, master_password: str = None) -> None:
        """Save password data to encrypted storage."""
        if master_password is None:
            master_password = get_master_password()
        
        data_save[company] = data
        encrypted_data = encrypt_passwords(data_save, master_password)
        
        with open(PATH, 'w') as file:
            file.write(encrypted_data)
        

    @staticmethod
    def query_data(master_password: str = None):
        """Load and decrypt password data."""
        if master_password is None:
            master_password = get_master_password()
        
        try:
            with open(PATH, 'r') as file:
                encrypted_data = file.read()
            
            # Decrypt the data
            data_file = decrypt_passwords(encrypted_data, master_password)
            
            if data_file == {}:
                print("There's nothing here yet!")
            
            return data_file
            
        except FileNotFoundError:
            print("Password file not found. This appears to be your first time using PYPWD!")
            print("Please run: python pypwd.py --setup")
            print("This will help you set up your master password.")
            return {}
        except Exception as e:
            if "Decryption failed" in str(e):
                print("Wrong master password! Please try again.")
                print("If you forgot your master password, you'll need to start over.")
                print("Run: python pypwd.py --setup (this will reset all passwords)")
            else:
                print(f"Error loading passwords: {e}")
            return {}

    
    @staticmethod
    def delete_element(key, master_password: str = None):
        """Delete a password entry from storage."""
        if master_password is None:
            master_password = get_master_password()
            
        elements = DataHandler.query_data(master_password)
        elements.pop(key, None)

        encrypted_data = encrypt_passwords(elements, master_password)
        with open(PATH, 'w') as storage:
            storage.write(encrypted_data)

        print("Element deleted successfully")



def save_data(company, data, master_password: str = None):
    """Save a password entry for the given company/service."""
    try:
        if master_password is None:
            master_password = get_master_password()
            
        user_content = DataHandler.query_data(master_password)
        DataHandler.data_saver(company, data, user_content, master_password)

    except Exception as error:
        print(f"Error saving password: {error}")
        DataHandler.data_saver(company, data, master_password=master_password)


def load_data(mode='read', item=None, master_password: str = None):
    """Load and display all stored passwords."""
    try:
        if master_password is None:
            master_password = get_master_password()
        response = DataHandler.query_data(master_password)
    except:
        DataHandler.create_file()
        response = DataHandler.query_data(master_password)

    Formatter.json(response)


# Example usage
# save_data('company_a', 'password123')  # Save a password (uncomment to test)
# load_data(mode='read')  # Read and print the values
# load_data(mode='delete', item='company_a')  # Delete an item (uncomment to test)
