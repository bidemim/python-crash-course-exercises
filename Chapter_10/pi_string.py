# working with the file reader example form the book. 
# this file will be modified several times to show the different examples.
# working with the file from the editor because it requires another file to run.

from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f'{pi_string[:52]}...')
print(len(pi_string))