# /bin/python3.11
import pickle

def save_data(company, data):
    try:
        passwords = {}
        with open('./2038dmf', 'rb+') as binary_file:
            data_file = pickle.load(binary_file)
            data_file[company] = data
            passwords = data_file

        with open('./2038dmf', "wb") as binary_file:
            pickle.dump(passwords, binary_file)

    except Exception as error:
        with open('./2038dmf', 'wb') as binary_file:
            data_save = {company:data}
            pickle.dump(data_save, binary_file)

# This function do two thing, read and print the values saved
# on the file or delete one item from it, the objetive with This
# function is not repeat code
def load_data(mode = 'read', item = None):
    try:
        temp_data = None
        with open('./2038dmf', 'rb') as binary_file:
            # Just print the values if the mode is on read
            # In the future I will implement more funcionalities in <mode>
            if mode == 'read':
                for key, value in pickle.load(binary_file).items():
                    print('\t {} ->     {} '.format(key.ljust(12, ' '), value))
            else:

                # Remove de data storaged in the item (its a key in fact)
                # if item has something storage 
                data_from_file = pickle.load(binary_file)
                if item and (response := data_from_file.pop(item, None)):
                    temp_data = data_from_file
                else:
                    print("Something was wrong, the item tere is not in the collection")
        if temp_data:
            with open('./2038dmf', 'wb') as file:
                pickle.dump(temp_data, file)
                print("Data deleted successfully")

    except Exception as error:
        print(f"Has been ocurred an error: {error}")

