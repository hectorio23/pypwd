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


def load_data():
    try:
        with open('./2038dmf', 'rb') as binary_file:
            for key, value in pickle.load(binary_file).items():
                print('\t {} -> {} '.format(key, value))

    except Exception as error:
        print(f"Has been ocurred an error: {error}")

save_data("Font Awesome", "Yo soy el desarrolllador mdjeu8384874")
load_data()


