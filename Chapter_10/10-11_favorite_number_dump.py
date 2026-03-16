from pathlib import Path
import json

# Prompt user for their favorite number
favorite_number = input('Tell me your favorite number: ')

path = Path('txt_files/favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)

