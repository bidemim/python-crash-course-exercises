from pathlib import Path
import json

def show_favorite_number(path):
    # load favorite number if avaialable.
    path = Path('txt_files/favorite_number.json')
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None

def get_favorite_number():
    # Get user's favorite number
    path = Path('favorite_number.json')
    favorite_number = show_favorite_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:  
        favorite_number = input('Tell me your favorite number: ')   
        contents = json.dumps(favorite_number)
        path.write_text(contents)
        print(f"I know your favorite number! It's {favorite_number}.")

get_favorite_number()
