# this code is copied from the file_reader.py file from the book. 
# all examples are kept in this chapter as they are required 
# to work through exercises.

from pathlib import Path

path = Path('txt_files/pi_digits.txt')
# contents = path.read_text().rstrip()
contents = path.read_text()

# this line attempts to write simpler and more concise code by 
# not creating a 'lines' variable.
for line in contents.splitlines():
    print(line)