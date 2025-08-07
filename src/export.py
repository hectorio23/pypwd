# /bin/python3.11
from src.env import PATH               # Import the path of the password file
from src.save_pwd import load_data     # Import the load_data function from the save_pwd module
import pickle                          # Import the pickle module for serialization
from src.Formatter import *
from pathlib import Path


def export_as(new_path=r'./default.txt') -> None:
    '''
    Export passwords in various formats from the binary file.

    Args:
    - new_path (str): Destination file path.
    - default_format (str): One of ['json', 'txt', 'xml', 'yaml']

    Returns:
    - None
    '''
    exporters = {
        '.json': JsonExporter(),
        '.txt': TxtExporter(),
        '.xml': XmlExporter(),
        '.yaml': YamlExporter()
    }
    
    extension = Path(new_path).suffix.lower()

    if extension not in exporters:
        print(f"[-] Formatt not supported!: { extension }")
        return

    try:
        with open(PATH, 'rb') as binary_file:
            content = pickle.load(binary_file)

        exporter = PasswordExporter(exporters[extension])

        exporter.export(content, new_path)

    except Exception as err:
        print(f"[-] Has been an error for exporting: {err}")

