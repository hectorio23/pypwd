# /bin/python3.11
from src.configure_pypswd import PATH, ROUTE_FILE
import os
import pickle

def save_data(company, data):
    '''This function only saves the password'''
    try:
        # Try to open the file in binary read and write mode
        with open(PATH, 'rb+') as binary_file:
            try:
                # Try to load existing data
                data_file = pickle.load(binary_file)
            except EOFError:
                # If no data exists, initialize with an empty dictionary
                data_file = {}

            # Add or update the password for the specified company
            data_file[company] = data

            # Return to the beginning of the file and write the updated data
            binary_file.seek(0)
            pickle.dump(data_file, binary_file)

    except Exception as error:
        # If there's an error, create a new file with the provided data
        with open(PATH, 'wb') as binary_file:
            data_save = {company: data}
            pickle.dump(data_save, binary_file)

def load_data(mode='read', item=None):
    '''
    This function does two things: reads and prints the values saved
    on the file or deletes one item from it. The objective with this
    function is to avoid code repetition.
    '''
    try:
        temp_data = None

        # Check if the file exists
        if not os.path.exists(PATH):
            print("The file doesn't exist.")

            # Ask the user if they want to create a new one
            choose = input("Do you want to create a new one? (Y/N): ")

            # Create the directory and file if the user wants to proceed
            if choose.lower() in ("yes", "y"):
                os.makedirs(os.path.dirname(PATH), exist_ok=True)
                print(f"Folder '{os.path.dirname(PATH)}' created successfully.")

                # Create a new file with an empty dictionary
                with open(PATH, 'wb+') as file:
                    pickle.dump({}, file)
                    print("File created successfully.")
                return  # Exit the function after creating the directory and file

            else:
                print(":(")
                return  # Exit the function if the user chooses not to create the directory and file

        # The file exists, proceed with reading or deleting
        with open(PATH, 'rb') as binary_file:
            if mode == 'read':

                # Print the values if the mode is 'read'
                data = pickle.load(binary_file).items()
                for key, value in data:
                    print('\t {} ->     {} '.format(key.ljust(12, ' '), value))
            else:
                # Remove the data stored in the item (it's a key, in fact)
                # if the item has something stored
                data_from_file = pickle.load(binary_file)
                if item and (response := data_from_file.pop(item, None)):
                    temp_data = data_from_file
                else:
                    print("Something was wrong, the item there is not in the collection")

        # Write the modified data back to the file
        if temp_data:
            with open(PATH, 'wb') as file:
                pickle.dump(temp_data, file)
                print("Data deleted successfully")

    except Exception as error:
        print(f"Error: {error}")

# Example usage
# save_data('company_a', 'password123')  # Save a password (uncomment to test)
# load_data(mode='read')  # Read and print the values
# load_data(mode='delete', item='company_a')  # Delete an item (uncomment to test)
