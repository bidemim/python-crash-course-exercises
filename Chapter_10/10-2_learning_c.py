# replace all instance of python in the learning_python.txt file 
# to C(or some other programming language).

from pathlib import Path

path = Path('txt_files/learning_python.txt')
contents = path.read_text()

new_language = contents.replace('python', 'C')
print(f'\n{new_language}')