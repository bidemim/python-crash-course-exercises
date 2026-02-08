from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

# read all contents of the learning_python file
learning_string= ''
for line in contents.splitlines():
    learning_string += line

# print contents and loop it line by line   
print(f'\n{learning_string}')
# print all contents in one line
print(f'\n{contents}')

