# /bin/python3.11
from src.configure_pypswd import PATH  # Import the path of the password file
from src.save_pwd import load_data     # Import the load_data function from the save_pwd module
import pickle                          # Import the pickle module for serialization

def export_as(new_path=r'./default.txt') -> None:
    '''
    Export passwords as a text file.
    
    This function takes the accounts-passwords file
    and exports it to the path specified by the user.

    Args:
    - new_path (str): The destination path of the exported file.
                      By default, './default.txt' is used.
    
    Returns:
    - None
    '''
    # Create a header for the file
    file_content = "ACCOUNT  =>  PASSWORD\n"

    try:
        # Try to open the password file in binary read mode
        with open(PATH, 'rb') as binary_file:
            # Read the data from the file and store it in 'data'
            data = pickle.load(binary_file).items()
            # Iterate over the data and add it to the file content
            for key, value in data:
                file_content += "- {} =>  {} \n".format(key.ljust(12, ' '), value)
        
        # Create a new file at the specified path and write the file content
        with open(new_path, 'w') as new_file:
            new_file.write(file_content)

        # Delete the file_content variable to free memory
        del file_content
        # Print a success message along with the path of the exported file
        print(f"File password exported successfully! on the path { new_path }")
        
    except Exception as err:
        # If an error occurs, print an error message along with the error description
        print(f"[-] An error has occurred: { err }")
