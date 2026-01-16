# modifying previous code to conform with PE 8 
cute_animals = ['cats', 'parrots', 'dogs']
print([animal for animal in cute_animals])

for animal in cute_animals:
    print(f'{animal.title()} are cute animals.')

# added "editor.rulers": [80], to settings.json file. 
print(f'{cute_animals[0].title()} and {cute_animals[1]} are cute\
when they want to be. {cute_animals[2].title()} are always cool.')