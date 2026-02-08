from pathlib import Path

def read_animal_names(path):
    # print the names of cats and dogs in the cats.txt and dogs.txt files.
    try:
        contents = path.read_text()
    except FileNotFoundError:
        # print(f'Sorry the file {path} does not exist.')
        # failing silently 
        pass
    else:
        # print out each name in each file
        animal_names = contents.split('\n')
        print(animal_names)

filenames = ['cats.txt', 'dogs.txt']  
for filename in filenames:
    path = Path(filename)
    read_animal_names(path)
