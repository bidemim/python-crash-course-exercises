from pathlib import Path

contents = 'I love programming.\n'
contents += 'I love creating new games. \n'
contents += 'I also love working with data. \n'

# python will create a txt file if it doesn't exist.
# and overwrite the existing content when the programme is run.
path = Path('programming.txt')
path.write_text(contents)