from pathlib import Path
import json
import subprocess

user = subprocess.run(["whoami"], capture_output=True, text=True).stdout.strip()
file_path = f"/home/{ user }/Desktop/pypwd/src/config.json"

try:
    json_text = Path(file_path).read_text(encoding='utf-8')
        
    data = json.loads(json_text)
        
except FileNotFoundError:
    print(f"[ERROR] The file '{ file_path }' was not found!.")

except json.JSONDecodeError as e:
    print(f"[ERROR] The file '{ file_path }' is not a JSON format valid!: {e}")
except Exception as e:
    print(f"[ERROR] There was an error: {e}")

    
PATH = data['path'].replace("USER", user)
FILENAME = data['filename']
EXTENSION = data['extension']
FORMAT = data['default_format']
