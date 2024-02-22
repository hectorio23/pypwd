# /bin/python3.11
from src.configure_pypswd import PATH
from src.save_pwd import load_data
import pickle

def export_as(new_path = r'./default.txt') -> None:
    # file_writer_obj = new file_format()
    file_content = "ACCOUNT  =>  PASSWORD\n"
    """ export file 
        This function takes the accounts-passwords file
        and exports it on the path given by the user
    """
    try: 
        with open(PATH, 'rb') as binary_file:
            # Save the values in the file_content name
            data = pickle.load(binary_file).items()
            for key, value in data:
                file_content += "- {} =>  {} \n".format(key.ljust(12, ' '), value)
        
        # Creates the new file on the path given 
        with open(new_path, 'w') as new_file:
            new_file.write(file_content)

        del file_content
        print(f"File password exported successfully! on the path { new_path }")
        
    except Exception as err:
        print(f"[-] An error has occured: { err }")
