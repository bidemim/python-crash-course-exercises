# this code is copied from the file_reader.py file from the book. 
# all examples are kept in this chapter as they are required 
# to work through exercises.

from pathlib import Path

path = Path('pi_digits.txt')
# contents = path.read_text().rstrip()
contents = path.read_text()
# this exercise is to write simpler and more concise code by 
# skipping the lines variable.
for line in contents.splitlines():
    print(line)

