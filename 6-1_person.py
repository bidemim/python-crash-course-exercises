person = {
    'first_name': 'Samuel',
    'last_name': 'Jonhson',
    'age': 79,
    'city': 'Los Angeles',
}

for key, value in person.items():
    if isinstance(value, str):
        print(f'{key.title()}: {value.title()}')
    else:
        print(f'{key.title()}: {value}')
