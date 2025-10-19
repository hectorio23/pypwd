# /bin/python3.11
from src.env import PATH               # Import the path of the password file
from src.save_pwd import DataHandler   # Import the DataHandler class
from src.encryption import get_master_password, decrypt_passwords
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
        # Get master password for decryption
        master_password = get_master_password()
        
        # Load and decrypt the password data
        content = DataHandler.query_data(master_password)

        exporter = PasswordExporter(exporters[extension])

        exporter.export(content, new_path)

    except Exception as err:
        print(f"[-] Has been an error for exporting: {err}")

