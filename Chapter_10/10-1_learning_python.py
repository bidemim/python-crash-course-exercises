from pathlib import Path

path = Path('txt_files/learning_python.txt')
contents = path.read_text()

# read all contents of the learning_python file
print(f'\n{contents}')

learning_string= ''
# print contents and loop it line by line  
for line in contents.splitlines():
    learning_string += line
    
print(f'\n{learning_string}')