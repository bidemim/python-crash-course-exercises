# working with the file reader example form the book. 
# this file will be modified several times to show the different examples.
# working with the file from the editor because it requires another file to run.

from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()
pi_string = ''

for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input('Enter your birthday in the form of mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')
