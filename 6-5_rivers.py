major_rivers = {
    'nile': 'egypt',
    'mississipi' : 'usa',
    'niger': 'nigeria',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in major_rivers.items():
    country = country.upper() if country == 'usa' else country.title()
    print(f'The {river.title()} runs through {country}.')

for river in major_rivers:
    print(river.title())
for country in major_rivers.values():
    print(country.title())