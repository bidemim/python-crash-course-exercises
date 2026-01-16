pet_1 = {'animal': 'dog', 'owner': 'Ade',} 
pet_2 = {'animal': 'cat', 'owner': 'Olu',} 
pet_3  = {'animal': 'parrot', 'owner': 'Ola',} 

pets = [pet_1, pet_2, pet_3]

for index, pet in enumerate(pets, start=1):
    print(f'Pet #{index}:')
    for key, value in pet.items():
        print(f'\t{key.title()}: {value.title()}')
