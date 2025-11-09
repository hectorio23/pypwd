# /bin/python3.11
from src.env import PATH               # Import the path of the password file
from src.save_pwd import DataHandler   # Import the DataHandler class
from src.encryption import get_master_password, decrypt_passwords
from src.Formatter import *
from pathlib import Path


def export_as(new_path=r'./default.txt') -> None:
    """
    Export passwords in various formats.
    
    Args:
        new_path: Destination file path. Format is determined by file extension.
                  Supported formats: json, txt, xml, yaml
    """
    exporters = {
        '.json': JsonExporter(),
        '.txt': TxtExporter(),
        '.xml': XmlExporter(),
        '.yaml': YamlExporter()
    }
    
    extension = Path(new_path).suffix.lower()

    if extension not in exporters:
        print(f"[-] Format not supported: {extension}")
        return

    try:
        master_password = get_master_password()
        content = DataHandler.query_data(master_password)

        exporter = PasswordExporter(exporters[extension])
        exporter.export(content, new_path)

    except Exception as err:
        print(f"[-] Export error: {err}")

