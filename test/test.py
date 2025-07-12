import json
from pathlib import Path

def load_json_file(file_path):
    try:
        # Usamos Path para mayor robustez cross-platform
        json_text = Path(file_path).read_text(encoding='utf-8')
        
        # Cargamos el JSON
        data = json.loads(json_text)
        
        return data
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{file_path}' no fue encontrado.")
    except json.JSONDecodeError as e:
        print(f"[ERROR] El archivo '{file_path}' no contiene un JSON válido: {e}")
    except Exception as e:
        print(f"[ERROR] Ocurrió un error inesperado: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    json_data = load_json_file("config.json")
    
    if json_data:
        print(f"ruta del archivo: {json_data.get('path') }/{ json_data.get('filename') }.{ json_data.get('extension') }")

