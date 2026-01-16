# code from 6-1 with two more people
people = [ 
    {
        'first_name': 'Samuel',
        'last_name': 'Jonhson',
        'age': 79,
        'city': 'Los Angeles',
    },

    {
        'first_name': 'Danielle',
        'last_name': 'Wale',
        'age': 41,
        'city': 'San Francisco',
    },

    {
        'first_name': 'Monica',
        'last_name': 'Williams',
        'age': 32,
        'city': 'New York',
    }
]

for index, person in enumerate(people, start=1):
    name = f'{person['first_name']} {person['last_name']}'
    print(f'\nName: {name}') 
    age = person['age']
    city = person['city']
    print(f'Age: {age}')
    print(f'City: {city}')
