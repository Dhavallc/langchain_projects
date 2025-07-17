import json
import sys

def validate_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Valid JSON file: {file_path}")
        return True
    except json.JSONDecodeError as e:
        print(f" Invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print(f" File not found: {file_path}")
        return False
    except Exception as e:
        print(f" Error reading file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python validate_json.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    validate_json_file(file_path)

