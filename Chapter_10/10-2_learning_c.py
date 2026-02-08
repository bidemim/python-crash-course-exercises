# replace all instance of python in the learning_python.txt file 
# to C(or some other programming language).
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()


new_language = contents.replace('python', 'C')
print(new_language)