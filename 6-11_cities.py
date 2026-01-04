cities = {
    'san francisco':
        {
        'country': 'usa',
        'population': 827526,
        'fact': 'home of silicon valley',
        },
    'new york':
        {
        'country': 'usa',
        'population': 8478072,
        'fact': 'highest total Asian population of any U.S. city',
        },
    'seoul':
        {
        'country': 'south korea',
        'population' : 25200000,
        'fact': 'largest city in the whole of Korea'
        },
}

for city, info in cities.items():
    country = info['country']
    country = country.upper() if country == 'usa' else country.title()
   
    print(f'\nCity: {city.title()}')
    print(f'\tCountry: {country}')
    population = info['population']
    fact = info['fact']
    print(f'\tPopulation: {population}')
    print(f'\tFact: {fact}')

