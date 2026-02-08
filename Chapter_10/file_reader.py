# working with the file reader example form the book. 
# this file will be modified several times to show the different examples.
# working with the file from the editor because it requires another file to run.

from pathlib import Path

path = Path('pi_digits.txt')
# contents = path.read_text().rstrip()
contents = path.read_text()

for line in contents.splitlines():
    print(line)
