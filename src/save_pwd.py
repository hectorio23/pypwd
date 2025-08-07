# /bin/python3.11
from src.env import PATH  
import pickle
import os

class Formatter:
    @staticmethod
    def json(content: dict):
        counter = 1
        for key, value in content.items():
            print('[{}] {} ->     {} '.format(counter, key.ljust(12, ' '), value))
            counter += 1


class DataHandler:
    ''' Class DataHandler
    The main porpouse of this class is the 
    magnament of the users data, this class 
    allowed to us to save and query the passwords.
    '''
    @staticmethod
    def create_file():
        
        # Crate the folerd's file 
        os.makedirs(os.path.dirname(PATH), exist_ok=True)
        print(f"Folder '{os.path.dirname(PATH)}' created successfully.")

        # Create a new file with an empty dictionary
        with open(PATH, 'wb+') as file:
            pickle.dump({}, file)
            print("File created successfully.")


    @staticmethod
    def data_saver(company: str, data: str, data_save={ }) -> None:
        with open(PATH, 'rb+') as binary_file:
            data_save[company] = data
            pickle.dump(data_save, binary_file)
        

    @staticmethod
    def query_data(flag=False):
        # Try to open the file in binary read and write mode
        with open(PATH, 'rb+') as binary_file:
            try:
                # Try to load existing data
                data_file = pickle.load(binary_file)

                if data_file == { } and command:
                    print("UPSS There's nothing here yet! ")

            except EOFError:
                # If no data exists, initialize with an empty dictionary
                data_file = {}
                # print("UPSS There's nothing here yet! ")
            
        return data_file

    
    @staticmethod
    def delete_element(key):
        elements = DataHandler.query_data()
        elements.pop(key, None)

        with open(PATH, 'wb') as storage:
            pickle.dump(elements, storage)

        print("Element deleted successfully")



def save_data(company, data):
    '''This function only saves the password'''
    try:
        user_content = DataHandler.query_data()
        DataHandler.data_saver(company, data, user_content)

    except Exception as error:
        DataHandler.data_saver(company, data)


def load_data(mode='read', item=None):
    try:
        response = DataHandler.query_data()
    except:
        DataHandler.create_file()
        response = DataHandler.query_data()

    Formatter.json(response)


# Example usage
# save_data('company_a', 'password123')  # Save a password (uncomment to test)
# load_data(mode='read')  # Read and print the values
# load_data(mode='delete', item='company_a')  # Delete an item (uncomment to test)
